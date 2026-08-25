# Ju Dong — Academic Homepage Design Doc

Source content: `page-story.md`
Output target: `index.html` (single file, project root)

---

## Design Context

### Users

Three audiences, arriving with different questions and different amounts of patience.

**Robotics researchers and reviewers** land here after seeing a paper on arXiv, a talk at ICRA/IROS, or a citation. They want to answer one question fast: *what has this person actually built, and does it work on real hardware?* They scan for venue names, numbers, and the teaser figure. They will click through to arXiv or the project page within seconds if the page gives them a reason to.

**Prospective collaborators and lab members** — PhD students, postdocs, group leads — want the shape of the research agenda, not just a list. They read the About section, then check whether the publications cohere into a direction.

**Recruiters at robotics companies and research labs** scan affiliations, timeline, and whether the work has touched real robots rather than only simulation. Agile Robots experience and the real-hardware results matter to them specifically.

All three are reading on a laptop, often with many tabs open, often skimming. None of them will scroll a long page patiently. The job to be done is: *establish credibility and research identity within one screen, then make every artifact one click away.*

### Brand Personality

**Precise. Grounded. Unadorned.**

The voice of the page-story is a researcher who quantifies claims (70.0% success at 125 Hz, 43x speedup, 7–56% higher success rates) and states limitations plainly. The About section's core statement — that learned policies generalize but are too slow or brittle for closed-loop control, while classical controllers are stable but rigid — is an engineering thesis, not a marketing line. The design must match that register.

The emotional goal is **confidence through evidence**, not excitement. A reader should come away thinking "this person knows what they're doing on real hardware," which is earned by clear presentation of numbers and figures, not by visual flourish. Any decoration that reads as promotional would undercut the content.

### Aesthetic Direction

**Blueprint Scholar** — the visual language of engineering drawings: a cool blue palette, a barely-visible grid substrate, hairline rules instead of shadows, sharp corners, and small monospace labels for metadata. Precision made visible.

The rationale: the subject builds controllers and policies for physical robots. Technical drafting is the native visual idiom of that work, and it maps onto academic-page conventions without costume — a grid is structure, hairlines are measurement, monospace is data. It stays quiet while being distinctly *not* a generic clean/modern template.

Theme: **dual light and dark**, light as default. Light mode is the drafting-paper state (near-white, cool-tinted); dark mode is the backlit-screen state (deep navy). Both must carry the same grid and hairline logic.

Anti-references — what this must NOT look like:
- Startup landing page: gradient hero, oversized CTA buttons, testimonial cards, emoji
- Portfolio/designer site: full-bleed imagery, motion-heavy scroll effects, expressive type
- Corporate template: stock rounded cards floating on soft gray, drop shadows everywhere
- Bootstrap default: the "generic clean modern" look with no point of view

#### Reference

Analyzed from `w-r-s/academic-homepage-template` (`index.html` + `stylesheet.css`, 1940 lines), supplied by the user with the directional note *"style is fine, but change the color scheme to blue."*

Extracted signals:

| Signal | Reference value | Disposition |
|---|---|---|
| Color temperature | Warm — amber/gold links `#f49300`, accent `#fba524`, hover `#6e3519` | **Overridden by user** → cool blue |
| Typography | Lato, sans-serif throughout; 14px base — compact, information-dense | Adopt: sans-serif, compact base |
| Spatial density | Compact; `line-height: 1.8` on contact lines, tight sections | Adopt: dense over airy |
| Layout | Single centered column, `max-width: 800px`; fixed right-side scroll-progress dot nav (`.section-drip-nav`); breakpoint at 680px | Adopt: single column + right rail nav |
| Surface treatment | Soft multi-layer shadows (`0 2px 10px rgba(0,0,0,0.06)`, `0 6px 22px rgba(20,40,70,0.22)`); small radii 4–10px; avatar `50%` | **Tilt away** — Blueprint uses hairline borders instead of shadows, sharper corners |
| Animation | 21 `transition`/`@keyframes` rules — present but restrained | Adopt: restrained transitions, no scroll-triggered motion |
| Hover character | Color shift on links, no transform | Adopt |

