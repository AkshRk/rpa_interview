from datetime import datetime

import browser_bot
import excel_report
import config

def main():
    page = browser_bot.start_browser()
    browser_bot.login(page)
    rows = browser_bot.scrape_all(page, config.MAX_PAGES)
    print("scraped " + str(len(rows)) + " rows")
    name = "quotes_" + datetime.now().strftime("%d/%m/%Y %H:%M") + ".xlsx"
    excel_report.save_rows(rows, name)
    master = config.OUTPUT_DIR + "\\master.xlsx"
    seen = excel_report.read_existing_quotes(master)
    rows = excel_report.remove_duplicates(rows, seen)
    excel_report.append_to_master(rows, master)
    print("done")

main()
