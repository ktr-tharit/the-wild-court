import rawBundle from "./game-data.generated.json";

export type Evidence = Record<string, number>;
export type WeightedEvidence = { construct: string; value: number; weight: number; role: string };
export type GameOption = { id: string; copy: string; evidence: Evidence; consequence_tags?: string[] };
export type BoundaryOption = Omit<GameOption, "evidence"> & { evidence: WeightedEvidence[] };
export type GameQuestion = {
  id: string; act: string; title: string; scenario: string; targets: string[];
  options: GameOption[]; setup?: string; transition_after?: string; location?: string;
  intensity?: string; scene_order?: number; discriminates?: string[];
};
export type BoundaryQuestion = Omit<GameQuestion, "options"> & {
  domain: string;
  constructs: string[];
  options: BoundaryOption[];
};
export type ScoringAnimal = { realm: string; core: number[]; facets: number[] };
export type ScoringModel = {
  model_version: string;
  classification_policy: "soft_realm_then_conditional_animal";
  core_dimensions: string[];
  motive_facets: string[];
  construct_weights: Record<string, number>;
  confidence_targets: Record<string, number>;
  animal_softmax_temperature: number;
  realm_pooling: "mean_animal_likelihood";
  prior_policy: "equal_realm_then_equal_animal";
  animals: Record<string, ScoringAnimal>;
  response_softmax_temperature: number;
  max_adaptive_questions: number;
  minimum_information_gain: number;
  require_adaptive_domain_diversity: boolean;
};
export type ResultIdentity = {
  title: string; identity_promise: string; short_result: string; share_line: string;
  signatures: string[]; bible: string; full_result: string | null;
  patterns: {
    what_moves_you: string; how_you_connect: string; how_you_protect: string;
    when_winter_closes_in: string; what_you_rarely_ask_for: string;
  };
  misunderstanding: string; restoring_balance: string; realm_connection: string; closing: string;
};
export type GameBundle = {
  title: string; player_role: string; opening: string[];
  acts: Record<string, { title: string; intro: string; outro: string }>;
  judgment: { intro: string; transition_to_result: string };
  core_scenes: GameQuestion[]; adaptive_questions: GameQuestion[];
  boundary_questions: BoundaryQuestion[];
  dimensions: { id: string; negative: string; positive: string }[];
  animals: Record<string, { kingdom: string; vector: number[]; design_note: string }>;
  realms: Record<string, { name: string; title: string; belief: string }>;
  results: Record<string, ResultIdentity>;
  scoring: ScoringModel;
};

export type ScoringResponse = { evidence: Evidence | WeightedEvidence[] };
export type SoftmaxResult = {
  estimates: Record<string, number>;
  confidence: Record<string, number>;
  animal_probabilities: Record<string, number>;
  realm_probabilities: Record<string, number>;
  conditional_animal_probabilities: Record<string, Record<string, number>>;
  distances: Record<string, number>;
  realm_scores: Record<string, number>;
  ranking: string[];
  within_realm_ranking: string[];
  top_animal: string;
  top_realm: string;
  top_margin: number;
};
export type BoundarySelection = { question: BoundaryQuestion; information_gain: number };

export type PlayableQuestion = GameQuestion | (BoundaryQuestion & { act: "Judgment"; location: string });
export type ResponseRecord = { question_id: string; act: string; option_id: string; evidence: Evidence | WeightedEvidence[]; consequence_tags: string[] };
export type GameResult = {
  realm: { name: string; title: string; belief: string };
  primary_animal: string;
  identity: ResultIdentity;
  callbacks: string[];
  questions_answered: number;
  adaptive_questions_answered: number;
  internal: { vector: Record<string, number>; ranking: string[]; distances: Record<string, number>; responses: ResponseRecord[] };
};
export type Evaluation = {
  answers: string[];
  current: PlayableQuestion | null;
  phase: string;
  core_answered: number;
  judgment_total: number;
  judgment_answered: number;
  tags: Record<string, number>;
  callbacks: string[];
  result: GameResult | null;
};

export const gameBundle = rawBundle as unknown as GameBundle;

const motiveFacets = new Set(["REC", "MAS", "RCP", "CON", "RST"]);