Reference signals are soft inputs. They shape the skeleton (single column, compact type, right-rail nav) while the Blueprint aesthetic governs surface treatment (hairlines and grid replace shadows and rounded cards).

### Design Principles

1. **Evidence before ornament.** Every visual element must help a reader evaluate the work. Numbers, venue names, and teaser figures get typographic priority. Nothing decorative competes with them.

2. **Hairlines, not shadows.** Depth is expressed through 1px rules and grid alignment, the way a technical drawing separates regions. Elevation effects are forbidden — they signal "card UI," which is the wrong register.

3. **The grid is structure, not texture.** The blueprint grid sits at very low opacity as a substrate that content aligns to. If it ever reads as a decorative pattern rather than a measurement surface, it is too strong.

4. **Scannable in one screen, complete on scroll.** Name, role, affiliation, research statement, and contact must be visible without scrolling. Everything else rewards the reader who continues.

5. **Density with air between sections.** Tight within a block (following the reference's compact register), generous between blocks. Rhythm comes from section spacing, not from padding inside every element.

6. **Accessible by construction.** WCAG AA contrast minimum in both themes; visible `:focus-visible` rings; `prefers-reduced-motion` respected; the blue accent must never be the sole carrier of meaning, since deuteranopia and protanopia affect a meaningful share of this audience.

---

## Design System

Generated by `ui-ux-pro-max --design-system` with the query
`"academic researcher personal homepage robotics publications technical minimal blue"`,
then adapted where the skill's recommendations conflict with the Design Context above.
Each deviation is recorded with its reason; everything else is taken as-is.

### Pattern

**Minimal Single Column** — adopted as-is. Large typography, generous whitespace, no nav clutter, mobile-first. Matches both the reference skeleton (800px single column) and Principle 4 (scannable in one screen).

Deviation: the pattern's "Single CTA focus" and its prescribed section order (hero → description → 3 benefit bullets → CTA → footer) are landing-page conversion structures. An academic page has no conversion goal and its section order is fixed by `page-story.md`. **Reason for override:** the page-story is the authoritative source for content and ordering; adding a CTA button would violate Principle 1 (evidence before ornament) and read as promotional to a reviewer audience. The "single focus" intent is preserved differently — the About block is the one thing that must land before the fold.

### Style

**Exaggerated Minimalism** — adopted in spirit (high contrast, decisive negative space, full light *and* dark support, WCAG AA, excellent performance), with its scale prescriptions overridden.

Deviation: the skill's key effects specify `font-size: clamp(3rem, 10vw, 12rem)`, `font-weight: 900`, `letter-spacing: -0.05em`, and "massive whitespace." **Reason for override:** those values belong to fashion/agency/editorial pages where a single statement carries the screen. This page must present three publications with author lists, venue names, and quantitative results — display type at 12rem would push all evidence below the fold and directly contradict Principle 1 and the reference's compact 14px information-dense register. The high-contrast, negative-space *intent* is retained at academic scale: heading weight tops out at 600, the display size at `clamp(2rem, 4vw, 2.75rem)`, and whitespace is spent between sections rather than inside them (Principle 5).

### Colors

The skill's monochrome-plus-blue-accent palette is adopted, which independently matches the user's directional note ("change the color scheme to blue"). Neutrals are shifted from pure gray toward a cool tint to serve the blueprint aesthetic.

**Light theme**

| Role | Skill value | Used | Note |
|---|---|---|---|
| `--color-foreground` | `#09090B` | `#0B1220` | Cool-shifted near-black; blueprint ink, not neutral black |
| `--color-secondary` | `#3F3F46` | `#41505F` | Cool-shifted secondary text |
| `--color-accent` | `#2563EB` | `#2563EB` | As-is — the anchor of the whole palette |
| `--color-background` | `#FAFAFA` | `#F8FAFC` | Cool-shifted; drafting-paper white |
| `--color-muted` | `#E8ECF0` | `#E8ECF0` | As-is — already cool |
| `--color-border` | `#E4E4E7` | `#DBE3EC` | Cool-shifted hairline |
| `--color-ring` | `#18181B` | `#2563EB` | Focus ring uses accent so it reads as interactive, not as text |
| `--color-on-primary` | `#FFFFFF` | `#FFFFFF` | As-is |
| `--color-destructive` | `#DC2626` | — | Unused; the page has no destructive actions |

Additional tokens required by the aesthetic: `--grid-line: rgba(37, 99, 235, 0.07)` (blueprint substrate), `--color-surface: #FFFFFF`, `--color-muted-foreground: #64748B`.

**Dark theme** (the skill covers dark support but emits no values; generated per `color-dark-mode` — desaturated tonal variants, not inverted)

| Token | Value |
|---|---|
| `--color-background` | `#0B1220` — deep navy, the backlit-screen state |
| `--color-surface` | `#111C31` |
| `--color-foreground` | `#E6EDF7` |
| `--color-secondary` | `#A9B8CC` |
| `--color-muted-foreground` | `#8595AB` |
| `--color-accent` | `#60A5FA` — lightened and desaturated for dark surfaces |
| `--color-border` | `rgba(148, 163, 184, 0.20)` |
| `--grid-line` | `rgba(96, 165, 250, 0.08)` |

Contrast verification (target AA 4.5:1 body, 3:1 large/UI):
`#0B1220` on `#F8FAFC` ≈ 18.4:1 · `#2563EB` on `#F8FAFC` ≈ 5.6:1 · `#64748B` on `#F8FAFC` ≈ 4.8:1 · `#E6EDF7` on `#0B1220` ≈ 15.6:1 · `#60A5FA` on `#0B1220` ≈ 7.4:1 · `#8595AB` on `#0B1220` ≈ 6.1:1. All pass.

### Typography

Deviation: the skill recommends **Crimson Pro** (heading, serif) + **Atkinson Hyperlegible** (body). **Reason for override:** Crimson Pro is a literary serif — correct for a humanities journal, wrong for the Blueprint aesthetic, which is built on drafting and instrumentation conventions where serifs do not appear. A supplementary `--domain typography` query for `"technical engineering precise sans monospace data"` returned the **Developer Mono** pairing, also from the skill's own database, which fits the design context directly.

- **Body / headings:** IBM Plex Sans — designed for IBM's technical documentation; neutral, engineered, excellent at small sizes. Weights 400 / 500 / 600.
- **Metadata, labels, figures:** JetBrains Mono — venue tags, dates, section numbers, and quantitative results. Weights 400 / 500.

```css
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');
```

Type scale (16px base, satisfying the skill's `readable-font-size` check; the reference's 14px is rejected as below the mobile minimum):

| Role | Size | Weight | Tracking |
|---|---|---|---|
| Name (h1) | `clamp(2rem, 4vw, 2.75rem)` | 600 | `-0.02em` |
| Section head (h2) | `0.8125rem` mono, uppercase | 500 | `0.12em` |
| Paper title (h3) | `1.0625rem` | 600 | `-0.01em` |
| Body | `1rem` / 1.65 | 400 | normal |
| Metadata | `0.8125rem` mono | 400 | `0.01em` |
| Micro-label | `0.6875rem` mono, uppercase | 500 | `0.14em` |

Numerals use `font-variant-numeric: tabular-nums` throughout, per `number-tabular` — this page is full of percentages and frequencies.

### Effects

- **Transitions:** 160ms `ease-out` on color and border-color; 200ms on theme switch. Within the skill's 150–300ms window.
- **Motion:** no scroll-triggered reveals, no parallax, no entrance staggering. Per `motion-meaning`, every transition here expresses a state change (hover, focus, theme) and nothing is decorative.
- **Reduced motion:** `@media (prefers-reduced-motion: reduce)` collapses all durations to 0.01ms.
- **Shadows:** none in light mode — replaced by hairline borders (see Aesthetic Implementation). Dark mode uses one flat surface lift only where a panel must separate from the background.

### Anti-patterns to Avoid

From the skill: corporate templates, generic layouts, emoji as icons, removed focus rings, gray-on-gray text, raw hex in components, body text under 12px, animating width/height, color as the sole carrier of meaning.

From the Design Context: gradient heroes, CTA buttons, testimonial cards, floating rounded cards on soft gray, full-bleed decorative imagery, scroll-driven motion.

### Aesthetic Implementation

Blueprint Scholar translated into concrete CSS. This is the bridge between the aesthetic choice and the build.

**Layout structure**

Single centered column, `max-width: 780px`, with a fixed right-rail scroll-progress nav (adopted from the reference's `.section-drip-nav`): small dots, one per section, the active one filled with accent and widened into a short bar. The rail is `position: fixed` at `right: clamp(1.5rem, 4vw, 3rem)`, vertically centered, hidden below 1100px and hidden when the footer enters view. Page content is a single flow of `<section>` elements; publications are full-width rows (teaser image above, metadata below), not a card grid — a grid would fragment the reading order and shrink the figures that carry the evidence.

**Surface treatment**

```css
/* No cards. Regions are delimited by hairlines and grid alignment. */
.entry {
  background: transparent;
  border: 0;
  border-top: 1px solid var(--color-border);   /* hairline rule, drafting-style */
  border-radius: 0;
  box-shadow: none;
}
.teaser {
  border: 1px solid var(--color-border);
  border-radius: 2px;                           /* near-sharp; a drawn frame, not a card */
}
```

Corner radius is `0` for structural regions and `2px` where a frame surrounds an image. `box-shadow` is forbidden in light mode.

**Typography expression**

Headings sit only one step above body in weight (600 vs 400) — hierarchy is carried by the mono/sans switch and by letter-spacing, not by size jumps. Section headings are small uppercase monospace with `0.12em` tracking and a hairline rule running to the right edge of the column, echoing a drawing's title block. Body is IBM Plex Sans at `1rem/1.65`, measure capped near 72 characters.

**Decorative rules**

Present: the grid substrate; hairline rules; small mono coordinate labels on section headings (`01`, `02`, …); a 1px accent left-edge marker on the active nav dot.
Forbidden: shadows in light mode, gradients as backgrounds, rounded cards, glow effects, emoji, icon fills (icons are 1.5px stroke, `currentColor`), decorative dividers beyond the hairline, any animation not tied to a state change.

**Spatial rhythm**

Compact within a block, generous between them — a 4/8px scale throughout. Section gap `4.5rem` desktop / `3rem` mobile; entry gap `2rem`; inside an entry, `0.5rem` between title, authors, and venue. This is the reference's density register, with the airiness relocated to section boundaries per Principle 5.

**Signature CSS**

```css
:root {
  --grid: 26px;
}
/* 1. The blueprint substrate — a measurement surface, not a texture */
body::before {
  content: '';
  position: fixed;
  inset: 0;
  z-index: -1;
  pointer-events: none;
  background-image:
    linear-gradient(to right, var(--grid-line) 1px, transparent 1px),
    linear-gradient(to bottom, var(--grid-line) 1px, transparent 1px);
  background-size: var(--grid) var(--grid);
  mask-image: radial-gradient(ellipse 120% 80% at 50% 0%, #000 35%, transparent 78%);
}
/* 2. Hairline rules replace every shadow */
.rule { border-top: 1px solid var(--color-border); }
/* 3. Section heads as drafting title blocks */
.section-head {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.8125rem;
  font-weight: 500;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--color-accent);
}
/* 4. Sharp corners — frames, not cards */
* { border-radius: 0; }
.teaser, .avatar-frame { border-radius: 2px; }
/* 5. Tabular figures — this page is made of numbers */
body { font-variant-numeric: tabular-nums; }
```
