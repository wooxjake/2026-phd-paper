from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable

from deep_translator import GoogleTranslator

ROOT = Path(__file__).resolve().parent

HEADER_FOOTER_PATTERNS = [
    re.compile(r"^\s*=+\s*PAGE\s+\d+\s*=+\s*$", re.IGNORECASE),
    re.compile(r"^\s*archiv\s+euromedica.*$", re.IGNORECASE),
    re.compile(r"^\s*download\s+article\s*\(pdf\)\s*$", re.IGNORECASE),
    re.compile(r"^\s*\d+\s*$"),
]

SECTION_HEADING_RE = re.compile(
    r"^(ABSTRACT|INTRODUCTION|MATERIALS\s+AND\s+METHODS|METHODS|RESULTS|DISCUSSION|CONCLUSIONS|FUNDING|CONFLICT\s+OF\s+INTEREST|REFERENCES)\s*$",
    re.IGNORECASE,
)
SUB_HEADING_RE = re.compile(
    r"^(Aim of the study|Materials\s+and\s+methods|Results)\s*:?\s*$",
    re.IGNORECASE,
)
CAPTION_RE = re.compile(r"^(Chart|Figure|Table)\s+\d+\s*[-–:]\s*(.+)$", re.IGNORECASE)


def is_boilerplate(line: str) -> bool:
    return any(p.match(line) for p in HEADER_FOOTER_PATTERNS)


def normalize_lines(text: str) -> list[str]:
    raw = text.splitlines()
    lines: list[str] = []
    for line in raw:
        if is_boilerplate(line):
            continue
        cleaned = line.rstrip()
        lines.append(cleaned)
    return lines


def extract_title(lines: list[str], fallback: str) -> str:
    for i, line in enumerate(lines[:120]):
        s = line.strip()
        if not s:
            continue
        if SECTION_HEADING_RE.match(s) or s.upper() in {"NEUROLOGY"}:
            continue
        if len(s) > 15 and s == s.upper() and not s.startswith("Cite as"):
            parts = [s]
            for nxt in lines[i + 1 : i + 5]:
                ns = nxt.strip()
                if not ns:
                    break
                if ns == ns.upper() and len(ns) > 2:
                    parts.append(ns)
                else:
                    break
            return " ".join(parts)
    return fallback


def extract_metadata(lines: list[str]) -> list[str]:
    meta: list[str] = []
    for line in lines[:180]:
        s = line.strip()
        if not s:
            continue
        if s.startswith("Cite as:") or s.startswith("Received") or s.startswith("Accepted") or s.startswith("Published"):
            meta.append(s)
        elif "DOI" in s:
            meta.append(s)
        elif "@" in s:
            meta.append(f"Contact: {s}")
    dedup: list[str] = []
    for m in meta:
        if m not in dedup:
            dedup.append(m)
    return dedup


def to_paragraphs(lines: list[str]) -> list[str]:
    paras: list[str] = []
    buf: list[str] = []

    def flush() -> None:
        nonlocal buf
        if not buf:
            return
        joined = " ".join(x.strip() for x in buf if x.strip())
        joined = re.sub(r"\s+", " ", joined).strip()
        if joined:
            paras.append(joined)
        buf = []

    for line in lines:
        s = line.strip()
        if not s:
            flush()
            continue
        if SECTION_HEADING_RE.match(s) or SUB_HEADING_RE.match(s) or CAPTION_RE.match(s):
            flush()
            paras.append(s)
            continue
        buf.append(s)
    flush()
    return paras


def split_long(text: str, limit: int = 4000) -> Iterable[str]:
    if len(text) <= limit:
        yield text
        return
    sentences = re.split(r"(?<=[.!?])\s+", text)
    chunk = ""
    for sent in sentences:
        if not sent:
            continue
        if len(chunk) + len(sent) + 1 > limit and chunk:
            yield chunk
            chunk = sent
        else:
            chunk = f"{chunk} {sent}".strip()
    if chunk:
        yield chunk


def translate_text(translator: GoogleTranslator, text: str) -> str:
    parts: list[str] = []
    for chunk in split_long(text):
        try:
            parts.append(translator.translate(chunk))
        except Exception:
            parts.append("[원문 추출 불명확]")
    out = " ".join(parts)
    return re.sub(r"\s+", " ", out).strip()


def heading_ko(h: str) -> str:
    if SECTION_HEADING_RE.match(h):
        return h.upper()
    if SUB_HEADING_RE.match(h):
        return f"### {h.rstrip(':')}"
    m = CAPTION_RE.match(h)
    if m:
        label = m.group(1)
        num = re.search(r"\d+", h)
        n = num.group(0) if num else "?"
        cap = m.group(2).strip()
        return f"### {label} {n} - {cap}"
    return h


def build_markdown(txt_path: Path, pdf_path: Path) -> str:
    text = txt_path.read_text(encoding="utf-8", errors="replace")
    lines = normalize_lines(text)
    title = extract_title(lines, pdf_path.stem)
    meta = extract_metadata(lines)
    paras = to_paragraphs(lines)

    translator = GoogleTranslator(source="auto", target="ko")
    out: list[str] = [f"# {title}", "", "## 논문 정보"]
    if meta:
        out.extend([f"- {m}" for m in meta])
    else:
        out.append("- [원문 추출 불명확]")
    out.append("")

    for p in paras:
        if SECTION_HEADING_RE.match(p):
            out.append(f"## {p.upper()}")
            out.append("")
            continue
        if SUB_HEADING_RE.match(p):
            out.append(f"### {p.rstrip(':')}")
            out.append("")
            continue
        cap = CAPTION_RE.match(p)
        if cap:
            label = cap.group(1)
            idx = re.search(r"\d+", p)
            num = idx.group(0) if idx else "?"
            cap_txt = translate_text(translator, cap.group(2).strip())
            out.append(f"### {label} {num} - {cap_txt}")
            out.append("- 이미지 재현: [원문 추출 불명확]")
            out.append("")
            continue

        translated = translate_text(translator, p)
        out.append(translated if translated else "[원문 추출 불명확]")
        out.append("")

    return "\n".join(out).strip() + "\n"


def main() -> None:
    pdfs = sorted(ROOT.glob("*.pdf"))
    made = 0
    skipped = 0
    failed: list[str] = []

    for pdf in pdfs:
        out_md = ROOT / f"{pdf.stem}_논문_번역.md"
        if out_md.exists():
            skipped += 1
            continue

        txt = ROOT / f"{pdf.stem}.txt"
        if not txt.exists():
            failed.append(f"{pdf.name}: missing txt")
            continue

        try:
            md = build_markdown(txt, pdf)
            out_md.write_text(md, encoding="utf-8")
            made += 1
            print(f"[OK] {out_md.name}")
        except Exception as e:
            failed.append(f"{pdf.name}: {e}")

    print(f"total_pdf={len(pdfs)} skipped={skipped} created={made} failed={len(failed)}")
    if failed:
        print("-- failed --")
        for f in failed:
            print(f)


if __name__ == "__main__":
    main()
