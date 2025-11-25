#!/usr/bin/env python3
import os
from pathlib import Path
import time

from openai import OpenAI
from openai import APIError, RateLimitError

# ---------- CONFIG ----------
TXT_DIR = Path("txt")
OUT_DIR = Path("summary")
# MODEL = "gpt-4o-mini"  # change to another model if you prefer
MODEL = "gpt-5.1"  # change to another model if you prefer
MAX_RETRIES = 3
# ----------------------------

def get_client():
    # Uses OPENAI_API_KEY from environment
    # export OPENAI_API_KEY="sk-..."
    return OpenAI()

def summarize_text(client, text, filename_for_context):
    """
    Call OpenAI to summarize a transcript.
    """
    prompt = f"""
You are summarizing a transcript from an audio or video talk.

Filename (for context only): {filename_for_context}

Please produce a detailed, structured summary with:
- A 2–3 sentence high-level overview
- An introduction of the speaker, their background, credentials, and current affiliations (university, research group, company, etc)
- A bullet-point list of the main sections or topics, in order

Then, for every item in the list of main sections or topics, generate a summary containing key takeaways, actionable points, Include definitions, examples, and explanations as necessary.  Cap each section summary to 5 sentences.

Write clearly in plain English.
"""

    messages = [
        {"role": "system", "content": "You are an expert note-taker and summarizer."},
        {"role": "user", "content": prompt},
        {"role": "user", "content": text},
    ]

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                temperature=0.2,
            )
            return resp.choices[0].message.content.strip()
        except RateLimitError as e:
            wait = 5 * attempt
            print(f"Rate limit hit (attempt {attempt}/{MAX_RETRIES}). Sleeping {wait}s...")
            time.sleep(wait)
        except APIError as e:
            print(f"API error on attempt {attempt}/{MAX_RETRIES}: {e}")
            wait = 5 * attempt
            time.sleep(wait)

    raise RuntimeError("Failed to summarize after multiple retries.")

def main():
    if not TXT_DIR.exists():
        print(f"Input directory '{TXT_DIR}' does not exist.")
        return

    OUT_DIR.mkdir(exist_ok=True)

    client = get_client()

    txt_files = sorted(TXT_DIR.glob("*.txt"))
    if not txt_files:
        print(f"No .txt files found in '{TXT_DIR}'.")
        return

    for txt_path in txt_files:
        out_path = OUT_DIR / (txt_path.stem + ".summary.txt")

        # Skip if already summarized (optional; comment this out if you want to overwrite)
        if out_path.exists():
            print(f"Skipping existing summary: {out_path.name}")
            continue

        print(f"Summarizing: {txt_path.name} → {out_path.name}")

        text = txt_path.read_text(encoding="utf-8", errors="ignore")

        # Quick sanity guard against empty or tiny files
        if len(text.strip()) < 50:
            print(f"  File too short or empty, writing trivial summary.")
            out_path.write_text("Transcript too short or empty to summarize.", encoding="utf-8")
            continue

        try:
            summary = summarize_text(client, text, txt_path.name)
            out_path.write_text(summary, encoding="utf-8")
        except Exception as e:
            print(f"  ERROR summarizing {txt_path.name}: {e}")

    print("Done summarizing all transcripts.")

if __name__ == "__main__":
    main()

