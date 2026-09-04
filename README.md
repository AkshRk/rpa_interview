# RPA Python Code Review Exercise

This repository contains three small automation projects written by a junior RPA developer.
They "work" on the developer's machine but have not been reviewed.

## Your task

Review the code as if it were a pull request going to production.

For each set, produce a list of findings. For every finding state:

1. **File and line** where the problem is.
2. **What is wrong** (bug / correctness / security / performance / maintainability).
3. **Why it matters** in a real unattended RPA run.
4. **How you would fix it** (a short code sketch is enough).

You do not need to run the code. Do not fix the code unless asked.

---

## Set 1 — `set1_web_playwright_excel/`

Business requirement:

- Log in to the demo portal `https://quotes.toscrape.com/login`.
- Scrape **all quotes from pages 1 to 5** (quote text, author, tags).
- Write the results into a single Excel workbook, one row per quote, with a header row.
- The `Length` column must be a **number** so the business team can sort and sum it.
- The bot runs unattended on a Windows VM at 2 AM.

Entry point: `run_set1.py`

## Set 2 — `set2_doc_azure_openai/`

Business requirement:

- Read every PDF invoice in the input folder.
- Send the extracted text to Azure OpenAI and get back structured JSON with:
  `invoice_number`, `vendor_name`, `invoice_date`, `total`, `currency`.
- Write all results to a single JSON file.
- Report how many documents were processed and how many failed.
- A failure in one document must not stop the batch.

Entry point: `run_set2.py`

## Set 3 — `set3_api_excel/`

Business requirement:

- Read `transactions.xlsx` (columns: `TxnId`, `TxnDate`, `CountryCode`, `Currency`, `Amount`).
- `Amount` is in the transaction's **local currency**.
- Call a public exchange-rate API and convert every amount **into USD**.
- Add the country name for each `CountryCode`.
- Keep only transactions from the last 30 days.
- Write an enriched report and a summary file. **The source file must not be modified.**

Entry point: `run_set3.py`

---

## Environment

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

Sample input for Set 3 can be generated with `sample_data/create_sample_input.py`.
