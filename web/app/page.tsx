"use client";

import { useEffect, useMemo, useState } from "react";
import { evaluateAnswers, gameBundle, type Evaluation } from "./game-engine";

type Stage = "threshold" | "journey" | "interlude" | "realm" | "animal" | "result";

const storageKey = "wildcourt.three-realm.answers.v1";
const roman = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI"];
const palette = [
  { name: "Pine Night", code: "#08110E", role: "Ceremony" }, { name: "Deep Fir", code: "#10221B", role: "Surface" },
  { name: "Frosted Bone", code: "#E7E3D7", role: "Reading" }, { name: "Snow Mist", code: "#F5F3EC", role: "Highlight" },
  { name: "Lichen Silver", code: "#A8B5A7", role: "Guidance" }, { name: "Ember Copper", code: "#C78E62", role: "Identity" },
  { name: "Covenant Red", code: "#743B3D", role: "Consequence" },
];
const realmImages: Record<string, string> = {
  Taiga: "/biomes/taiga/realm-v1.jpg",
  Desert: "/biomes/desert/realm-v1.jpg",
  Rainforest: "/biomes/rainforest/realm-v5.jpg",
};
const animalImages: Record<string, string> = {
  "Grey Wolf": "/animals/taiga/grey-wolf-v1.jpg",
  Reindeer: "/animals/taiga/reindeer-v1.jpg",
  Lynx: "/animals/taiga/lynx-v1.jpg",
  Bear: "/animals/taiga/bear-v1.jpg",
  Moose: "/animals/taiga/moose-v1.jpg",
  Wolverine: "/animals/taiga/wolverine-v1.jpg",
  "Fennec Fox": "/animals/desert/fennec-fox-v1.jpg",
  Caracal: "/animals/desert/caracal-v1.jpg",
  Cobra: "/animals/desert/cobra-v1.jpg",
  Camel: "/animals/desert/camel-v1.jpg",
  Scorpion: "/animals/desert/scorpion-v1.jpg",
  Oryx: "/animals/desert/oryx-v1.jpg",
  Jaguar: "/animals/rainforest/jaguar-v2.jpg",
  "Scarlet Macaw": "/animals/rainforest/scarlet-macaw-v2.jpg",
  "Orchid Mantis": "/animals/rainforest/orchid-mantis-v2.jpg",
  Okapi: "/animals/rainforest/okapi-v2.jpg",
  "Golden Lion Tamarin": "/animals/rainforest/golden-lion-tamarin-v2.jpg",
  "Blue Morpho": "/animals/rainforest/blue-morpho-v2.jpg",
};
const courtSigils: Record<string, string> = {
  Bonds: "/sigils/bonds.svg",
  Fracture: "/sigils/fracture.svg",
  Judgment: "/sigils/judgment.svg",
  Taiga: "/sigils/taiga.svg",
  Desert: "/sigils/desert.svg",
  Rainforest: "/sigils/rainforest.svg",
};