function weightedEvidence(evidence: Evidence | WeightedEvidence[]): WeightedEvidence[] {
  if (Array.isArray(evidence)) return evidence;
  return Object.entries(evidence).map(([construct, value]) => ({
    construct, value, weight: 1, role: "primary",
  }));
}

function scoringProfiles(model: ScoringModel) {
  const constructs = [...model.core_dimensions, ...model.motive_facets];
  return Object.fromEntries(Object.entries(model.animals).map(([name, animal]) => [
    name,
    Object.fromEntries(constructs.map((construct, index) => [
      construct,
      [...animal.core, ...animal.facets][index],
    ])),
  ])) as Record<string, Record<string, number>>;
}

function estimateConstructs(responses: ScoringResponse[], model: ScoringModel) {
  const sums = Object.fromEntries(model.core_dimensions.map((construct) => [construct, 0])) as Record<string, number>;
  const evidenceWeights = Object.fromEntries(model.core_dimensions.map((construct) => [construct, 0])) as Record<string, number>;
  responses.forEach((response) => weightedEvidence(response.evidence).forEach((item) => {
    if (!(item.construct in sums) || motiveFacets.has(item.construct)) return;
    sums[item.construct] += item.value * item.weight;
    evidenceWeights[item.construct] += item.weight;
  }));
  const estimates: Record<string, number> = {};
  const confidence: Record<string, number> = {};
  model.core_dimensions.forEach((construct) => {
    if (evidenceWeights[construct] <= 0) return;
    estimates[construct] = sums[construct] / evidenceWeights[construct];
    confidence[construct] = Math.min(1, evidenceWeights[construct] / model.confidence_targets[construct]);
  });
  return { estimates, confidence };
}

export function scoreResponses(
  responses: ScoringResponse[],
  bundle: GameBundle = gameBundle,
): SoftmaxResult {
  const model = bundle.scoring;
  const profiles = scoringProfiles(model);
  const { estimates, confidence } = estimateConstructs(responses, model);
  const distances: Record<string, number> = {};
  const distanceTo = (profile: Record<string, number>) => {
    const terms = Object.keys(estimates).map((construct) => ({
      construct,
      weight: model.construct_weights[construct] * confidence[construct],
    })).filter(({ construct }) => construct in profile);
    const denominator = terms.reduce((sum, item) => sum + item.weight, 0);
    return denominator
      ? terms.reduce((sum, item) => sum + item.weight * (estimates[item.construct] - profile[item.construct]) ** 2, 0) / denominator
      : 0;
  };

  const realmAnimals: Record<string, string[]> = {};
  Object.entries(model.animals).forEach(([animal, profile]) => {
    (realmAnimals[profile.realm] ??= []).push(animal);
    distances[animal] = distanceTo(profiles[animal]);
  });
  const logits = Object.fromEntries(Object.entries(distances).map(([animal, distance]) => [
    animal, -distance / model.animal_softmax_temperature,
  ]));
  const peak = Math.max(...Object.values(logits));
  const likelihoods = Object.fromEntries(Object.entries(logits).map(([animal, value]) => [
    animal, Math.exp(value - peak),
  ]));
  const realmScores = Object.fromEntries(Object.entries(realmAnimals).map(([realm, animals]) => [
    realm,
    animals.reduce((sum, animal) => sum + likelihoods[animal], 0) / animals.length,
  ]));
  const realmTotal = Object.values(realmScores).reduce((sum, score) => sum + score, 0);
  const realmProbabilities = Object.fromEntries(Object.entries(realmScores).map(([realm, score]) => [
    realm, score / realmTotal,
  ]));
  const conditionalAnimalProbabilities: Record<string, Record<string, number>> = {};
  Object.entries(realmAnimals).forEach(([realm, animals]) => {
    const total = animals.reduce((sum, animal) => sum + likelihoods[animal], 0);
    conditionalAnimalProbabilities[realm] = Object.fromEntries(animals.map((animal) => [
      animal, likelihoods[animal] / total,
    ]));
  });
  const animalProbabilities = Object.fromEntries(Object.entries(model.animals).map(([animal, profile]) => [
    animal,
    realmProbabilities[profile.realm] * conditionalAnimalProbabilities[profile.realm][animal],
  ]));
  const ranking = Object.keys(animalProbabilities).sort((left, right) => animalProbabilities[right] - animalProbabilities[left]);
  const topRealm = Object.keys(realmProbabilities).sort((left, right) => realmProbabilities[right] - realmProbabilities[left])[0];
  const withinRealmRanking = [...realmAnimals[topRealm]].sort((left, right) =>
    conditionalAnimalProbabilities[topRealm][right] - conditionalAnimalProbabilities[topRealm][left]);
  const topAnimal = withinRealmRanking[0];
  return {
    estimates,
    confidence,
    animal_probabilities: animalProbabilities,
    realm_probabilities: realmProbabilities,
    conditional_animal_probabilities: conditionalAnimalProbabilities,
    distances,
    realm_scores: realmScores,
    ranking,
    within_realm_ranking: withinRealmRanking,
    top_animal: topAnimal,
    top_realm: topRealm,
    top_margin: conditionalAnimalProbabilities[topRealm][withinRealmRanking[0]]
      - conditionalAnimalProbabilities[topRealm][withinRealmRanking[1]],
  };
}

