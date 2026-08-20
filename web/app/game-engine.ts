import rawBundle from "./game-data.generated.json";

export type Evidence = Record<string, number>;
export type GameOption = { id: string; copy: string; evidence: Evidence; consequence_tags?: string[] };
export type GameQuestion = {
  id: string; act: string; title: string; scenario: string; targets: string[];
  options: GameOption[]; setup?: string; transition_after?: string; location?: string;
  intensity?: string; scene_order?: number; discriminates?: string[];
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
  dimensions: { id: string; negative: string; positive: string }[];
  animals: Record<string, { kingdom: string; vector: number[]; design_note: string }>;
  realm: { name: string; title: string };
  results: Record<string, ResultIdentity>;
};

export type ResponseRecord = { question_id: string; act: string; option_id: string; evidence: Evidence; consequence_tags: string[] };
export type GameResult = {
  realm: { name: string; title: string };
  primary_animal: string;
  identity: ResultIdentity;
  callbacks: string[];
  questions_answered: number;
  adaptive_questions_answered: number;
  internal: { vector: Record<string, number>; ranking: string[]; distances: Record<string, number>; responses: ResponseRecord[] };
};
export type Evaluation = {
  answers: string[];
  current: GameQuestion | null;
  phase: string;
  core_answered: number;
  judgment_total: number;
  judgment_answered: number;
  tags: Record<string, number>;
  callbacks: string[];
  result: GameResult | null;
};

export const gameBundle = rawBundle as unknown as GameBundle;

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

function distance(left: number[], right: number[]) {
  return Math.sqrt(left.reduce((sum, value, index) => sum + (value - right[index]) ** 2, 0) / left.length);
}

function estimateVector(responses: ResponseRecord[], bundle: GameBundle) {
  const sums: Record<string, number> = {};
  const counts: Record<string, number> = {};
  bundle.dimensions.forEach(({ id }) => { sums[id] = 0; counts[id] = 0; });
  responses.forEach((response) => Object.entries(response.evidence).forEach(([trait, value]) => {
    sums[trait] += value; counts[trait] += 1;
  }));
  return bundle.dimensions.map(({ id }) => counts[id] ? sums[id] / counts[id] : 0);
}

function rankAnimals(vector: number[], bundle: GameBundle) {
  return Object.keys(bundle.animals).sort((left, right) =>
    distance(vector, bundle.animals[left].vector) - distance(vector, bundle.animals[right].vector),
  );
}

function optionFor(question: GameQuestion, optionId: string) {
  return question.options.find((option) => option.id === optionId.toUpperCase()) ?? question.options[0];
}

function responseFor(question: GameQuestion, optionId: string): ResponseRecord {
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

function judgmentFor(responses: ResponseRecord[], bundle: GameBundle) {
  const ranking = rankAnimals(estimateVector(responses, bundle), bundle);
  const pair = new Set(ranking.slice(0, 2));
  return bundle.adaptive_questions.filter((question) =>
    question.discriminates?.length === 2 && question.discriminates.every((animal) => pair.has(animal)),
  ).map((question) => ({ ...question, setup: bundle.judgment.intro, location: "Hall of Judgment" }));
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

  const judgmentQuestions = judgmentFor(responses, bundle);
  const extraAnswers = answerIds.slice(coreCount, coreCount + judgmentQuestions.length);
  judgmentQuestions.forEach((question, index) => {
    if (index >= extraAnswers.length) return;
    const option = optionFor(question, extraAnswers[index]);
    acceptedAnswers.push(option.id);
    responses.push(responseFor(question, option.id));
  });

  if (extraAnswers.length < judgmentQuestions.length) {
    return { answers: acceptedAnswers, current: judgmentQuestions[extraAnswers.length], phase: "Judgment", core_answered: coreCount, judgment_total: judgmentQuestions.length, judgment_answered: extraAnswers.length, tags, callbacks: callbacksFrom(tags), result: null };
  }

  const vector = estimateVector(responses, bundle);
  const ranking = rankAnimals(vector, bundle);
  const primary = ranking[0];
  const distances = Object.fromEntries(ranking.map((animal) => [animal, distance(vector, bundle.animals[animal].vector)]));
  const result: GameResult = {
    realm: bundle.realm,
    primary_animal: primary,
    identity: bundle.results[primary],
    callbacks: callbacksFrom(tags),
    questions_answered: responses.length,
    adaptive_questions_answered: responses.length - coreCount,
    internal: {
      vector: Object.fromEntries(bundle.dimensions.map(({ id }, index) => [id, vector[index]])),
      ranking, distances, responses,
    },
  };
  return { answers: acceptedAnswers, current: null, phase: "Result", core_answered: coreCount, judgment_total: judgmentQuestions.length, judgment_answered: judgmentQuestions.length, tags, callbacks: result.callbacks, result };
}

export function bestAnswerForAnimal(question: GameQuestion, animal: string, bundle: GameBundle = gameBundle) {
  const vector = bundle.animals[animal].vector;
  const index = Object.fromEntries(bundle.dimensions.map(({ id }, position) => [id, position]));
  return question.options.reduce((best, option) => {
    const score = Object.entries(option.evidence).reduce((sum, [trait, value]) => sum + (vector[index[trait]] - value) ** 2, 0);
    const bestScore = Object.entries(best.evidence).reduce((sum, [trait, value]) => sum + (vector[index[trait]] - value) ** 2, 0);
    return score < bestScore ? option : best;
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
