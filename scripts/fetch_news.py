#!/usr/bin/env python3
"""
fetch_news.py — Daily AI/ML research log updater for AI-Infrastructure-Research-Log

Queries the Hacker News Algolia API for AI/ML stories, filters by relevance,
selects the top 5 by score, and appends a dated entry to logs.md.

Usage:
    python scripts/fetch_news.py

Environment: Runs inside GitHub Actions via daily-research.yml workflow.
"""

import urllib.request
import json
import datetime
import os
import sys

# HN Algolia API endpoint
HN_API_URL = "https://hn.algolia.com/api/v1/search?query=AI+machine+learning&tags=story&hitsPerPage=50"

# Keywords to filter for AI/ML/infra relevance (any match = keep)
RELEVANT_KEYWORDS = [
    "llm", "language model", "gpt", "claude", "gemini", "mistral", "llama",
    "inference", "gpu", "cuda", "diffusion", "stable diffusion", "flux",
    "transformer", "rag", "embedding", "vector", "fine-tun", "lora", "qlora",
    "tts", "text-to-speech", "text to speech", "voice", "speech",
    "image generation", "video generation", "multimodal",
    "runpod", "vast.ai", "lambda labs", "serverless",
    "pytorch", "tensorflow", "jax", "triton",
    "ollama", "vllm", "hugging face", "huggingface",
    "automation", "pipeline", "workflow", "orchestrat",
    "neural", "deep learning", "machine learning", "artificial intelligence",
    "comfyui", "museTalk", "chatterbox", "whisper", "openai", "anthropic",
]

LOG_FILE = "logs.md"


def fetch_stories():
    """Fetch stories from Hacker News Algolia API."""
    try:
        with urllib.request.urlopen(HN_API_URL, timeout=30) as response:
            data = json.loads(response.read().decode("utf-8"))
        return data.get("hits", [])
    except Exception as e:
        print(f"Error fetching from HN API: {e}", file=sys.stderr)
        sys.exit(1)


def is_relevant(story):
    """Return True if the story title or URL contains at least one relevant keyword."""
    title = (story.get("title") or "").lower()
    url = (story.get("url") or "").lower()
    text = title + " " + url
    return any(kw in text for kw in RELEVANT_KEYWORDS)


def format_entry(rank, story):
    """Format a single story as a Markdown table row."""
    title = story.get("title", "Untitled").replace("|", "\\|")
    url = story.get("url") or f"https://news.ycombinator.com/item?id={story.get('objectID', '')}"
    hn_url = f"https://news.ycombinator.com/item?id={story.get('objectID', '')}"
    score = story.get("points", 0)
    return f"| {rank} | [{title}]({url}) | [HN Discussion]({hn_url}) | {score} |"


def build_log_section(stories):
    """Build a full dated Markdown section for today's top stories."""
    today = datetime.date.today().isoformat()
    lines = [
        f"## {today}",
        "",
        "| # | Title | Discussion | Score |",
        "|---|-------|-----------|-------|",
    ]
    for rank, story in enumerate(stories, start=1):
        lines.append(format_entry(rank, story))
    lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def append_to_log(section):
    """Append the new section to logs.md."""
    if not os.path.exists(LOG_FILE):
        print(f"{LOG_FILE} not found. Creating it.", file=sys.stderr)
        with open(LOG_FILE, "w") as f:
            f.write("# AI Infrastructure Research Log\n\n---\n\n")

    with open(LOG_FILE, "a") as f:
        f.write("\n" + section)

    print(f"Appended {LOG_FILE} successfully.")


def main():
    print("Fetching AI/ML stories from Hacker News...")
    stories = fetch_stories()
    print(f"  Retrieved {len(stories)} raw stories")

    relevant = [s for s in stories if is_relevant(s)]
    print(f"  {len(relevant)} stories matched AI/ML/infra filter")

    # Sort by HN score descending, take top 5
    top5 = sorted(relevant, key=lambda s: s.get("points", 0), reverse=True)[:5]

    if not top5:
        print("No relevant stories found today. Skipping log update.", file=sys.stderr)
        sys.exit(0)

    section = build_log_section(top5)
    append_to_log(section)
    print("Done.")


if __name__ == "__main__":
    main()
