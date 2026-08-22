"use client";

import { useState } from "react";

const animals = [
  { name: "Lion", title: "The Crown in Full View", promise: "Authority becomes honorable only when it accepts the gaze and consequence of those it moves.", image: "/animals/savanna/lion-v1.jpg" },
  { name: "Elephant", title: "The Keeper of the Living Legacy", promise: "What a people remembers should protect the lives still becoming, not only the names already carved in stone.", image: "/animals/savanna/elephant-v1.jpg" },
  { name: "Secretary Bird", title: "The Step That Ends the Argument", promise: "When the moment becomes clear, you act where everyone can see the consequence.", image: "/animals/savanna/secretary-bird-v1.jpg" },
  { name: "Hyena", title: "The Laugh Beneath the Throne", promise: "Your laughter reminds the room that no one is too important to be questioned.", image: "/animals/savanna/hyena-v1.jpg" },
  { name: "Greater Kudu", title: "The Crown That Never Asked", promise: "You do not need to claim the center for your presence to carry its own authority.", image: "/animals/savanna/greater-kudu-v1.jpg" },
  { name: "Giraffe", title: "The Witness of the Far Horizon", promise: "Seeing farther matters when you bring the horizon back without looking down on those beside you.", image: "/animals/savanna/giraffe-v1.jpg" },
] as const;

export default function SavannaAnimalVisualReview() {
  const [selectedIndex, setSelectedIndex] = useState(0);
  const selected = animals[selectedIndex];

  return (
    <main className="wildcourt-app wildcourt-animal-review">
      <header className="wildcourt-header">
        <div className="wildcourt-wordmark"><span className="wildcourt-wordmark-mark">W</span><span>The Wild Court</span></div>
        <div className="wildcourt-header-meta"><span>Visual review · Savanna animals v1</span></div>
      </header>
      <nav className="wildcourt-review-selector" aria-label="Choose an animal portrait to review">
        {animals.map((animal, index) => (
          <button key={animal.name} type="button" data-selected={index === selectedIndex} onClick={() => setSelectedIndex(index)}>{animal.name}</button>
        ))}
      </nav>
      <section className="wildcourt-reveal wildcourt-animal-reveal" data-realm="savanna">
        <div className="wildcourt-animal-reveal-grid">
          <figure className="wildcourt-animal-portrait"><img src={selected.image} alt={`Illustrated portrait of the ${selected.name}`} /></figure>
          <div className="wildcourt-animal-reveal-copy">
            <p className="wildcourt-eyebrow">Savanna · Your true nature</p>
            <h2>{selected.name}</h2>
            <h3>{selected.title}</h3>
            <p className="wildcourt-reveal-copy">{selected.promise}</p>
            <div className="wildcourt-review-spec"><span>Master 1122×1402</span><span>Web 1120×1400</span><span>4:5 canonical</span></div>
            <span className="wildcourt-primary-action">Read your result <span aria-hidden="true">↓</span></span>
          </div>
        </div>
      </section>
      <footer className="wildcourt-footer"><span>THE GOLDEN CROWN</span><span>Animal portrait crop review</span></footer>
    </main>
  );
}
