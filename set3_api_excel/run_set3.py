import pandas as pd

import transform
import config

INPUT_FILE = "C:\temp\rpa_input\transactions.xlsx"


def main():
    df = transform.load_transactions(INPUT_FILE)
    df = transform.enrich(df)
    df = transform.filter_recent(df, config.RECENT_DAYS)
    stats = transform.summarize(df)
    print(stats)

    large = transform.flag_large(df)
    if len(large) > 0:
        print("large transactions: " + str(large))

    df.to_excel(INPUT_FILE)
    summary = pd.DataFrame(stats)
    summary.to_excel(config.OUTPUT_DIR + "\summary.xlsx")
    print("report finished")


main()
