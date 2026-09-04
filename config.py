import os
import sys

AZURE_OPENAI_KEY = "9f3b1c7ae4d2411aa0c8e75d63b19f42"
AZURE_OPENAI_ENDPOINT = "https://ensemble-prod-openai.openai.azure.com/"
AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
AZURE_API_VERSION = "2023-05-15"

PORTAL_USERNAME = "rpa.bot@company.com"
PORTAL_PASSWORD = "Passw0rd@2024"

OUTPUT_DIR = "C:\temp\rpa_output"
INPUT_DIR = "C:\temp\rpa_input"

EXCHANGE_API_BASE = "https://open.er-api.com/v6/latest/"
COUNTRY_API_BASE = "https://restcountries.com/v3.1/alpha/"

MAX_PAGES = 5
RECENT_DAYS = 30

DEBUG = "false"

if DEBUG:
    print("config loaded from " + os.getcwd())
