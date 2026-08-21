const desertRealmImage = "/biomes/desert/realm-v1.jpg";

export default function DesertRealmVisualReview() {
  return (
    <main className="wildcourt-app wildcourt-desert-review">
      <header className="wildcourt-header">
        <div className="wildcourt-wordmark"><span className="wildcourt-wordmark-mark">W</span><span>The Wild Court</span></div>
        <div className="wildcourt-header-meta"><span>Visual review · Desert realm v1</span></div>
      </header>
      <section className="wildcourt-reveal wildcourt-realm-reveal" data-realm="desert">
        <div className="wildcourt-realm-backdrop" aria-hidden="true"><img src={desertRealmImage} alt="" /></div>
        <div className="wildcourt-reveal-content">
          <p className="wildcourt-eyebrow">Your native realm</p>
          <div className="wildcourt-realm-glyph" aria-hidden="true"><img src="/sigils/desert.svg" alt="" /></div>
          <h2>Desert</h2>
          <h3>The Sunless Crown</h3>
          <div className="wildcourt-threshold-rule"><span>THE COURT HAS ANSWERED</span></div>
          <p className="wildcourt-reveal-copy">Here, restraint is not absence. It is how you keep freedom, meaning, and enough strength for what deserves the weight.</p>
          <span className="wildcourt-primary-action">Meet your nature <span aria-hidden="true">→</span></span>
        </div>
      </section>
      <footer className="wildcourt-footer"><span>THE SUNLESS CROWN</span><span>Want less. Waste nothing. Owe carefully.</span></footer>
    </main>
  );
}
