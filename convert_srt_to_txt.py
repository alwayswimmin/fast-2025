#!/usr/bin/env python3
import os
import re
from pathlib import Path

SRC_DIR = Path("srt")
OUT_DIR = Path("txt")

# create output dir
OUT_DIR.mkdir(exist_ok=True)

def srt_to_text(srt_content: str) -> str:
    """
    Convert SRT subtitle content to plain text by:
    - removing numbering
    - removing timestamps
    - collapsing multiple newlines
    """
    # Remove index lines (e.g., "12")
    no_index = re.sub(r'^\d+\s*$', '', srt_content, flags=re.MULTILINE)

    # Remove timestamps
    no_timestamps = re.sub(
        r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}',
        '',
        no_index
    )

    # Remove leftover blank lines
    cleaned = re.sub(r'\n\s*\n', '\n', no_timestamps)

    return cleaned.strip()


def process_all_srts():
    for srt_path in SRC_DIR.glob("*.srt"):
        text = srt_to_text(srt_path.read_text(encoding="utf-8", errors="ignore"))

        out_path = OUT_DIR / (srt_path.stem + ".txt")
        out_path.write_text(text, encoding="utf-8")

        print(f"Converted: {srt_path.name} → {out_path.name}")


if __name__ == "__main__":
    process_all_srts()
    print("Done.")

