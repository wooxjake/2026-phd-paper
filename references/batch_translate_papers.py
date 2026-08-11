from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable, NamedTuple, Protocol

from deep_translator import GoogleTranslator

ROOT = Path(__file__).resolve().parent

PAGE_MARKER_RE = re.compile(r"^=+\s*PAGE\s+(\d+)\s*=+$", re.IGNORECASE)
NUM_SECTION_RE = re.compile(r"^\d+\.\s+.+$")
NUM_SUBSECTION_RE = re.compile(r"^\d+\.\d+\.\s+.+$")
KEYWORDS_RE = re.compile(r"^Keywords:\s*(.+)$", re.IGNORECASE)
REFERENCE_ITEM_RE = re.compile(r"^\d+\.\s+")
AUTHOR_YEAR_REFERENCE_RE = re.compile(r"^[A-Z].*,\s(?:19|20)\d{2}[a-z]?\.")
AUTHOR_LIST_START_RE = re.compile(r"^[A-Z][A-Za-z'’€.-]+,\s+[A-Z]")
REFERENCE_YEAR_RE = re.compile(r"(?:19|20)\d{2}[a-z]?\.")
TABLE_NUMBER_RE = re.compile(r"^Table\s+(\d+)\b", re.IGNORECASE)
STANDALONE_TABLE_RE = re.compile(r"^Table\s+(\d+)\s*$", re.IGNORECASE)
MEAN_SD_RE = re.compile(r"[-−]?\d+(?:\.\d+)?\s*[±]\s*\d+(?:\.\d+)?")

HEADER_FOOTER_PATTERNS = [
    re.compile(r"^\s*archiv\s+euromedica.*$", re.IGNORECASE),
    re.compile(r"^\s*download\s+article\s*\(pdf\)\s*$", re.IGNORECASE),
    re.compile(r"^\s*Sensors\s+\d{4}.*$", re.IGNORECASE),
    re.compile(r"^\s*contents\s+lists\s+available\s+at\s+sciencedirect\s*$", re.IGNORECASE),
    re.compile(r"^\s*journal\s+homepage:.*$", re.IGNORECASE),
    re.compile(r"^\s*applied\s+ergonomics\s+xxx.*$", re.IGNORECASE),
    re.compile(r"^\s*applied\s+ergonomics\s*$", re.IGNORECASE),
    re.compile(r"^\s*please\s+cite\s+this\s+article\s+in\s+press\s+as:.*$", re.IGNORECASE),
    re.compile(r"^\s*[A-Z]\.[A-Z]\.\s+[A-Za-z'’.-]+\s+et\s+al\.\s*/\s*Applied\s+Ergonomics.*$", re.IGNORECASE),
    re.compile(r"^\s*.*Applied\s+Ergonomics\s*\(\d{4}\),\s*http://dx\.doi\.org/.*$", re.IGNORECASE),
    re.compile(r"^\s*BA\s+snoitpircsed.*$", re.IGNORECASE),
    re.compile(r"^\s*\d+\s*$"),
]

SECTION_HEADING_RE = re.compile(
    r"^(ABSTRACT|Abstract|HIGHLIGHTS|Highlights|INTRODUCTION|Introduction|MATERIALS\s+AND\s+METHODS|Materials\s+and\s+Methods|METHODS|Methods|RESULTS|Results|DISCUSSION|Discussion|CONCLUSIONS|Conclusion|Conclusions|SUPPLEMENTARY\s+MATERIALS|Supplementary\s+Materials|AUTHOR\s+CONTRIBUTIONS|Author\s+Contributions|FUNDING|Funding|DATA\s+AVAILABILITY\s+STATEMENT|Data\s+Availability\s+Statement|CONFLICTS?\s+OF\s+INTEREST|Conflicts?\s+of\s+Interest|REFERENCES|References|DISCLAIMER/PUBLISHER.?S\s+NOTE|Disclaimer/Publisher.?s\s+Note|RESEARCH\s+GAP,\s+CONTRIBUTION,\s+OBJECTIVES,\s+AND\s+HYPOTHESIS|Research\s+Gap,\s+Contribution,\s+Objectives,\s+and\s+Hypothesis)$",
    re.IGNORECASE,
)
SUB_HEADING_RE = re.compile(
    r"^(Aim of the study|Materials\s+and\s+methods|Results)\s*:?\s*$",
    re.IGNORECASE,
)
# PDF text extractors use different delimiters after the caption number, most
# commonly a period ("Figure 1.") rather than a dash or colon. The delimiter
# remains required so in-text references such as "Figure 3)" are not captions.
CAPTION_RE = re.compile(r"^(Chart|Figure|Table|Fig\.?)\s+\d+\s*[.\-–:]\s*(.+)$", re.IGNORECASE)

