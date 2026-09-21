#!/usr/bin/env python3
"""Build a deduplicated, OCR-ready corpus from the 2017–2023 topical PDF."""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

import pypdfium2 as pdfium
from pypdf import PdfReader


ENTRY_RE = re.compile(
    r"\((9702)/(4[123])_(Summer|Winter|March)_(20\d{2})_Q(\d+)\)\s*-\s*([^|]+)"
)
CHAPTER_RE = re.compile(r"^(CH\d+\s*-\s*[^|]+|QUANTUM PHYSICS|PARTICLE & NUCLEAR PHYSICS|MEDICAL PHYSICS|ASTRONOMY & COSMOLOGY)")


def safe_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]+", "-", value).strip("-")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("out_dir", type=Path)
    parser.add_argument("catalog", type=Path)
    parser.add_argument("--max-year", type=int, default=2021)
    parser.add_argument("--scale", type=float, default=1.8)
    args = parser.parse_args()

    reader = PdfReader(str(args.pdf))
    entries = []
    current_chapter = ""
    for page_idx in range(1, 692):  # question pages only; 0-based indices
        text = (reader.pages[page_idx].extract_text() or "").replace("\n", " | ")
        chapter_match = CHAPTER_RE.search(text)
        if chapter_match:
            current_chapter = chapter_match.group(1).strip()
        match = ENTRY_RE.search(text)
        if not match:
            continue
        _, variant, session, year, question, topics = match.groups()
        entries.append(
            {
                "page_idx": page_idx,
                "pdf_page": page_idx + 1,
                "variant": variant,
                "session": session,
                "year": int(year),
                "question": int(question),
                "topics": topics.strip(),
                "chapter": current_chapter,
            }
        )

    for idx, entry in enumerate(entries):
        next_start = entries[idx + 1]["page_idx"] if idx + 1 < len(entries) else 692
        entry["end_page_idx"] = next_start - 1
        entry["page_count"] = next_start - entry["page_idx"]

    grouped = defaultdict(list)
    for entry in entries:
        if entry["year"] <= args.max_year:
            key = (entry["year"], entry["session"], entry["variant"], entry["question"])
            grouped[key].append(entry)

    selected = []
    for key, occurrences in sorted(grouped.items()):
        # Prefer the most complete occurrence; ties use the earliest PDF occurrence.
        chosen = sorted(occurrences, key=lambda item: (-item["page_count"], item["page_idx"]))[0].copy()
        chosen["all_occurrences"] = [
            {
                "pdf_page": item["pdf_page"],
                "page_count": item["page_count"],
                "chapter": item["chapter"],
                "topics": item["topics"],
            }
            for item in occurrences
        ]
        chosen["question_id"] = f"9702/{chosen['variant']}_{chosen['session']}_{chosen['year']}_Q{chosen['question']}"
        selected.append(chosen)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    pdf = pdfium.PdfDocument(str(args.pdf))
    image_records = []
    for q_index, entry in enumerate(selected, start=1):
        entry["images"] = []
        for local_index, page_idx in enumerate(range(entry["page_idx"], entry["end_page_idx"] + 1), start=1):
            stem = safe_name(entry["question_id"])
            image_path = args.out_dir / f"{q_index:03d}_{stem}_p{page_idx + 1:03d}_{local_index:02d}.jpg"
            bitmap = pdf[page_idx].render(scale=args.scale)
            bitmap.to_pil().convert("RGB").save(image_path, quality=90, optimize=True)
            entry["images"].append(str(image_path))
            image_records.append({"question_id": entry["question_id"], "pdf_page": page_idx + 1, "path": str(image_path)})

    payload = {
        "source": str(args.pdf),
        "max_year": args.max_year,
        "entry_count": len(entries),
        "unique_question_count": len(selected),
        "rendered_page_count": len(image_records),
        "questions": selected,
        "images": image_records,
    }
    args.catalog.parent.mkdir(parents=True, exist_ok=True)
    args.catalog.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({key: payload[key] for key in ("entry_count", "unique_question_count", "rendered_page_count")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
