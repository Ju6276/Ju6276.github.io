# Audit Report — Ju Dong Academic Homepage

Target: `index.html` · Measured in-browser at 375 / 640 / 1024 / 1440px, both themes.

## Audit Health Score

| # | Dimension | Score | Key Finding |
|---|-----------|-------|-------------|
| 1 | Accessibility | 4 | WCAG AA met in both themes; worst measured ratio 4.94:1 (light), 6.14:1 (dark) |
| 2 | Performance | 4 | CLS 0, 296KB total assets, DOMContentLoaded 11ms, no failed requests |
| 3 | Responsive Design | 4 | No horizontal scroll at 375px; touch targets ≥44px on coarse pointers |
| 4 | Theming | 4 | Fully tokenized, dual theme, no flash on load, no hardcoded colors below `:root` |
| 5 | Anti-Patterns | 3 | Clean, but the mono-label + grid combination sits near a known developer-aesthetic trope |
| **Total** | | **19/20** | **Excellent (minor polish)** |

## Anti-Patterns Verdict

**Pass.** Would someone say "an AI made this"? Unlikely, but not impossible — and the reason is worth naming.

Absent: gradient hero, CTA buttons, testimonial cards, identical card grids, glassmorphism, neon-on-dark, gradient text, hero-metric template, emoji icons, rounded rectangles with generic drop shadows, purple-to-blue gradients, Inter/Roboto.

Present and deliberate: a blueprint grid substrate, hairline rules in place of elevation, sharp corners, monospace metadata, a right-rail scroll indicator adapted from the user's own reference.

The one honest reservation: `frontend-design` explicitly warns against "monospace typography as lazy shorthand for technical/developer vibes." This page uses JetBrains Mono for dates, venue tags, section labels, and the footer. The usage is defensible — those are all data or metadata, tabular figures genuinely help the date column align, and body copy stays in IBM Plex Sans — but the combined signal of *mono labels plus a technical grid* is a recognizable idiom. It reads as intentional here rather than borrowed, which is why this scores 3 and not lower. Dropping to 2 would require the mono to leak into body text or the grid to become decorative.

## Executive Summary

- Audit Health Score: **19/20** (Excellent)
- Issues found: 0 P0, 0 P1, 2 P2, 2 P3 — all P2/P3 were fixed during the polish pass before this report
- No blocking or release-blocking defects remain

## Detailed Findings

### Fixed during polish

**[P2] Publication link targets below 44px on touch devices**
Location: `.pub-links a`, `min-height: 34px`
Category: Responsive / Touch
Impact: arXiv and Project Page links — the primary click destinations for a reviewer on a phone — were 34px tall, under the Apple HIG and Material minimum.
Standard: Apple HIG 44×44pt, Material 48×48dp
Fix applied: `@media (pointer: coarse) { .pub-links a { min-height: 44px } }`. Pointer devices keep the tighter row so the layout stays compact where precision is available.

**[P2] Light-theme secondary text at minimum contrast**
Location: `--color-muted-foreground: #64748B`
Category: Accessibility
Impact: Measured 4.55:1 against `#F8FAFC` — passing AA, but with almost no margin. Subpixel antialiasing and non-sRGB displays could push perceived contrast below the line for summaries, dates, and venue text.
Standard: WCAG 2.1 AA (1.4.3)
Fix applied: darkened to `#5A6980`, raising the page's worst-case light ratio from 4.55:1 to 4.94:1.

**[P3] Blueprint grid vanished below the first screen**
Location: `body::before` mask
Category: Anti-Pattern / design-intent drift
Impact: The radial mask faded to fully transparent, so everything past the masthead lost the defining aesthetic element and reverted to a generic clean layout — a direct contradiction of the design doc's Principle 3.
Fix applied: mask floor raised to `rgba(0,0,0,0.55)` and the ellipse widened to `150% 105%`, keeping the grid present the full height of the page.

**[P3] `transition: all` on the nav rail indicator**
Location: `.rail a::after`
Category: Performance
Impact: `all` transitions every animatable property including unintended ones, and defeats compositor optimization.
Fix applied: enumerated to `width`, `height`, `border-color`, `background-color`.

Also corrected in the same pass: duplicate `display` declaration on `.rail a`; `aria-current="true"` changed to the semantically correct `aria-current="location"` for same-page anchors; `:active` states added to all three interactive families; easing standardized to `cubic-bezier(0.25, 1, 0.5, 1)` (ease-out-quart) per the motion guidance; inline SVG favicon added to eliminate a 404.

### Verified clean

- **Heading hierarchy**: `1,2,2,2,3,3,3,2,2,2,2` — no skipped levels
- **Images**: all three have descriptive alt text (19 / 163 / 207 characters), explicit `width`/`height`, and `loading="lazy"` on the two below the fold
- **CLS**: 0
- **Failed resources**: none
- **Horizontal overflow at 375px**: none (`scrollWidth === clientWidth === 375`)
- **Keyboard**: skip link present; every interactive element reachable with a visible 2px accent focus ring; the rail is `display: none` below 1100px so it leaves the tab order rather than becoming an invisible trap
- **Reduced motion**: honored, all durations collapse to 0.01ms
- **Theme flash**: none — theme is applied by an inline script before first paint
- **Console**: no errors or warnings

## Patterns & Systemic Observations

No systemic issues. Colors are tokenized without exception, spacing draws from a single 4/8px scale (`--space-1` through `--space-18`), and one timeline component serves News, Patents, Education, Experience, and Talks rather than five bespoke layouts.

## Positive Findings

- **Evidence hierarchy works.** Author lists bold "Ju Dong" so a reader finds the name instantly; venue tags are legible at a glance; teaser figures carry the results without the reader having to click through.
- **Contrast has margin in dark mode** (6.14:1 worst case), not just bare compliance.
- **Single file, no build step.** Deployable to GitHub Pages by copying one HTML file and an assets folder; nothing to break in CI.
- **Assets are lean**: 3.1MB of source PNGs reduced to 296KB of WebP without visible quality loss at display size.

## Recommended Actions

None blocking. Two optional follow-ups if the page grows:

1. **[P3] `/critique`** — worth running if more sections are added, to re-check whether the single-column density still holds up at double the current length.
2. **[P3] `/typeset`** — if a publication list grows past ~8 entries, the author-line treatment may need a truncation or expansion strategy.