UNCLEAR_TEXT = "[원문 추출 불명확]"
GENERATED_STATUS = "<!-- Translation status: generated -->"
REVIEW_REQUIRED_STATUS = "<!-- Translation status: review-required -->"


class Translator(Protocol):
    def translate(self, text: str) -> str: ...


class SimpleTable(NamedTuple):
    headers: list[str]
    rows: list[list[str]]
    note: str | None


class ParsedDocument(NamedTuple):
    title: str
    metadata: list[str]
    paragraphs: list[str]
    simple_tables: dict[str, SimpleTable]


def is_boilerplate(line: str) -> bool:
    return any(p.match(line) for p in HEADER_FOOTER_PATTERNS)


def normalize_lines(text: str) -> list[str]:
    raw = text.splitlines()
    lines: list[str] = []
    for line in raw:
        marker = PAGE_MARKER_RE.match(line.strip())
        if marker:
            lines.append(f"<!-- Page {marker.group(1)} -->")
            continue
        if is_boilerplate(line):
            continue
        cleaned = line.rstrip()
        lines.append(cleaned)
    return lines


def merge_caption_lines(lines: list[str]) -> list[str]:
    merged: list[str] = []
    index = 0

    while index < len(lines):
        current = lines[index].strip()
        match = STANDALONE_TABLE_RE.match(current)
        if not match:
            merged.append(lines[index])
            index += 1
            continue

        next_index = index + 1
        while next_index < len(lines) and not lines[next_index].strip():
            next_index += 1

        if next_index >= len(lines):
            merged.append(lines[index])
            index += 1
            continue

        next_line = lines[next_index].strip()
        if (
            not PAGE_MARKER_RE.match(next_line)
            and not STANDALONE_TABLE_RE.match(next_line)
            and not CAPTION_RE.match(next_line)
            and not SECTION_HEADING_RE.match(next_line)
            and not SUB_HEADING_RE.match(next_line)
            and not NUM_SECTION_RE.match(next_line)
            and not NUM_SUBSECTION_RE.match(next_line)
        ):
            merged.append(f"Table {match.group(1)}. {next_line}")
            index = next_index + 1
            continue

        merged.append(lines[index])
        index += 1

    return merged


def merge_keyword_lines(lines: list[str]) -> list[str]:
    merged: list[str] = []
    index = 0

    while index < len(lines):
        current = lines[index].strip()
        if current.lower() != "keywords:":
            merged.append(lines[index])
            index += 1
            continue

        keywords: list[str] = []
        next_index = index + 1
        while next_index < len(lines):
            candidate = lines[next_index].strip()
            if (
                not candidate
                or PAGE_MARKER_RE.match(candidate)
                or SECTION_HEADING_RE.match(candidate)
                or SUB_HEADING_RE.match(candidate)
                or NUM_SECTION_RE.match(candidate)
                or NUM_SUBSECTION_RE.match(candidate)
                or CAPTION_RE.match(candidate)
                or STANDALONE_TABLE_RE.match(candidate)
            ):
                break
            keywords.append(candidate)
            next_index += 1

        if keywords:
            merged.append(f"Keywords: {'; '.join(keywords)}")
            index = next_index
            continue

        merged.append(lines[index])
        index += 1

    return merged


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


def extract_simple_tables(text: str) -> dict[str, SimpleTable]:
    """Return only tables whose columns and numeric rows can be verified from text."""
    lines = text.splitlines()
    tables: dict[str, SimpleTable] = {}

    for index, line in enumerate(lines):
        caption = line.strip()
        match = TABLE_NUMBER_RE.match(caption)
        if not match:
            continue

        caption_is_standalone = bool(STANDALONE_TABLE_RE.match(caption))

        content: list[str] = []
        for candidate in lines[index + 1 :]:
            value = candidate.strip()
            if not value or PAGE_MARKER_RE.match(value):
                continue
            if (
                TABLE_NUMBER_RE.match(value)
                or CAPTION_RE.match(value)
                or NUM_SECTION_RE.match(value)
                or NUM_SUBSECTION_RE.match(value)
            ):
                break
            content.append(value)

        if caption_is_standalone and content:
            content = content[1:]

        if len(content) < 3:
            continue

        headers = re.split(r"(?<=\))\s+(?=[A-Z])", content[0])
        if len(headers) < 2:
            continue

        rows: list[list[str]] = []
        note: str | None = None
        for value in content[1:]:
            numeric_values = MEAN_SD_RE.findall(value)
            if len(numeric_values) == len(headers):
                label = value[: value.find(numeric_values[0])].strip(" ,")
                if label:
                    rows.append([label, *numeric_values])
                continue
            if value.lower().startswith(("value", "values", "note", "notes")):
                note = value

        if len(rows) >= 2 and all(len(row) == len(headers) + 1 for row in rows):
            tables[f"Table {match.group(1)}"] = SimpleTable(headers, rows, note)

    return tables


