import os
import sys

EXCHANGE_API_BASE = "https://open.er-api.com/v6/latest/"
COUNTRY_API_BASE = "https://restcountries.com/v3.1/alpha/"

INPUT_DIR = "C:\temp\rpa_input"
OUTPUT_DIR = "C:\temp\rpa_output"

RECENT_DAYS = 30
LARGE_TXN_THRESHOLD = 10000

DEBUG = "false"

if DEBUG:
    print("config loaded from " + os.getcwd())
