import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import streamlit as st
import json
# CONFIGURATION
SERVICE_ACCOUNT_FILE = 'credentials.json'  # <-- Your downloaded key file
SHEET_NAME = 'Research Log AI Marker'  # <-- Must match the sheet name exactly
SHEET_KEY = st.secrets["GOOGLE_SHEET_KEY"]

def sync_results_to_google_sheets():
    # Load credentials and authorize client
    scope = ['https://www.googleapis.com/auth/spreadsheets',]
    gdrive_creds = json.loads(st.secrets["G_SERVICE_JSON"])
    creds = Credentials.from_service_account_info(gdrive_creds, scopes=scope)
    gc = gspread.authorize(creds)

    # Open Google Sheet
    sheet = gc.open_by_key(SHEET_KEY).sheet1  # Use .worksheet("Sheet2") for other tabs

    # Load local results CSV
    df = pd.read_csv("results.csv")

    # Optional: clear old data before pushing new
    # sheet.clear()

    # Update all rows including headers
    sheet.update([df.columns.values.tolist()] + df.values.tolist())

    print("✅ Google Sheet updated successfully.")

# For standalone execution
if __name__ == "__main__":
    sync_results_to_google_sheets()
