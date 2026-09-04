# Set 1 — Web Automation (Playwright) + Excel Reporting

A bot written by a junior RPA developer. It works on their machine and has never been reviewed.

## What it is supposed to do

1. Log in to the demo portal `https://quotes.toscrape.com/login`.
2. Scrape **all quotes from pages 1 to 5** — quote text, author, and tags.
3. Write the results to a timestamped Excel workbook, **one row per quote**, with a header row.
4. The `Length` column must be a **number**, so the business team can sort and total it.
5. Deduplicate against `master.xlsx` and append the new quotes to it.

The bot is scheduled to run **unattended at 2 AM on a Windows VM**, with nobody watching.

## Files

| File | Role |
|---|---|
| `config.py` | Credentials, paths, and run settings |
| `browser_bot.py` | Playwright login and scraping |
| `excel_report.py` | openpyxl workbook writing and deduplication |
| `run_set1.py` | Entry point |

## Setup

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
python run_set1.py
```

The demo site accepts any username and password.

## Your task

Review this code as if it were a pull request going to production.

For every finding, state:

1. **File and line number.**
2. **What is wrong** — bug, correctness, security, performance, or maintainability.
3. **Why it matters** for a bot that runs unattended with no human watching.
4. **How you would fix it** — a short code sketch is enough.

You do not need to run the code; reading it is enough. Do not fix anything unless asked.
Work through the code in whatever order you like, but be ready to tell us which finding
you consider the most serious and why.
