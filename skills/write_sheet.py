"""
Append rows to a Google Sheet tab.

Usage:
    python skills/write_sheet.py <spreadsheet_id> <tab_name> <json_rows>

Where json_rows is a JSON array of arrays (each inner array = one row, each element = one cell).

Example:
    python skills/write_sheet.py 1OYnAoSfx5AsYnwwDiBFfNlogwTla0jBRdwGjqaFLiJg "Rewire" '[["8 Mar","Shiva","Did Sujith complete his Rem-B today?","","Open"]]'

Requirements:
    pip install google-auth google-auth-httplib2 google-api-python-client
"""

import sys
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

CREDENTIALS_FILE = 'credentials/relaxedness-website-09b3a51b96a2.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


def append_rows(spreadsheet_id, tab_name, rows):
    creds = service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=creds)
    body = {'values': rows}
    result = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=tab_name,
        valueInputOption='RAW',
        insertDataOption='INSERT_ROWS',
        body=body
    ).execute()
    updated_range = result.get('updates', {}).get('updatedRange', 'unknown')
    rows_added = result.get('updates', {}).get('updatedRows', 0)
    print(f"Appended {rows_added} row(s) to {updated_range}")


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python skills/write_sheet.py <spreadsheet_id> <tab_name> <json_rows>")
        sys.exit(1)
    spreadsheet_id = sys.argv[1]
    tab_name = sys.argv[2]
    rows = json.loads(sys.argv[3])
    append_rows(spreadsheet_id, tab_name, rows)
