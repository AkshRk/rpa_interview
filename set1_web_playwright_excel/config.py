import os
import sys

PORTAL_USERNAME = "rpa.bot@company.com"
PORTAL_PASSWORD = "Passw0rd@2024"

BASE_URL = "https://quotes.toscrape.com"

OUTPUT_DIR = "C:\temp\rpa_output"

MAX_PAGES = 5

DEBUG = "false"

if DEBUG:
    print("config loaded from " + os.getcwd())
