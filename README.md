![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=180&section=header&text=AI%20Infrastructure%20Research%20Log&fontSize=34&fontColor=fff&animation=twinkling&fontAlignY=38&desc=Daily%20Automated%20Research%20%7C%20Hacker%20News%20%7C%20GitHub%20Actions&descAlignY=58)

<div align="center">

![Auto-Updated](https://img.shields.io/badge/Auto--Updated-Daily_08:00_UTC-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![Source](https://img.shields.io/badge/Source-Hacker_News_API-FF6600?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Maintained](https://img.shields.io/badge/Maintained-By_InFrontWebs-green?style=flat-square)

</div>

---

## What This Is

`AI-Infrastructure-Research-Log` is a living, machine-maintained research journal that tracks the daily frontier of AI/ML engineering — with a focus on inference infrastructure, GPU orchestration, generative model pipelines, open-source tooling, and production deployment patterns.

This is not a curated newsletter written by hand. Every morning at 08:00 UTC, a GitHub Actions workflow automatically queries the Hacker News Algolia API, filters for the highest-signal AI/ML stories, formats the top 5 results with title, URL, and engagement data, and appends them to [`logs.md`](logs.md) under a dated heading — then commits and pushes the update. The repository grows autonomously, one day at a time, without any human intervention.

**Maintained by [InFrontWebs](https://infrontwebs.com)** — an AI automation and cloud infrastructure firm based in Bangladesh.

---

## How It Works

```
GitHub Actions (cron: 08:00 UTC daily)
    │
    ▼
scripts/fetch_news.py
    │
    ├─ Queries Hacker News Algolia API
    │  https://hn.algolia.com/api/v1/search?query=AI&tags=story
    │
    ├─ Filters results by AI/ML keywords
    │  (LLM, inference, GPU, diffusion, transformer, RAG, etc.)
    │
    ├─ Selects top 5 by Hacker News score
    │
    ├─ Formats: ## YYYY-MM-DD heading + 5 entries
    │
    └─ Appends to logs.md → git commit → git push
```

The workflow runs on `schedule` (daily cron) and can also be triggered manually via `workflow_dispatch` from the GitHub Actions tab.

---

## How to Use This Log

**As a reader:**
- Browse [`logs.md`](logs.md) for daily AI engineering headlines with direct source links
- Use GitHub's search to find entries by topic: `GPU`, `LLM`, `inference`, `RunPod`, `LoRA`, etc.
- Watch this repo to get a GitHub notification each time it updates

**As an engineer building similar systems:**
- Fork this repo and customise the search query in `scripts/fetch_news.py`
- Change the filter keywords to match your domain (robotics, biotech, security, etc.)
- Adjust the cron schedule in `.github/workflows/daily-research.yml`
- The entire automation fits in ~60 lines of Python and one workflow YAML

**As a data source:**
- `logs.md` is plain Markdown — parseable as structured text
- Each day's section has a consistent `## YYYY-MM-DD` heading for easy parsing
- The HN URL and source URL are both included in each entry

---

## Repository Structure

```
AI-Infrastructure-Research-Log/
├── logs.md                          # Daily research log (auto-appended)
├── scripts/
│   └── fetch_news.py                # Python script: HN API → logs.md
├── .github/
│   └── workflows/
│       └── daily-research.yml       # GitHub Actions cron workflow
└── README.md
```

---

## Contributing

This log is maintained automatically, but human contributions are welcome:

- **Suggest a search query** — open an issue with your proposed HN search term
- **Report a duplicate or irrelevant entry** — open an issue with the date and entry
- **Improve the filter logic** — open a PR against `scripts/fetch_news.py`

---

## License

MIT — see repository root.

Built by [InFrontWebs](https://infrontwebs.com) · Bangladesh

![footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=80&section=footer)