export default function Home() {
  const [stage, setStage] = useState<Stage>("threshold");
  const [answers, setAnswers] = useState<string[]>([]);
  const [savedAnswers, setSavedAnswers] = useState<string[]>([]);
  const [selected, setSelected] = useState<string | null>(null);
  const [interludePhase, setInterludePhase] = useState("Bonds");
  const [paletteOpen, setPaletteOpen] = useState(false);
  const evaluation = useMemo(() => evaluateAnswers(answers), [answers]);

  useEffect(() => {
    try {
      const stored = JSON.parse(localStorage.getItem(storageKey) ?? "[]");
      if (Array.isArray(stored) && stored.every((answer) => typeof answer === "string")) setSavedAnswers(stored);
    } catch { localStorage.removeItem(storageKey); }
  }, []);

  useEffect(() => {
    window.scrollTo({ top: 0, behavior: "auto" });
  }, [stage]);

  function persist(nextAnswers: string[]) {
    setAnswers(nextAnswers); setSavedAnswers(nextAnswers);
    localStorage.setItem(storageKey, JSON.stringify(nextAnswers));
  }

  function startFresh() { persist([]); setSelected(null); setStage("journey"); }
  function resume() {
    const restored = evaluateAnswers(savedAnswers);
    setAnswers(restored.answers); setSelected(null);
    setStage(restored.result ? "realm" : "journey");
  }
  function restart() {
    if (answers.length && !window.confirm("เริ่มการเดินทางใหม่และลบคำตอบที่บันทึกไว้?")) return;
    localStorage.removeItem(storageKey); setAnswers([]); setSavedAnswers([]); setSelected(null); setStage("threshold");
  }
  function goBack() {
    if (!answers.length) { setStage("threshold"); return; }
    persist(answers.slice(0, -1)); setSelected(null); setStage("journey");
  }
  function submitChoice() {
    if (!selected || !evaluation.current) return;
    const oldPhase = evaluation.phase;
    const nextAnswers = [...answers, selected];
    const next = evaluateAnswers(nextAnswers);
    persist(nextAnswers); setSelected(null);
    if (next.result) {
      if (oldPhase === "Fracture") { setInterludePhase("Judgment"); setStage("interlude"); }
      else setStage("realm");
      return;
    }
    if (next.phase !== oldPhase) { setInterludePhase(next.phase); setStage("interlude"); return; }
    setStage("journey");
  }

  const current = evaluation.current;
  const result = evaluation.result;
  const totalQuestions = 16 + evaluation.judgment_total;
  const progress = Math.min(100, (answers.length / Math.max(16, totalQuestions)) * 100);
  const interlude = interludePhase === "Judgment"
    ? { title: "Judgment — Name the way you protect", intro: gameBundle.judgment.intro, outro: gameBundle.judgment.transition_to_result }
    : gameBundle.acts[interludePhase];
  const interludeNote = interludePhase === "Judgment" ? gameBundle.judgment.transition_to_result : null;

  return (
    <main className={`wildcourt-app wildcourt-stage-${stage}`}>
      <header className="wildcourt-header">
        <button className="wildcourt-wordmark" type="button" onClick={() => setStage("threshold")} aria-label="Return to opening"><span className="wildcourt-wordmark-mark">W</span><span>The Wild Court</span></button>
        <div className="wildcourt-header-meta"><span>{answers.length ? `${answers.length} choices remembered` : "Taiga · Desert · Rainforest prototype"}</span><button className="wildcourt-palette-toggle" type="button" onClick={() => setPaletteOpen(true)}>Palette</button>{answers.length > 0 && <button className="wildcourt-palette-toggle" type="button" onClick={restart}>Restart</button>}</div>
      </header>

      {stage === "threshold" && <Threshold savedCount={savedAnswers.length} onBegin={startFresh} onResume={resume} />}

      {stage === "journey" && current && (
        <section className="wildcourt-journey" aria-live="polite">
          <div className="wildcourt-progress-block"><div className="wildcourt-progress-copy"><span>{current.act}</span><span>{answers.length + 1} / {Math.max(16, totalQuestions)}</span></div><div className="wildcourt-progress-track"><span style={{ width: `${progress}%` }} /></div></div>
          <div className="wildcourt-scene-grid">
            <aside className="wildcourt-scene-aside"><span className="wildcourt-roman">{current.act === "Judgment" ? "J" : roman[(current.scene_order ?? 1) - 1]}</span><p>{current.location ?? "Hall of Judgment"}</p><div className="wildcourt-wind-mark" aria-hidden="true"><i /><i /><i /></div></aside>
            <article className="wildcourt-question-panel">
              <p className="wildcourt-eyebrow">The First Winter · {current.act}</p><h2>{current.title}</h2>{current.setup && <p className="wildcourt-setup">{current.setup}</p>}<p className="wildcourt-question">{current.scenario}</p>
              <div className="wildcourt-choices" role="radiogroup" aria-label={current.scenario}>
                {current.options.map((choice) => <button className="wildcourt-choice" data-selected={selected === choice.id} key={choice.id} type="button" role="radio" aria-checked={selected === choice.id} onClick={() => setSelected(choice.id)}><span>{choice.id}</span><span>{choice.copy}</span><span aria-hidden="true">{selected === choice.id ? "◆" : "◇"}</span></button>)}
              </div>
              <div className="wildcourt-question-footer"><button className="wildcourt-back" type="button" onClick={goBack}>← Back</button><p>{selected ? "Your choice will be remembered." : "Choose your real response, not the most admirable one."}</p><button className="wildcourt-continue" type="button" disabled={!selected} onClick={submitChoice}>Confirm <span aria-hidden="true">→</span></button></div>
            </article>
          </div>
        </section>
      )}

      {stage === "interlude" && (
        <section className="wildcourt-interlude"><div className="wildcourt-sigil" aria-hidden="true"><img src={courtSigils[interludePhase]} alt="" /></div><p className="wildcourt-eyebrow">{answers.length} choices remembered</p><h2>{interlude.title}</h2><p className="wildcourt-interlude-lead">{interlude.intro}</p><div className="wildcourt-memory-list">{evaluation.callbacks.map((memory, index) => <p key={memory}><span>0{index + 1}</span>{memory}</p>)}</div>{interludeNote && <p className="wildcourt-prototype-note">{interludeNote}</p>}<button className="wildcourt-primary-action" type="button" onClick={() => setStage(interludePhase === "Judgment" && evaluation.result ? "realm" : "journey")}>{interludePhase === "Judgment" && evaluation.result ? "Receive the answer" : `Enter ${interludePhase}`} <span aria-hidden="true">→</span></button></section>
      )}

      {stage === "realm" && result && (
        <section className="wildcourt-reveal wildcourt-realm-reveal" data-realm={result.realm.name.toLowerCase()}>
          <div className="wildcourt-realm-backdrop" aria-hidden="true"><img src={realmImages[result.realm.name]} alt="" /></div>
          <div className="wildcourt-reveal-content"><p className="wildcourt-eyebrow">Your native realm</p><RealmGlyph realm={result.realm.name} /><h2>{result.realm.name}</h2><h3>{result.realm.title}</h3><div className="wildcourt-threshold-rule"><span>THE COURT HAS ANSWERED</span></div><p className="wildcourt-reveal-copy">{result.realm.belief}</p><button className="wildcourt-primary-action" type="button" onClick={() => setStage("animal")}>Meet your nature <span aria-hidden="true">→</span></button></div>
        </section>
      )}

      {stage === "animal" && result && (
        <section className="wildcourt-reveal wildcourt-animal-reveal" data-realm={result.realm.name.toLowerCase()}>
          <div className="wildcourt-animal-reveal-grid"><figure className="wildcourt-animal-portrait"><img src={animalImages[result.primary_animal]} alt={`Illustrated portrait of the ${result.primary_animal}`} /></figure><div className="wildcourt-animal-reveal-copy"><p className="wildcourt-eyebrow">{result.realm.name} · Your true nature</p><h2>{result.primary_animal}</h2><h3>{result.identity.title}</h3><p className="wildcourt-reveal-copy">{result.identity.identity_promise}</p><div className="wildcourt-result-signatures">{result.identity.signatures.map((signature) => <span key={signature}>{signature}</span>)}</div><button className="wildcourt-primary-action" type="button" onClick={() => setStage("result")}>Read your result <span aria-hidden="true">↓</span></button></div></div>
        </section>
      )}

      {stage === "result" && result && <ResultPage result={result} onRestart={restart} />}
      <footer className="wildcourt-footer"><span>THE WILD COURT</span><span>Three realms are listening.</span></footer>
      {paletteOpen && <PaletteDrawer onClose={() => setPaletteOpen(false)} />}
    </main>
  );
}

