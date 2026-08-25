# Implementation Plan — Ju Dong Academic Homepage

**Spec:** `docs/plans/ju-dong-design.md` (Design Context + Design System + Aesthetic Implementation)
**Content source:** `page-story.md` (authoritative — render faithfully, do not add, remove, reorder, or reinterpret)
**Output:** `index.html` — single file, project root, no build step
**Assets:** `avatar.png`, `assets/m4diffuser_teaser.png`, `assets/flow2one_teaser.png` (paths relative to `index.html`)

Note on process: PageClaw Step 3 calls for the `writing-plans` skill, which is not distributed with the pageclaw repository (only 10 of the 11 referenced skills ship with it). This plan is written directly in the format that step requires — task-by-task, each with acceptance criteria — so the pipeline's artifact contract is preserved.

---

## Task 1 — Document skeleton and design tokens

Create `index.html` with `<!DOCTYPE html>`, `lang="en"`, `<meta charset>`, `<meta name="viewport" content="width=device-width, initial-scale=1">`, a descriptive `<title>` and `<meta name="description">`, plus Open Graph tags using `assets/m4diffuser_teaser.png`.

Inline all CSS in a single `<style>` block. Preconnect to `fonts.googleapis.com` and `fonts.gstatic.com`, then import IBM Plex Sans (400/500/600) and JetBrains Mono (400/500) with `display=swap`.

Define every color as a CSS custom property under `:root` (light) and `[data-theme="dark"]`, using the exact token values from the Design System tables. No raw hex anywhere below `:root`.

**Acceptance:** Page renders with correct fonts; toggling `data-theme` on `<html>` in devtools switches every color with no leftover hardcoded values.

## Task 2 — Blueprint grid substrate

Implement the `body::before` fixed grid from Signature CSS: dual `linear-gradient` at `--grid: 26px`, colored `--grid-line`, `z-index: -1`, `pointer-events: none`, faded by a radial `mask-image` so it is strongest at the top and dissolves down the page.

**Acceptance:** Grid is perceptible as structure but never competes with text (Principle 3). It does not scroll with content, does not intercept clicks, and is present in both themes at their respective `--grid-line` values.

## Task 3 — Header block (name, role, contact, avatar)

Two-column flex at desktop: text left, avatar right at 148px with a 1px framed border and `2px` radius; stacks to single column below 640px with the avatar first. `<h1>` is the name at `clamp(2rem, 4vw, 2.75rem)`, weight 600, tracking `-0.02em`. Below it, affiliation and role in `--color-secondary`.

Contact row renders the `## Links` section per Rendering Conventions: inline SVG icons, 1.5px stroke, `currentColor`, each wrapped in an `<a>` with `aria-label`. Email uses a generic envelope SVG; Google Scholar and GitHub use their Simple Icons glyphs. Hit areas ≥44×44px via padding.

**Acceptance:** Name, role, affiliation, and all three links visible above the fold at 1440×900 and at 375px width. Every icon link is keyboard-focusable with a visible accent ring. No emoji.

## Task 4 — Section heading component

Reusable pattern: a small monospace uppercase label at `0.8125rem` / `0.12em` tracking in `--color-accent`, prefixed by a zero-padded ordinal (`01`, `02`, …) in `--color-muted-foreground`, followed by a 1px hairline rule that extends to the right edge of the column — the drafting title-block motif.

**Acceptance:** Applied identically to all six sections. The ordinal is decorative-but-semantic (drafting convention) and marked `aria-hidden` so screen readers announce only the section name.

## Task 5 — About section

Render the three paragraphs from `## About Me` verbatim, at `1rem/1.65`, measure capped near 72 characters. Supervisor and lab links are inline `<a>` in accent, underlined on hover with `text-underline-offset`.

The avatar markdown in the page-story belongs to the header block (Task 3), not to this section's flow.

**Acceptance:** Text matches the page-story word for word. No promotion of any sentence into a hero or badge (page-story governs placement).

## Task 6 — Publications section

The most important block on the page. Each of the three entries renders as a full-width row separated by a hairline `border-top`:

