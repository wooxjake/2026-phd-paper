# 역할: Copilot의 /add 요청에서 참고문헌 상태를 확인하고 원문 PDF 텍스트를 추출한다.
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


TITLE_PATTERN = re.compile(r"^\s*/add\s+(?P<title>.+?)\s*$", re.DOTALL)
TRANSLATION_PATTERN = re.compile(r"(논문_번역|번역|translation|translated)$", re.IGNORECASE)
STATUS_PATTERN = re.compile(r"-\s*\*\*상태\*\*:\s*(candidate|cited)", re.IGNORECASE)


def emit(message: str | None = None) -> None:
    result: dict[str, Any] = {"continue": True}
    if message:
        result["systemMessage"] = message
    print(json.dumps(result, ensure_ascii=False))


def normalized_key(value: str) -> str:
    name = value.replace("°", " degree ")
    name = re.sub(r"(_논문_번역|논문_번역|_translation|_translated|번역본)$", "", name, flags=re.IGNORECASE)
    name = re.sub(r"[_-]+", " ", name)
    name = re.sub(r"[^\w\d]+", " ", name, flags=re.UNICODE).lower()
    return re.sub(r"\s+", " ", name).strip()


def title_key(title: str) -> str:
    return normalized_key(Path(title).stem)


def text_contains_title(text: str, title: str) -> bool:
    requested_tokens = set(normalized_key(title).split())
    if not requested_tokens:
        return False
    requested_key = normalized_key(title)
    for line in text.splitlines():
        line_key = normalized_key(line)
        if requested_key and requested_key in line_key:
            return True
        line_tokens = set(line_key.split())
        shared_ratio = len(requested_tokens & line_tokens) / len(requested_tokens)
        if shared_ratio >= 0.8:
            return True
    return False


def token_similarity(left: str, right: str) -> float:
    if left == right:
        return 1.0
    if len(left) >= 12 and (left in right or right in left):
        return 0.95

    left_tokens = {token for token in left.split() if len(token) > 1}
    right_tokens = {token for token in right.split() if len(token) > 1}
    if not left_tokens or not right_tokens:
        return 0.0
    return len(left_tokens & right_tokens) / len(left_tokens | right_tokens)


def project_root(hook_input: dict[str, Any]) -> Path:
    raw_root = hook_input.get("cwd") or os.environ.get("VSCODE_WORKSPACE_FOLDER") or os.getcwd()
    root = Path(str(raw_root)).resolve()
    return root if root.is_dir() else root.parent


def relative_path(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root).as_posix()


def tail(text: str, limit: int = 2000) -> str:
    text = text.strip()
    return text if len(text) <= limit else text[-limit:]


def is_nonempty_text(path: Path) -> bool:
    try:
        return path.is_file() and path.stat().st_size > 0 and bool(path.read_text(encoding="utf-8", errors="replace").strip())
    except OSError:
        return False