function Threshold({ savedCount, onBegin, onResume }: { savedCount: number; onBegin: () => void; onResume: () => void }) {
  return <section className="wildcourt-threshold"><div className="wildcourt-forest" aria-hidden="true"><span className="wildcourt-tree wildcourt-tree-one"/><span className="wildcourt-tree wildcourt-tree-two"/><span className="wildcourt-tree wildcourt-tree-three"/><span className="wildcourt-tree wildcourt-tree-four"/></div><div className="wildcourt-threshold-copy"><p className="wildcourt-eyebrow">An identity adventure</p><h1>Winter remembers<br/>how you arrived.</h1><p className="wildcourt-threshold-thai">ฤดูหนาวมาเร็วกว่าที่ควร และในกระเป๋าเสื้อของคุณมีข้อความซึ่งอาจเปลี่ยนชะตาของ Hearthhold</p><div className="wildcourt-threshold-rule"><span>THE FIRST WINTER</span></div><div className="wildcourt-threshold-actions"><button className="wildcourt-primary-action" type="button" onClick={onBegin}>{savedCount ? "Begin again" : "Cross the threshold"} <span aria-hidden="true">→</span></button>{savedCount > 0 && <button className="wildcourt-secondary-action" type="button" onClick={onResume}>Continue {savedCount} remembered choices</button>}</div><p className="wildcourt-duration">16–18 choices · progress saved on this device</p></div><aside className="wildcourt-unmarked-note"><span>Guest record</span><strong>The Unmarked Wayfarer</strong><p>No house. No inherited allegiance. Only the pattern of your choices.</p></aside></section>;
}

function RealmGlyph({ realm }: { realm: string }) {
  return <div className="wildcourt-realm-glyph" aria-hidden="true"><img src={courtSigils[realm]} alt="" /></div>;
}

