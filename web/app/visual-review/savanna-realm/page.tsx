const savannaRealmImage = "/biomes/savanna/realm-v1.jpg";

export default function SavannaRealmVisualReview() {
  return (
    <main className="wildcourt-app wildcourt-savanna-review">
      <header className="wildcourt-header">
        <div className="wildcourt-wordmark"><span className="wildcourt-wordmark-mark">W</span><span>The Wild Court</span></div>
        <div className="wildcourt-header-meta"><span>Visual review · Savanna realm v1</span></div>
      </header>
      <section className="wildcourt-reveal wildcourt-realm-reveal" data-realm="savanna">
        <div className="wildcourt-realm-backdrop" aria-hidden="true"><img src={savannaRealmImage} alt="" /></div>
        <div className="wildcourt-reveal-content">
          <p className="wildcourt-eyebrow">Your native realm</p>
          <div className="wildcourt-realm-glyph" aria-hidden="true"><img src="/sigils/savanna.svg" alt="" /></div>
          <h2>Savanna</h2>
          <h3>The Golden Crown</h3>
          <div className="wildcourt-threshold-rule"><span>THE COURT HAS ANSWERED</span></div>
          <p className="wildcourt-reveal-copy">Here, presence is not vanity. What shapes the many must stand where the many can see it—and answer.</p>
          <span className="wildcourt-primary-action">Meet your nature <span aria-hidden="true">→</span></span>
        </div>
      </section>
      <footer className="wildcourt-footer"><span>THE GOLDEN CROWN</span><span>I was not made to disappear.</span></footer>
    </main>
  );
}
