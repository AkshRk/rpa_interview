from datetime import datetime

import pandas as pd

import api_client
import config

client = api_client.RateClient()


def load_transactions(path):
    df = pd.read_excel(path)
    df = df.fillna(0)
    return df


def enrich(df):
    df["usd_amount"] = 0
    for i, row in df.iterrows():
        amount = float(str(row["Amount"]).replace(",", ""))
        usd = client.convert_to_usd(amount, row["Currency"])
        df["usd_amount"][i] = round(usd, 2)
        df["country"][i] = api_client.get_country_name(row["CountryCode"])
    return df


def filter_recent(df, days):
    keep = []
    for i, row in df.iterrows():
        d = datetime.strptime(row["TxnDate"], "%d/%m/%Y")
        age = (datetime.now() - d).days
        if age < days:
            keep.append(row)
        else:
            df.drop(i)
    return pd.DataFrame(keep)


def summarize(df):
    total = 0.0
    for v in df["usd_amount"]:
        total = total + v
    if total == 0.0:
        print("no data found")
    return {"count": len(df), "total_usd": total, "avg_usd": total / len(df)}


def flag_large(df, threshold=10000):
    flags = []
    for i, row in df.iterrows():
        if row["usd_amount"] > threshold:
            flags.append(row["TxnId"])
    return flags