function optionProbabilities(
  profile: Record<string, number>,
  question: BoundaryQuestion,
  temperature: number,
) {
  const utilities = question.options.map((option) => {
    const evidence = option.evidence.filter((item) => !motiveFacets.has(item.construct));
    const totalWeight = evidence.reduce((sum, item) => sum + item.weight, 0);
    const squaredError = evidence.reduce((sum, item) =>
      sum + item.weight * (profile[item.construct] - item.value) ** 2, 0) / totalWeight;
    return -squaredError / temperature;
  });
  const peak = Math.max(...utilities);
  const exponentials = utilities.map((value) => Math.exp(value - peak));
  const total = exponentials.reduce((sum, value) => sum + value, 0);
  return exponentials.map((value) => value / total);
}

function entropy(probabilities: Record<string, number>) {
  return -Object.values(probabilities).reduce((sum, probability) =>
    probability > 0 ? sum + probability * Math.log(probability) : sum, 0);
}

export function expectedInformationGain(
  animalProbabilities: Record<string, number>,
  question: BoundaryQuestion,
  bundle: GameBundle = gameBundle,
) {
  const profiles = scoringProfiles(bundle.scoring);
  const likelihoods = Object.fromEntries(Object.entries(profiles).map(([animal, profile]) => [
    animal,
    optionProbabilities(profile, question, bundle.scoring.response_softmax_temperature),
  ])) as Record<string, number[]>;
  let expectedEntropy = 0;
  question.options.forEach((_, optionIndex) => {
    const optionProbability = Object.entries(animalProbabilities).reduce((sum, [animal, probability]) =>
      sum + probability * likelihoods[animal][optionIndex], 0);
    if (optionProbability <= 0) return;
    const posterior = Object.fromEntries(Object.entries(animalProbabilities).map(([animal, probability]) => [
      animal,
      probability * likelihoods[animal][optionIndex] / optionProbability,
    ]));
    expectedEntropy += optionProbability * entropy(posterior);
  });
  return entropy(animalProbabilities) - expectedEntropy;
}

export function selectNextBoundaryQuestion(
  responses: ScoringResponse[],
  askedQuestionIds: string[] = [],
  usedDomains: string[] = [],
  bundle: GameBundle = gameBundle,
): BoundarySelection | null {
  const model = bundle.scoring;
  if (askedQuestionIds.length >= model.max_adaptive_questions) return null;
  const result = scoreResponses(responses, bundle);
  const candidates = bundle.boundary_questions.filter((question) =>
    !askedQuestionIds.includes(question.id)
    && (!model.require_adaptive_domain_diversity || !usedDomains.includes(question.domain)));
  const ranked = candidates.map((question) => ({
    question,
    information_gain: expectedInformationGain(result.animal_probabilities, question, bundle),
  })).sort((left, right) =>
    right.information_gain - left.information_gain || right.question.id.localeCompare(left.question.id));
  const selection = ranked[0];
  return selection && selection.information_gain >= model.minimum_information_gain ? selection : null;
}

