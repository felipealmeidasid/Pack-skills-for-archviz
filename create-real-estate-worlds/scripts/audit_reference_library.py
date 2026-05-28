#!/usr/bin/env python3
"""Audit the real estate reference library using only the standard library."""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path


URL_RE = re.compile(r"https?://[^\s)>\"]+")
CARD_HEADING_RE = re.compile(r"^##\s+(.+)$", re.MULTILINE)

REQUIRED_INDEX = [
    "00-index/master-index.md",
    "00-index/usage-rules.md",
    "00-index/style-taxonomy.md",
]

REQUIRED_STYLE_FILES = [
    "style-brief.md",
    "project-links.md",
    "architects.md",
    "prompt-rules.md",
    "avoid.md",
]

REQUIRED_CARD_FIELDS = [
    "Source",
    "Link",
    "Author / Studio",
    "Location",
    "Type",
    "Useful for",
    "What to observe",
    "Rules extracted",
    "Do not copy",
    "Accessed",
]

RECOMMENDED_CONFIDENCE_FIELDS = [
    "Source type",
    "Verification status",
    "Rights status",
    "Original source found",
    "Copy risk",
]

RISKY_PHRASES = [
    "copy this facade",
    "copy the facade",
    "same composition",
    "exact style",
    "clone",
    "make it look like",
    "in the style of",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def has_field(card: str, field: str) -> bool:
    return re.search(rf"^\s*-\s+{re.escape(field)}\s*:", card, re.MULTILINE) is not None


def split_cards(text: str) -> list[tuple[str, str]]:
    matches = list(CARD_HEADING_RE.finditer(text))
    cards: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        cards.append((match.group(1).strip(), text[start:end]))
    return cards


def audit(root: Path) -> int:
    issues: list[str] = []
    warnings: list[str] = []

    if not root.exists() or not root.is_dir():
        print(f"ISSUE: reference library not found: {root}")
        return 2

    for item in REQUIRED_INDEX:
        if not (root / item).exists():
            issues.append(f"Missing required index file: {item}")

    style_root = root / "01-styles"
    if not style_root.exists():
        issues.append("Missing style folder: 01-styles/")
        style_folders: list[Path] = []
    else:
        style_folders = sorted(path for path in style_root.iterdir() if path.is_dir())
        if not style_folders:
            issues.append("No style folders found under 01-styles/.")

    for folder in style_folders:
        for filename in REQUIRED_STYLE_FILES:
            if not (folder / filename).exists():
                issues.append(f"Missing {filename} in {rel(folder, root)}")

    urls: defaultdict[str, list[str]] = defaultdict(list)
    for path in sorted(root.rglob("*.md")):
        text = read_text(path)
        if text.startswith("\ufeff"):
            issues.append(f"File has UTF-8 BOM: {rel(path, root)}")

        for url in URL_RE.findall(text):
            urls[url.rstrip(".,")] .append(rel(path, root))

        for line_number, line in enumerate(text.splitlines(), start=1):
            lowered = line.lower()
            if "avoid" in lowered or "do not" in lowered:
                continue
            for phrase in RISKY_PHRASES:
                if phrase in lowered:
                    warnings.append(f"Risky phrase `{phrase}` in {rel(path, root)}:{line_number}")

        if path.name == "project-links.md":
            cards = split_cards(text)
            if not cards:
                warnings.append(f"No reference cards found in {rel(path, root)}")
            for title, card in cards:
                for field in REQUIRED_CARD_FIELDS:
                    if not has_field(card, field):
                        issues.append(f"Missing required field `{field}` in card `{title}` ({rel(path, root)})")
                for field in RECOMMENDED_CONFIDENCE_FIELDS:
                    if not has_field(card, field):
                        warnings.append(f"Missing confidence field `{field}` in card `{title}` ({rel(path, root)})")

    for url, locations in sorted(urls.items()):
        unique_locations = sorted(set(locations))
        non_index_locations = [item for item in unique_locations if not item.startswith("00-index/")]
        if len(non_index_locations) <= 1:
            continue
        if len(unique_locations) > 1:
            warnings.append(f"Duplicate URL appears in multiple files: {url} -> {', '.join(unique_locations)}")

    print("# Reference Library Audit\n")
    print(f"- Root: `{root}`")
    print(f"- Markdown files: {len(list(root.rglob('*.md')))}")
    print(f"- Style folders: {len(style_folders)}")

    if issues:
        print("\n## Issues\n")
        for item in issues:
            print(f"- {item}")

    if warnings:
        print("\n## Warnings\n")
        for item in warnings:
            print(f"- {item}")

    if not issues and not warnings:
        print("\nNo issues found.")

    return 1 if issues else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit a real estate reference library.")
    parser.add_argument("reference_library", type=Path)
    args = parser.parse_args()
    return audit(args.reference_library)


if __name__ == "__main__":
    raise SystemExit(main())