def reference_has_year(parts: list[str]) -> bool:
    return bool(REFERENCE_YEAR_RE.search(" ".join(parts)))


def is_reference_item_start(line: str, active_reference: list[str] | None = None) -> bool:
    if REFERENCE_ITEM_RE.match(line):
        return True
    if AUTHOR_YEAR_REFERENCE_RE.match(line):
        if active_reference and not reference_has_year(active_reference) and AUTHOR_LIST_START_RE.match(line):
            return False
        return True
    if not AUTHOR_LIST_START_RE.match(line):
        return False
    if not active_reference:
        return True
    return reference_has_year(active_reference)


def to_paragraphs(lines: list[str]) -> list[str]:
    paras: list[str] = []
    buf: list[str] = []
    in_references = False
    active_reference: list[str] = []
    skip_reference_table_body = False

    def flush() -> None:
        nonlocal buf
        if not buf:
            return
        joined = " ".join(x.strip() for x in buf if x.strip())
        joined = re.sub(r"\s+", " ", joined).strip()
        if joined:
            paras.append(joined)
        buf = []

    def flush_reference() -> None:
        nonlocal active_reference
        if not active_reference:
            return
        joined = " ".join(x.strip() for x in active_reference if x.strip())
        joined = re.sub(r"\s+", " ", joined).strip()
        if joined:
            paras.append(f"__REF__ {joined}")
        active_reference = []

    for line in lines:
        s = line.strip()
        if not s:
            flush()
            continue
        if s.startswith("<!-- Page "):
            flush()
            paras.append(s)
            if in_references:
                skip_reference_table_body = False
            continue
        if in_references:
            if skip_reference_table_body:
                if is_reference_item_start(s, active_reference):
                    skip_reference_table_body = False
                else:
                    continue
            if is_reference_item_start(s, active_reference):
                flush_reference()
                active_reference = [s]
                continue
            if (
                CAPTION_RE.match(s)
                or STANDALONE_TABLE_RE.match(s)
                or SECTION_HEADING_RE.match(s)
                or SUB_HEADING_RE.match(s)
                or NUM_SUBSECTION_RE.match(s)
                or NUM_SECTION_RE.match(s)
            ):
                paras.append(s)
                if TABLE_NUMBER_RE.match(s):
                    skip_reference_table_body = True
                continue
            if active_reference:
                active_reference.append(s)
                continue
            buf.append(s)
            continue
        if KEYWORDS_RE.match(s):
            flush()
            paras.append(f"__KEYWORDS__ {KEYWORDS_RE.match(s).group(1)}")
            continue
        if s.startswith("•"):
            flush()
            paras.append(f"__BULLET__ {s.lstrip('•').strip()}")
            continue
        if (
            SECTION_HEADING_RE.match(s)
            or SUB_HEADING_RE.match(s)
            or NUM_SUBSECTION_RE.match(s)
            or NUM_SECTION_RE.match(s)
            or CAPTION_RE.match(s)
        ):
            flush()
            paras.append(s)
            if s.lower() == "references":
                in_references = True
            continue
        buf.append(s)
    flush()
    flush_reference()
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


def translate_text(translator: Translator, text: str) -> str:
    parts: list[str] = []
    for chunk in split_long(text):
        try:
            parts.append(translator.translate(chunk))
        except Exception:
            parts.append(UNCLEAR_TEXT)
    out = " ".join(parts)
    return re.sub(r"\s+", " ", out).strip()


def render_markdown_table(
    translator: Translator,
    headers: list[str],
    rows: list[list[str]],
    note: str | None,
) -> list[str]:
    translated_headers = [translate_text(translator, header) for header in headers]
    out = [
        f"| 변수 | {' | '.join(translated_headers)} |",
        f"| --- | {' | '.join(['---:' for _ in translated_headers])} |",
    ]
    for row in rows:
        out.append(
            f"| {translate_text(translator, row[0])} | {' | '.join(row[1:])} |"
        )
    if note:
        out.extend(["", f"주: {translate_text(translator, note)}"])
    return out


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


def parse_document(text: str, fallback_title: str) -> ParsedDocument:
    lines = merge_keyword_lines(merge_caption_lines(normalize_lines(text)))
    return ParsedDocument(
        title=extract_title(lines, fallback_title),
        metadata=extract_metadata(lines),
        paragraphs=to_paragraphs(lines),
        simple_tables=extract_simple_tables(text),
    )