function ResultPage({ result, onRestart }: { result: NonNullable<Evaluation["result"]>; onRestart: () => void }) {
  const patternCards = [
    ["What moves you", result.identity.patterns.what_moves_you],
    ["How you connect", result.identity.patterns.how_you_connect],
    ["How you protect", result.identity.patterns.how_you_protect],
    ["When winter closes in", result.identity.patterns.when_winter_closes_in],
    ["What you rarely ask for", result.identity.patterns.what_you_rarely_ask_for],
  ];

  return <section className="wildcourt-deep-result" data-realm={result.realm.name.toLowerCase()}>
    <header className="wildcourt-result-masthead">
      <div className="wildcourt-result-landscape" aria-hidden="true"><img src={realmImages[result.realm.name]} alt="" /></div>
      <div className="wildcourt-result-hero">
        <figure className="wildcourt-result-animal"><img src={animalImages[result.primary_animal]} alt={`Illustrated portrait of the ${result.primary_animal}`} /></figure>
        <div className="wildcourt-result-identity"><p className="wildcourt-eyebrow">{result.realm.name} · The Court remembers</p><h1>{result.primary_animal}</h1><h2>{result.identity.title}</h2><p>{result.identity.identity_promise}</p><div className="wildcourt-result-signatures">{result.identity.signatures.map((signature) => <span key={signature}>{signature}</span>)}</div></div>
      </div>
    </header>
    <div className="wildcourt-result-reading">
      <section><span className="wildcourt-result-index">01 · Recognition</span><h3>At your core</h3><p>{result.identity.short_result}</p></section>
      <section className="wildcourt-pattern-section"><span className="wildcourt-result-index">02 · Your pattern</span><h3>The way your nature moves</h3><div className="wildcourt-pattern-grid">{patternCards.map(([title, copy], index) => <article className="wildcourt-pattern-card" data-shadow={index === 3} key={title}><span>0{index + 1}</span><h4>{title}</h4><p>{copy}</p></article>)}</div></section>
      <section><span className="wildcourt-result-index">03 · Your journey</span><h3>What the Court remembers</h3><div className="wildcourt-result-memories">{result.callbacks.map((callback, index) => <p key={callback}><span>0{index + 1}</span>{callback}</p>)}</div></section>
      <section className="wildcourt-misunderstanding"><span className="wildcourt-result-index">04 · Seen from outside</span><h3>The misunderstanding</h3><blockquote>“{result.identity.misunderstanding}”</blockquote><div className="wildcourt-balance-note"><span>Restoring balance</span><p>{result.identity.restoring_balance}</p></div></section>
      <section><span className="wildcourt-result-index">05 · Belonging</span><h3>Why {result.realm.name} knows you</h3><p>{result.identity.realm_connection}</p></section>
      <blockquote className="wildcourt-result-closing">“{result.identity.closing}”</blockquote>
      <div className="wildcourt-result-actions"><button className="wildcourt-primary-action" type="button" onClick={() => navigator.clipboard?.writeText(`${result.primary_animal} — ${result.identity.title}\n${result.identity.identity_promise}`)}>Copy share text <span aria-hidden="true">＋</span></button><button className="wildcourt-secondary-action wildcourt-secondary-dark" type="button" onClick={onRestart}>Begin again</button></div>
      <p className="wildcourt-result-footnote">Answered {result.questions_answered} questions · {result.adaptive_questions_answered} Judgment questions · exact scores remain private</p>
    </div>
  </section>;
}

function PaletteDrawer({ onClose }: { onClose: () => void }) {
  return <div className="wildcourt-palette-backdrop" role="presentation" onClick={onClose}><aside className="wildcourt-palette-sheet" role="dialog" aria-modal="true" aria-labelledby="palette-title" onClick={(event) => event.stopPropagation()}><button className="wildcourt-palette-close" type="button" onClick={onClose} aria-label="Close palette">×</button><p className="wildcourt-eyebrow">Theme foundation v0.1</p><h2 id="palette-title">Boreal Ceremonial</h2><p className="wildcourt-palette-intro">Dark ceremony, warm reading, restrained prestige. Copper marks identity; red is reserved for consequence.</p><div className="wildcourt-swatches">{palette.map((color) => <div className="wildcourt-swatch" key={color.code}><span style={{background:color.code}}/><div><strong>{color.name}</strong><small>{color.code} · {color.role}</small></div></div>)}</div><div className="wildcourt-theme-principles"><p><span>01</span> Spectacle is dark; reflection is light.</p><p><span>02</span> No gold unless the lore earns it.</p><p><span>03</span> One accent carries one meaning.</p></div></aside></div>;
}
