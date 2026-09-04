import os
import sys

AZURE_OPENAI_KEY = "9f3b1c7ae4d2411aa0c8e75d63b19f42"
AZURE_OPENAI_ENDPOINT = "https://ensemble-prod-openai.openai.azure.com/"
AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
AZURE_API_VERSION = "2023-05-15"

INPUT_DIR = "C:\temp\rpa_input"
OUTPUT_DIR = "C:\temp\rpa_output"

MAX_DOCUMENTS = 500

DEBUG = "false"

if DEBUG:
    print("config loaded from " + os.getcwd())
