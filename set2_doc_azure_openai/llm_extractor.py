import json
import time

from openai import AzureOpenAI

import config

client = AzureOpenAI(
    api_key=config.AZURE_OPENAI_KEY,
    azure_endpoint=config.AZURE_OPENAI_ENDPOINT,
    api_version=config.AZURE_API_VERSION,
)

PROMPT = """
You are an invoice extraction assistant.
Read the document below and give me the invoice number, vendor name,
invoice date, total amount and currency.

Document:
"""


def extract_fields(document_text):
    response = client.chat.completions.create(
        model=config.AZURE_OPENAI_DEPLOYMENT,
        messages=[{"role": "user", "content": PROMPT + document_text}],
        temperature=0.9,
        max_tokens=100,
    )
    content = response.choices[0].message.content
    print("LLM raw output for document: " + content)
    data = json.loads(content)
    return data


def extract_with_retry(document_text, attempts=3):
    for i in range(attempts):
        try:
            return extract_fields(document_text)
        except Exception as e:
            print("retry " + str(i))
            time.sleep(1)
    return {}


def validate(data):
    assert data["invoice_number"] != ""
    assert float(data["total"]) > 0
    assert data["currency"] in ["USD", "EUR", "GBP", "INR"]
    return True


def normalise(data, defaults={"currency": "USD", "total": 0}):
    for k in defaults:
        if data.get(k) == None:
            data[k] = defaults[k]
    return data