1. Teaser figure (M4Diffuser and Flow-to-One-Step only), `width: 100%`, `aspect-ratio` declared to prevent CLS, `loading="lazy"` on entries below the fold, 1px framed border, `2px` radius, descriptive `alt`.
2. Title at `1.0625rem`, weight 600.
3. Author list at `0.9375rem` in `--color-secondary`, with **Ju Dong** at weight 600 in `--color-foreground` so the reader finds their own name instantly. Equal-contribution asterisks preserved.
4. Venue as a monospace micro-label; `IROS 2026` / `ICRA 2026` carry an accent hairline-bordered tag, the T-RO entry reads `UNDER REVIEW`. Per `color-not-only`, the tag's meaning is carried by its text, not by its color.
5. Summary sentence in `--color-muted-foreground`.
6. Link row: `arXiv` / `Project Page` as bordered text links, not buttons.

Order follows the page-story exactly: Flow-to-One-Step, M4Diffuser, ResponsibleRobotBench.

**Acceptance:** No card containers, no shadows, no grid fragmentation. Numbers render with tabular figures. Images reserve their space before loading. At 375px the figures remain legible and nothing overflows horizontally.

## Task 7 — News, Education, Experience, Patents, Talks

Per the Rendering Conventions' "prose is the absence of a design decision," each of these is a sequence in time and renders as a timeline, not a bullet list: a monospace date column on the left (`7.5rem`, tabular figures) and content on the right, joined by a hairline. Below 640px the date moves above its entry as a micro-label.

News keeps the page-story's ordering. Education and Experience use the same timeline component. Patents is a single entry. Talks is a single entry.

**Acceptance:** One shared timeline component, not five bespoke layouts. Dates align to a common baseline on desktop. Reading order in the DOM matches visual order.

## Task 8 — Right-rail scroll-progress nav

Fixed dot rail adapted from the reference's `.section-drip-nav`: one dot per section, `position: fixed`, vertically centered at `right: clamp(1.5rem, 4vw, 3rem)`. The active dot fills with accent and widens into a short bar. Uses `IntersectionObserver` to track the active section; clicking a dot scrolls to it via `scroll-behavior: smooth` on an anchor. Hidden below 1100px. Each dot is an `<a>` with an `aria-label` naming its section, and `aria-current="true"` on the active one.

**Acceptance:** Keyboard-reachable and announced correctly. Hidden — not merely transparent — on narrow viewports, so it is removed from the tab order there. Respects `prefers-reduced-motion` by disabling smooth scroll.

## Task 9 — Theme toggle

Sun/moon inline SVG button, top-right corner, ≥44×44px hit area. Initial theme from `prefers-color-scheme`; user choice persisted to `localStorage` and re-applied on load by a small inline script placed before the body renders to avoid a flash of wrong theme. `aria-label` updates to reflect the action.

**Acceptance:** No flash on reload in either stored state. Both themes independently meet the contrast figures recorded in the Design System. Toggle works with keyboard.

## Task 10 — Responsive and interaction states

Breakpoints at 640px, 1024px, 1100px (nav rail). Verify no horizontal scroll at 375px and 1200px. Every interactive element gets `:hover` and `:focus-visible` states — a 2px accent outline with offset for focus, color/border shift for hover, with `transition: 160ms ease-out` on color and border-color only. `@media (prefers-reduced-motion: reduce)` collapses durations.

**Acceptance:** Tab through the entire page — focus is visible at every stop and never lost. No layout shift on hover. Tested at 375, 640, 1024, 1440.

## Task 11 — Footer

Single hairline-separated line: name, year, and a note that the page is hosted on GitHub Pages. Sets `.is-footer-visible` on the nav rail via IntersectionObserver to fade it out, matching the reference behavior.

**Acceptance:** Nav rail disappears when the footer is in view and reappears on scroll up.

---

## Build Verification Checklist

Run before declaring the build complete:

- [ ] All interactive elements have `:hover` and `:focus-visible`
- [ ] At least 3 distinct typographic levels
- [ ] Consistent 4/8px spacing rhythm
- [ ] No horizontal scroll at 375px or 1200px
- [ ] Asset paths resolve relative to `index.html`
- [ ] No bounded region is predominantly empty
- [ ] `## Links` rendered as icon links with `aria-label`
- [ ] Blueprint aesthetic legible in the CSS — grid, hairlines, sharp corners, mono labels — not generic clean/modern
- [ ] Dual light/dark via custom properties, toggle, `localStorage`, `prefers-color-scheme` default
- [ ] Content matches `page-story.md` with nothing added, removed, or reordered
