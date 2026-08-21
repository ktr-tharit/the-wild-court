"use client";

import { useState } from "react";

const animals = [
  { name: "Fennec Fox", title: "The Listener in the Dunes", promise: "Sensitivity is not fragility; it lets you hear the path that force would bury.", image: "/animals/desert/fennec-fox-v1.jpg" },
  { name: "Caracal", title: "The Silent Standard", promise: "Your dignity does not begin when the room recognizes it.", image: "/animals/desert/caracal-v1.jpg" },
  { name: "Cobra", title: "The Keeper of the Final Line", promise: "A boundary spoken clearly is an act of mercy before consequence becomes necessary.", image: "/animals/desert/cobra-v1.jpg" },
  { name: "Camel", title: "The Bearer of the Long Measure", promise: "You know the weight of a promise before you lift it—and that is why yours arrives.", image: "/animals/desert/camel-v1.jpg" },
  { name: "Scorpion", title: "The Unbowed Sovereign", promise: "Your right to a boundary is not measured by your size, status or usefulness.", image: "/animals/desert/scorpion-v1.jpg" },
  { name: "Oryx", title: "The Keeper of the Inner Spring", promise: "Enoughness can be radiant; survival does not require you to become barren inside.", image: "/animals/desert/oryx-v1.jpg" },
] as const;

export default function DesertAnimalVisualReview() {
  const [selectedIndex, setSelectedIndex] = useState(0);
  const selected = animals[selectedIndex];

  return (
    <main className="wildcourt-app wildcourt-animal-review">
      <header className="wildcourt-header">
        <div className="wildcourt-wordmark"><span className="wildcourt-wordmark-mark">W</span><span>The Wild Court</span></div>
        <div className="wildcourt-header-meta"><span>Visual review · Desert animals v1</span></div>
      </header>
      <nav className="wildcourt-review-selector" aria-label="Choose an animal portrait to review">
        {animals.map((animal, index) => (
          <button key={animal.name} type="button" data-selected={index === selectedIndex} onClick={() => setSelectedIndex(index)}>{animal.name}</button>
        ))}
      </nav>
      <section className="wildcourt-reveal wildcourt-animal-reveal" data-realm="desert">
        <div className="wildcourt-animal-reveal-grid">
          <figure className="wildcourt-animal-portrait"><img src={selected.image} alt={`Illustrated portrait of the ${selected.name}`} /></figure>
          <div className="wildcourt-animal-reveal-copy">
            <p className="wildcourt-eyebrow">Desert · Your true nature</p>
            <h2>{selected.name}</h2>
            <h3>{selected.title}</h3>
            <p className="wildcourt-reveal-copy">{selected.promise}</p>
            <div className="wildcourt-review-spec"><span>Master 1122×1402</span><span>Web 1120×1400</span><span>4:5 canonical</span></div>
            <span className="wildcourt-primary-action">Read your result <span aria-hidden="true">↓</span></span>
          </div>
        </div>
      </section>
      <footer className="wildcourt-footer"><span>THE SUNLESS CROWN</span><span>Animal portrait crop review</span></footer>
    </main>
  );
}
