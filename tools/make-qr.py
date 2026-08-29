"""Regenerate the contact QR code from assets/ju-dong.vcf.

The .vcf file is the single source of truth: the QR payload is the file's exact
contents (with CRLF line endings, as vCard requires), so the downloadable card
and the scanned card can never drift apart.

    python3 tools/make-qr.py
"""

import pathlib

import segno

root = pathlib.Path(__file__).resolve().parent.parent
vcf = root / "assets" / "ju-dong.vcf"

payload = vcf.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\n", "\r\n")

qr = segno.make(payload, error="m")
print(f"version {qr.version}, {len(payload)} bytes payload")

qr.save(
    root / "assets" / "contact-qr.svg",
    kind="svg",
    scale=1,
    border=2,
    dark="#0B1220",
    light="#FFFFFF",
    omitsize=True,
    xmldecl=False,
    svgns=True,
    nl=False,
)