const tagCallbacks: Record<string, string> = {
  acted_alone: "เมื่อคนอื่นลังเล คุณมักเริ่มจากพื้นที่ที่ตัวเองรับผิดชอบได้",
  gathered_people: "เมื่อสถานการณ์แตกออก คุณมักพยายามทำให้ผู้คนกลับมาเคลื่อนไหวร่วมกัน",
  trusted_instinct: "คุณยอมรับข้อมูลที่ร่างกายและประสบการณ์มองเห็นก่อนจะอธิบายได้ทั้งหมด",
  checked_evidence: "ก่อนฝากน้ำหนักไว้กับข้อสรุป คุณมักต้องการเห็นว่าหลักฐานเชื่อมกันอย่างไร",
  kept_structure: "ภายใต้แรงกดดัน คุณสร้างขอบเขต ลำดับ หรือทางสำรองให้สิ่งต่าง ๆ ยังเดินต่อ",
  adapted_in_motion: "คุณยอมให้คำตอบเปลี่ยนไปพร้อมสถานการณ์ แทนที่จะรักษาแผนเพียงเพราะเคยวางไว้",
  protected_bond: "เมื่อหลักการชนกับชีวิตจริง คุณมองเห็นน้ำหนักของความสัมพันธ์เฉพาะหน้า",
  protected_principle: "คุณพยายามรักษาหลักที่สามารถอธิบายและใช้กับทุกคนได้",
  showed_feeling: "คุณยอมให้สิ่งที่รู้สึกกลายเป็นข้อมูลซึ่งคนอื่นมองเห็น",
  held_feeling: "คุณมักถือความรู้สึกไว้ภายในจนกว่าจะรู้ว่าการเปิดเผยมันจำเป็น",
  stepped_forward: "เมื่อ direction ว่างลง คุณพร้อมรับผิดชอบการขยับครั้งถัดไป",
  supported_others: "คุณมองหาเจ้าของ direction ที่เหมาะสม และช่วยให้เขาทำหน้าที่ได้ดีขึ้น",
  self_authored: "คุณต้องยอมรับการตัดสินใจนั้นด้วยตัวเอง ก่อนบทบาทหรือธรรมเนียมจะมีอำนาจเหนือคุณ",
  honored_duty: "เมื่อรับบางสิ่งเป็นหน้าที่แล้ว คุณให้ความต่อเนื่องของคำมั่นมีน้ำหนักจริง",
  kept_known: "คุณรักษาสิ่งที่พิสูจน์แล้ว เมื่อความเสียหายจากการลองผิดอาจสูงเกินไป",
  took_risk: "คุณยอมเปิดทางใหม่ เมื่อเส้นทางเดิมไม่พอจะพาใครไปถึงอนาคต",
};

function optionFor(question: PlayableQuestion, optionId: string) {
  return question.options.find((option) => option.id === optionId.toUpperCase()) ?? question.options[0];
}

function responseFor(question: PlayableQuestion, optionId: string): ResponseRecord {
  const option = optionFor(question, optionId);
  return { question_id: question.id, act: question.act, option_id: option.id, evidence: option.evidence, consequence_tags: option.consequence_tags ?? [] };
}

function callbacksFrom(tags: Record<string, number>) {
  return Object.entries(tags)
    .sort(([leftTag, leftCount], [rightTag, rightCount]) => rightCount - leftCount || leftTag.localeCompare(rightTag))
    .slice(0, 3)
    .map(([tag]) => tagCallbacks[tag])
    .filter(Boolean);
}

function asJudgmentQuestion(question: BoundaryQuestion, bundle: GameBundle): PlayableQuestion {
  return { ...question, act: "Judgment", setup: bundle.judgment.intro, location: "Hall of Judgment" };
}

