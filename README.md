# Ju Dong — Academic Homepage

Personal academic homepage. Live at **https://ju6276.github.io**.

A single static `index.html` with no build step, no framework, and no dependencies beyond two Google Fonts. Edit the file, commit, push — GitHub Pages redeploys automatically.

## Files

| Path | Purpose |
|---|---|
| `index.html` | The entire site — markup, styles, and scripts inline |
| `assets/` | Avatar, publication teaser figures, and the WeChat QR (WebP) |
| `page-story.md` | Content source of truth: About, Links, News, Publications, Education, Experience, Service, Contact |
| `docs/plans/` | Design doc, implementation plan, and audit report |

## Editing content

`page-story.md` is the authoritative content record. Update it first, then mirror the change into `index.html`. Keeping the two in sync means the page can be regenerated from the story at any time.

Adding a publication means duplicating one `<article class="pub">` block: teaser figure, title, author list with `<span class="me">Ju Dong</span>`, a venue tag, a one-sentence summary, and the link row.

## Local preview

```bash
python3 -m http.server 8137 --bind 127.0.0.1
```

Then open http://127.0.0.1:8137.

## Adding a teaser figure

Teasers are cropped from the paper's Figure 1 and converted to WebP:

```bash
python3 -c "
import fitz
d = fitz.open('paper.pdf'); p = d[0]
boxes = [p.get_image_bbox(i) for i in p.get_images(full=True)]
u = boxes[0]
for b in boxes[1:]: u = u | b
print(u)  # use this rect as the clip below
p.get_pixmap(dpi=240, clip=u).save('teaser.png')
"
python3 -c "
from PIL import Image
im = Image.open('teaser.png').convert('RGB')
im.resize((1400, round(im.height*1400/im.width))).save('assets/name.webp', 'WEBP', quality=88, method=6)
"
```

Declare the resulting `width` and `height` on the `<img>` so the page reserves space and avoids layout shift.

## Contact QR code

`assets/wechat-qr.webp` is the WeChat code, cropped out of the app's share screenshot so the nickname and avatar are not published alongside it. To replace it, crop the code itself with a white margin around it and keep the square aspect ratio:

```bash
python3 -c "
from PIL import Image
im = Image.open('wechat-screenshot.png').convert('RGB')
im.crop((86, 238, 716, 869)).resize((600, 600), Image.LANCZOS).save('assets/wechat-qr.webp', 'WEBP', lossless=True, method=6)
"
```

WeChat invalidates the old code if you regenerate it in the app, so re-export this file whenever that happens.

## Design

Aesthetic direction is "Blueprint Scholar": a cool blue palette, a low-opacity drafting grid, hairline rules instead of shadows, sharp corners, and monospace metadata. Colors are CSS custom properties under `:root` and `[data-theme="dark"]` — change a token there and both themes follow.

Full rationale, the design system, and the audit report are in `docs/plans/`.

Built with [PageClaw](https://github.com/XY-Showing/pageclaw).
