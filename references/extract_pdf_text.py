from __future__ import annotations

from pathlib import Path
import sys

from pypdf import PdfReader


def extract_text(pdf_path: Path) -> tuple[str, list[int]]:
    reader = PdfReader(pdf_path)
    pages: list[str] = []
    empty_pages: list[int] = []

    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text() or ""
        if page_text.strip():
            pages.append(f"\n\n===== PAGE {page_number} =====\n\n{page_text.strip()}")
        else:
            empty_pages.append(page_number)

    return "".join(pages).lstrip(), empty_pages


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python extract_pdf_text.py <pdf_path>")

    pdf_path = Path(sys.argv[1]).resolve()
    if not pdf_path.is_file():
        raise SystemExit(f"PDF file not found: {pdf_path}")

    text, empty_pages = extract_text(pdf_path)
    output_path = pdf_path.with_suffix(".txt")
    output_path.write_text(text, encoding="utf-8")

    reader = PdfReader(pdf_path)
    print(f"Total pages: {len(reader.pages)}")
    print(f"Pages with text: {len(reader.pages) - len(empty_pages)}")
    print(f"Empty pages: {empty_pages or 'None'}")
    print(f"Characters extracted: {len(text)}")
    print(f"Output: {output_path}")


if __name__ == "__main__":
    main()
