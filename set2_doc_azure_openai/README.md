# Set 2 — Document Processing with Azure OpenAI

A bot written by a junior RPA developer. It works on their machine and has never been reviewed.

## What it is supposed to do

1. Read **every PDF invoice** dropped into the input folder.
2. Extract the text and send it to an Azure OpenAI deployment.
3. Get back structured JSON for each invoice with these fields:
   `invoice_number`, `vendor_name`, `invoice_date`, `total`, `currency`.
4. Validate the extracted fields.
5. Write all results to a single JSON file.
6. Report how many documents were **processed** and how many **failed**.

Hard requirement: **a failure on one document must not stop the batch.**
The remaining invoices must still be processed.

The bot is scheduled to run **unattended overnight on a Windows VM**, against a
paid Azure OpenAI deployment with a shared token quota.

## Files

| File | Role |
|---|---|
| `config.py` | Azure connection settings and folder paths |
| `pdf_reader.py` | Lists input files and extracts text with `pypdf` |
| `llm_extractor.py` | Calls Azure OpenAI, parses and validates the response |
| `run_set2.py` | Entry point, batch loop, counters, output file |

## Setup

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python run_set2.py
```

**Note:** the Azure key in `config.py` is not a working key, so this set cannot actually
be executed. Review it by reading only.

## Your task

Review this code as if it were a pull request going to production.

For every finding, state:

1. **File and line number.**
2. **What is wrong** — bug, correctness, security, prompt design, cost, or maintainability.
3. **Why it matters** for a bot that runs unattended against a paid, rate-limited API.
4. **How you would fix it** — a short code sketch is enough.

You do not need to run the code; reading it is enough. Do not fix anything unless asked.
Pay particular attention to whether the code actually satisfies the requirement that
one bad document must not stop the batch.
