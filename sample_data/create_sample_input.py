from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "transactions.xlsx"

ROWS = [
    ("0001", 3, "IN", "INR", 125000.50),
    ("0002", 10, "GB", "GBP", 2400.00),
    ("0003", 25, "DE", "EUR", 899.99),
    ("0004", 40, "US", "USD", 15000.00),
    ("0005", 61, "JP", "JPY", 350000.00),
    ("0006", 5, "IN", "INR", 990.25),
    ("0007", 18, "US", "USD", 12500.75),
    ("0008", 90, "GB", "GBP", 75.00),
]


def build():
    today = datetime.now()
    records = []
    for txn_id, age_days, country, currency, amount in ROWS:
        records.append(
            {
                "TxnId": txn_id,
                "TxnDate": (today - timedelta(days=age_days)).strftime("%d/%m/%Y"),
                "CountryCode": country,
                "Currency": currency,
                "Amount": amount,
            }
        )
    return pd.DataFrame(records)


if __name__ == "__main__":
    build().to_excel(OUT, index=False)
    print(f"wrote {OUT}")