export function evaluateAnswers(answerIds: string[], bundle: GameBundle = gameBundle): Evaluation {
  const acceptedAnswers: string[] = [];
  const responses: ResponseRecord[] = [];
  const tags: Record<string, number> = {};
  const coreCount = bundle.core_scenes.length;

  bundle.core_scenes.forEach((question, index) => {
    if (index >= answerIds.length) return;
    const option = optionFor(question, answerIds[index]);
    acceptedAnswers.push(option.id);
    const response = responseFor(question, option.id);
    responses.push(response);
    response.consequence_tags.forEach((tag) => { tags[tag] = (tags[tag] ?? 0) + 1; });
  });

  if (acceptedAnswers.length < coreCount) {
    return { answers: acceptedAnswers, current: bundle.core_scenes[acceptedAnswers.length], phase: bundle.core_scenes[acceptedAnswers.length].act, core_answered: acceptedAnswers.length, judgment_total: 0, judgment_answered: 0, tags, callbacks: callbacksFrom(tags), result: null };
  }

  const scoringResponses: ScoringResponse[] = responses.map(({ evidence }) => ({ evidence }));
  const askedQuestionIds: string[] = [];
  const usedDomains: string[] = [];
  const extraAnswers = answerIds.slice(coreCount, coreCount + bundle.scoring.max_adaptive_questions);
  for (const answer of extraAnswers) {
    const selection = selectNextBoundaryQuestion(scoringResponses, askedQuestionIds, usedDomains, bundle);
    if (!selection) break;
    const question = asJudgmentQuestion(selection.question, bundle);
    const option = optionFor(question, answer);
    acceptedAnswers.push(option.id);
    const response = responseFor(question, option.id);
    responses.push(response);
    scoringResponses.push({ evidence: response.evidence });
    askedQuestionIds.push(question.id);
    usedDomains.push(selection.question.domain);
  }

  const nextSelection = selectNextBoundaryQuestion(scoringResponses, askedQuestionIds, usedDomains, bundle);
  if (nextSelection) {
    return {
      answers: acceptedAnswers,
      current: asJudgmentQuestion(nextSelection.question, bundle),
      phase: "Judgment",
      core_answered: coreCount,
      judgment_total: askedQuestionIds.length + 1,
      judgment_answered: askedQuestionIds.length,
      tags,
      callbacks: callbacksFrom(tags),
      result: null,
    };
  }

  const scored = scoreResponses(scoringResponses, bundle);
  const primary = scored.top_animal;
  const result: GameResult = {
    realm: bundle.realms[scored.top_realm],
    primary_animal: primary,
    identity: bundle.results[primary],
    callbacks: callbacksFrom(tags),
    questions_answered: responses.length,
    adaptive_questions_answered: askedQuestionIds.length,
    internal: {
      vector: Object.fromEntries(bundle.scoring.core_dimensions.map((id) => [id, scored.estimates[id] ?? 0])),
      ranking: scored.ranking,
      distances: scored.distances,
      responses,
    },
  };
  return { answers: acceptedAnswers, current: null, phase: "Result", core_answered: coreCount, judgment_total: askedQuestionIds.length, judgment_answered: askedQuestionIds.length, tags, callbacks: result.callbacks, result };
}

export function bestAnswerForAnimal(question: PlayableQuestion, animal: string, bundle: GameBundle = gameBundle) {
  const profile = bundle.scoring.animals[animal];
  const values = Object.fromEntries([...bundle.scoring.core_dimensions, ...bundle.scoring.motive_facets].map((id, index) => [id, [...profile.core, ...profile.facets][index]]));
  const optionDistance = (option: GameOption | BoundaryOption) => {
    const evidence = weightedEvidence(option.evidence).filter((item) => item.construct in values);
    const denominator = evidence.reduce((sum, item) => sum + item.weight, 0);
    return evidence.reduce((sum, item) => sum + item.weight * (values[item.construct] - item.value) ** 2, 0) / denominator;
  };
  return question.options.reduce((best, option) => {
    return optionDistance(option) < optionDistance(best) ? option : best;
  }, question.options[0]).id;
}

export function runAnimalFixture(animal: string, bundle: GameBundle = gameBundle) {
  const answers: string[] = [];
  let evaluation = evaluateAnswers(answers, bundle);
  while (!evaluation.result) {
    if (!evaluation.current) throw new Error("Fixture reached an invalid state");
    answers.push(bestAnswerForAnimal(evaluation.current, animal, bundle));
    evaluation = evaluateAnswers(answers, bundle);
  }
  return evaluation;
}