def is_structural_paragraph(paragraph: str) -> bool:
    return bool(
        paragraph.startswith("<!-- Page ")
        or SECTION_HEADING_RE.match(paragraph)
        or SUB_HEADING_RE.match(paragraph)
        or NUM_SUBSECTION_RE.match(paragraph)
        or NUM_SECTION_RE.match(paragraph)
        or CAPTION_RE.match(paragraph)
    )


class MarkdownRenderer:
    def __init__(self, translator: Translator) -> None:
        self.translator = translator

    def render(self, document: ParsedDocument) -> str:
        out = [
            f"# {document.title}",
            "",
            GENERATED_STATUS,
            REVIEW_REQUIRED_STATUS,
            "",
            "## 논문 정보",
        ]
        if document.metadata:
            out.extend(f"- {item}" for item in document.metadata)
        else:
            out.append(f"- {UNCLEAR_TEXT}")
        out.append("")

        skip_table_body = False
        seen_body_content = False
        for paragraph in document.paragraphs:
            if skip_table_body:
                skip_table_body = False
                if not is_structural_paragraph(paragraph):
                    continue

            if is_structural_paragraph(paragraph) and not paragraph.startswith("<!-- Page "):
                seen_body_content = True

            if not seen_body_content and not (
                paragraph.startswith("<!-- Page ") or paragraph.startswith("__KEYWORDS__ ")
            ):
                continue

            rendered, skip_table_body = self._render_paragraph(
                paragraph, document.simple_tables
            )
            out.extend(rendered)

        return "\n".join(out).strip() + "\n"

    def _render_paragraph(
        self,
        paragraph: str,
        simple_tables: dict[str, SimpleTable],
    ) -> tuple[list[str], bool]:
        if paragraph.startswith("<!-- Page "):
            return [paragraph, ""], False
        if paragraph.startswith("__KEYWORDS__ "):
            keywords = paragraph.removeprefix("__KEYWORDS__ ")
            return [f"**Keywords:** {keywords}", ""], False
        if paragraph.startswith("__BULLET__ "):
            source = paragraph.removeprefix("__BULLET__ ")
            translated = translate_text(self.translator, source)
            return [f"- {translated or UNCLEAR_TEXT}"], False
        if paragraph.startswith("__REF__ "):
            return [paragraph.removeprefix("__REF__ "), ""], False
        if SECTION_HEADING_RE.match(paragraph):
            return [f"## {paragraph.upper()}", ""], False
        if SUB_HEADING_RE.match(paragraph):
            return [f"### {paragraph.rstrip(':')}", ""], False
        if NUM_SUBSECTION_RE.match(paragraph):
            return [f"### {paragraph}", ""], False
        if NUM_SECTION_RE.match(paragraph):
            return [f"## {paragraph}", ""], False

        caption = CAPTION_RE.match(paragraph)
        if caption:
            return self._render_caption(paragraph, caption, simple_tables)

        translated = translate_text(self.translator, paragraph)
        return [translated or UNCLEAR_TEXT, ""], False

    def _render_caption(
        self,
        paragraph: str,
        caption: re.Match[str],
        simple_tables: dict[str, SimpleTable],
    ) -> tuple[list[str], bool]:
        label = caption.group(1)
        number_match = re.search(r"\d+", paragraph)
        number = number_match.group(0) if number_match else "?"
        caption_text = translate_text(self.translator, caption.group(2).strip())
        out = [f"### {label} {number} - {caption_text}"]

        if label.lower() != "table":
            return [*out, "- 원본 이미지/도표: PDF 참조", ""], False

        table = simple_tables.get(f"Table {number}")
        if table:
            out.append("")
            out.extend(
                render_markdown_table(
                    self.translator, table.headers, table.rows, table.note
                )
            )
        else:
            out.extend(
                [
                    f"<!-- REVIEW REQUIRED: Table {number} -->",
                    "- 원본 표: PDF 참조",
                ]
            )
        out.append("")
        return out, True


def build_markdown(txt_path: Path, pdf_path: Path) -> str:
    text = txt_path.read_text(encoding="utf-8", errors="replace")
    document = parse_document(text, pdf_path.stem)
    translator = GoogleTranslator(source="auto", target="ko")
    return MarkdownRenderer(translator).render(document)


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
            print(f"[GENERATED: REVIEW REQUIRED] {out_md.name}")
        except Exception as e:
            failed.append(f"{pdf.name}: {e}")

    print(f"total_pdf={len(pdfs)} skipped={skipped} created={made} failed={len(failed)}")
    if failed:
        print("-- failed --")
        for f in failed:
            print(f)


if __name__ == "__main__":
    main()
