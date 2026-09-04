# Set 3 — Public REST API + Excel Automation

A bot written by a junior RPA developer. It works on their machine and has never been reviewed.

## What it is supposed to do

1. Read `transactions.xlsx`, which has the columns
   `TxnId`, `TxnDate`, `CountryCode`, `Currency`, `Amount`.
2. `Amount` is stated in the transaction's **local currency**.
   Convert every amount **into USD** using a public exchange-rate API.
3. Add the **country name** for each `CountryCode` using a public country API.
4. Keep only transactions from the **last 30 days**.
5. Print a summary — count, total USD, average USD — and flag large transactions.
6. Write an enriched report and a separate summary workbook.

Hard requirement: **the source file must not be modified.** Finance reconciles against it.

`TxnId` is a zero-padded reference (`0001`, `0002`, ...) and must stay exactly as it appears
in the source. The figures feed a financial report, so the numbers have to be right.

## Files

| File | Role |
|---|---|
| `config.py` | API endpoints, folder paths, thresholds |
| `api_client.py` | Exchange-rate and country lookups |
| `transform.py` | pandas load, enrich, filter, summarise |
| `run_set3.py` | Entry point |
| `sample_data/create_sample_input.py` | Generates a sample `transactions.xlsx` |

Both APIs are free and need no key.

## Setup

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python sample_data\create_sample_input.py
python run_set3.py
```

## Your task

Review this code as if it were a pull request going to production.

For every finding, state:

1. **File and line number.**
2. **What is wrong** — bug, correctness, data integrity, performance, or maintainability.
3. **Why it matters** for a bot producing a financial report unattended.
4. **How you would fix it** — a short code sketch is enough.

You do not need to run the code; reading it is enough. Do not fix anything unless asked.
Note that `sample_data/create_sample_input.py` is a test helper and is **out of scope** —
review the four files above it.
