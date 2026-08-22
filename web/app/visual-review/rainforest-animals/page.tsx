"use client";

import { useState } from "react";

const animals = [
  { name: "Jaguar", title: "The Sovereign Under Leaves", promise: "Connection does not require surrendering the right to say no.", image: "/animals/rainforest/jaguar-v2.jpg" },
  { name: "Scarlet Macaw", title: "The Voice of the Living Canopy", promise: "Your visibility is not vanity when it helps truth reach the lives that need it.", image: "/animals/rainforest/scarlet-macaw-v2.jpg" },
  { name: "Orchid Mantis", title: "The Beautiful Ambush", promise: "What you reveal is chosen; beauty can be intelligence rather than permission.", image: "/animals/rainforest/orchid-mantis-v2.jpg" },
  { name: "Okapi", title: "The Unwritten Heir", promise: "You can belong without becoming completely legible.", image: "/animals/rainforest/okapi-v2.jpg" },
  { name: "Golden Lion Tamarin", title: "The Golden Thread", promise: "Care is not softness at the edge of life; it is the thread that lets life continue together.", image: "/animals/rainforest/golden-lion-tamarin-v2.jpg" },
  { name: "Blue Morpho", title: "The Light Between Leaves", promise: "Change does not make your connections unreal, and connection does not give anyone ownership of what you become.", image: "/animals/rainforest/blue-morpho-v2.jpg" },
] as const;

export default function RainforestAnimalVisualReview() {
  const [selectedIndex, setSelectedIndex] = useState(0);
  const selected = animals[selectedIndex];

  return (
    <main className="wildcourt-app wildcourt-animal-review">
      <header className="wildcourt-header">
        <div className="wildcourt-wordmark"><span className="wildcourt-wordmark-mark">W</span><span>The Wild Court</span></div>
        <div className="wildcourt-header-meta"><span>Visual review · Rainforest animals v2</span></div>
      </header>
      <nav className="wildcourt-review-selector" aria-label="Choose an animal portrait to review">
        {animals.map((animal, index) => (
          <button key={animal.name} type="button" data-selected={index === selectedIndex} onClick={() => setSelectedIndex(index)}>{animal.name}</button>
        ))}
      </nav>
      <section className="wildcourt-reveal wildcourt-animal-reveal" data-realm="rainforest">
        <div className="wildcourt-animal-reveal-grid">
          <figure className="wildcourt-animal-portrait"><img src={selected.image} alt={`Illustrated portrait of the ${selected.name}`} /></figure>
          <div className="wildcourt-animal-reveal-copy">
            <p className="wildcourt-eyebrow">Rainforest · Your true nature</p>
            <h2>{selected.name}</h2>
            <h3>{selected.title}</h3>
            <p className="wildcourt-reveal-copy">{selected.promise}</p>
            <div className="wildcourt-review-spec"><span>Master 1122×1402</span><span>Web 1120×1400</span><span>4:5 canonical</span></div>
            <span className="wildcourt-primary-action">Read your result <span aria-hidden="true">↓</span></span>
          </div>
        </div>
      </section>
      <footer className="wildcourt-footer"><span>THE VERDANT EMPIRE</span><span>Animal portrait crop review</span></footer>
    </main>
  );
}