def extract_original_text(pdf_path: Path, root: Path) -> tuple[list[Path], list[str]]:
    extractor = root / "references" / "extract_pdf_text.py"
    python_path = root / ".venv" / "Scripts" / "python.exe"
    if not python_path.is_file():
        python_path = Path(sys.executable)

    if not extractor.is_file():
        return [], ["Original text extraction: unavailable because extract_pdf_text.py was not found."]
    if not python_path.is_file():
        return [], ["Original text extraction: unavailable because no Python executable was found."]

    output_path = pdf_path.with_suffix(".txt")
    try:
        completed = subprocess.run(
            [str(python_path), str(extractor), str(pdf_path)],
            cwd=str(root),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
    except OSError as error:
        return [], [f"Original text extraction: failed to start ({error})."]

    report = tail(completed.stdout + (f"\n{completed.stderr}" if completed.stderr else ""))
    if completed.returncode == 0 and is_nonempty_text(output_path):
        messages = [f"Original text extraction: completed ({relative_path(output_path, root)})"]
        if report:
            messages.append(f"Extraction report:\n{report}")
        return [output_path], messages

    if completed.returncode == 0 and output_path.is_file():
        messages = [
            "Original text extraction: completed, but no text was extracted; OCR may be required.",
        ]
        if report:
            messages.append(f"Extraction report:\n{report}")
        return [], messages

    messages = [f"Original text extraction: failed (exit code {completed.returncode})."]
    if report:
        messages.append(f"Extraction report:\n{report}")
    return [], messages


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, TypeError) as error:
        emit(f"Reference-add Hook could not parse its input: {error}")
        return

    prompt = str(hook_input.get("prompt") or hook_input.get("userPrompt") or "")
    match = TITLE_PATTERN.fullmatch(prompt)
    if not match:
        emit()
        return

    requested_title = match.group("title").strip()
    if len(requested_title) >= 2 and requested_title[0] == requested_title[-1] and requested_title[0] in "\"'":
        requested_title = requested_title[1:-1].strip()
    requested_title = re.sub(r"^#+\s*", "", requested_title).strip()
    if not requested_title:
        emit("Reference-add request: no paper title was supplied after /add. Ask for the exact title and do not change files.")
        return

    root = project_root(hook_input)
    references_root = root / "references"
    if not references_root.is_dir():
        emit(f"Reference-add request for '{requested_title}': references/ does not exist. Do not create a record.")
        return

    candidates: dict[str, dict[str, Any]] = {}
    for path in references_root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".pdf", ".txt", ".md"}:
            continue
        key = title_key(path.name)
        if len(key) < 5:
            continue
        candidates.setdefault(key, {"title": path.stem, "key": key, "paths": []})["paths"].append(path)

    requested_key = title_key(requested_title)
    ranked = sorted(
        candidates.values(),
        key=lambda candidate: (-token_similarity(requested_key, candidate["key"]), candidate["title"].lower()),
    )
    top_matches = ranked[:3]
    selected = top_matches[0] if top_matches and token_similarity(requested_key, top_matches[0]["key"]) >= 0.55 else None

    if selected is None:
        nearby = "\n".join(
            f"- {candidate['title']} (similarity {round(token_similarity(requested_key, candidate['key']) * 100)}%)"
            for candidate in top_matches
        ) or "- No local reference files were found."
        emit(
            "Reference-add state report (Copilot Hook)\n"
            f"Requested title: {requested_title}\n"
            "No local candidate reached the 55% title-similarity threshold.\n"
            f"Nearest local titles:\n{nearby}\n\n"
            "Required follow-up: verify title, authors, year, and DOI/PMID from an authoritative record before creating files. "
            "If an authorized original PDF is later placed in references/, run references/extract_pdf_text.py before completing the card. "
            "If extraction reports no text, mark OCR as required and do not invent an original-text citation. "
            "Do not modify introduce.md or treat search1.md, search2.md, or search3.md as evidence."
        )
        return

    paths: list[Path] = selected["paths"]
    pdf_paths = [path for path in paths if path.suffix.lower() == ".pdf"]
    source_text_paths = [
        path for path in paths
        if path.suffix.lower() == ".txt"
        and not TRANSLATION_PATTERN.search(path.stem)
        and is_nonempty_text(path)
    ]
    translation_paths = [path for path in paths if TRANSLATION_PATTERN.search(path.stem)]
    extraction_messages: list[str] = []

    if pdf_paths and not source_text_paths:
        source_text_paths, extraction_messages = extract_original_text(pdf_paths[0], root)
    elif source_text_paths:
        extraction_messages.append("Original text extraction: skipped because a non-translation .txt already exists.")

    index_path = root / "references.md"
    index_text = index_path.read_text(encoding="utf-8") if index_path.is_file() else ""
    registered_in_index = text_contains_title(index_text, requested_title)

    entries_root = references_root / "entries"
    entry_paths: list[Path] = []
    entry_statuses: list[str] = []
    if entries_root.is_dir():
        for entry_path in entries_root.glob("*.md"):
            entry_text = entry_path.read_text(encoding="utf-8", errors="replace")
            if text_contains_title(entry_text, requested_title):
                entry_paths.append(entry_path)
                status_match = STATUS_PATTERN.search(entry_text)
                if status_match:
                    entry_statuses.append(status_match.group(1).lower())

    detected_files = "\n".join(f"- {relative_path(path, root)}" for path in paths[:8])
    nearby = "\n".join(
        f"- {candidate['title']} (similarity {round(token_similarity(requested_key, candidate['key']) * 100)}%)"
        for candidate in top_matches
    )
    extraction_state = "\n".join(extraction_messages) or "Original text extraction: skipped because no source PDF was found."
    index_state = "registered" if registered_in_index else "missing"
    entry_state = f"registered ({len(entry_paths)})" if entry_paths else "missing"
    status_state = ", ".join(sorted(set(entry_statuses))) if entry_statuses else "not found"

    emit(
        "Reference-add state report (Copilot Hook)\n"
        f"Requested title: {requested_title}\n"
        f"Selected local candidate: {selected['title']} (similarity {round(token_similarity(requested_key, selected['key']) * 100)}%)\n"
        f"Other nearby titles:\n{nearby}\n\n"
        f"Detected files:\n{detected_files}\n"
        f"Original PDF: {'available' if pdf_paths else 'missing'}\n"
        f"Non-translation original text (.txt): {'available' if source_text_paths else 'missing'}\n"
        f"Translation file: {'available' if translation_paths else 'missing'}\n"
        f"references.md index: {index_state}\n"
        f"references/entries card: {entry_state}\n"
        f"Entry status: {status_state}\n"
        f"{extraction_state}\n\n"
        "Required follow-up: verify title, authors, year, and DOI/PMID from an authoritative record. "
        "The Hook has attempted extraction whenever a local PDF existed and the original TXT was missing or empty. "
        "Use the extraction report above; if no text was extracted, mark OCR as required and do not invent quotations. "
        "Create only missing references.md and references/entries records, keep unverified records as candidate, "
        "do not modify introduce.md, and do not change cited status automatically."
    )


if __name__ == "__main__":
    main()
