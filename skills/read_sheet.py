"""
Read a Google Sheet tab and return all rows as JSON.

Usage:
    python skills/read_sheet.py <spreadsheet_id> <tab_name>

Example:
    python skills/read_sheet.py 1OYnAoSfx5AsYnwwDiBFfNlogwTla0jBRdwGjqaFLiJg "Rev-B"
    python skills/read_sheet.py 1OYnAoSfx5AsYnwwDiBFfNlogwTla0jBRdwGjqaFLiJg "Rem-B"

Requirements:
    pip install google-auth google-auth-httplib2 google-api-python-client
"""

import sys
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

CREDENTIALS_FILE = 'credentials/relaxedness-website-09b3a51b96a2.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']


def read_sheet(spreadsheet_id, tab_name):
    creds = service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=creds)
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=tab_name
    ).execute()
    rows = result.get('values', [])
    if not rows:
        print(json.dumps([]))
        return
    # Find first non-empty row to use as headers
    header_idx = 0
    for i, row in enumerate(rows):
        if any(cell.strip() for cell in row if cell):
            header_idx = i
            break
    headers = rows[header_idx]
    data = []
    for row in rows[header_idx + 1:]:
        padded = row + [''] * (len(headers) - len(row))
        data.append(dict(zip(headers, padded)))
    print(json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python skills/read_sheet.py <spreadsheet_id> <tab_name>")
        sys.exit(1)
    spreadsheet_id = sys.argv[1]
    tab_name = sys.argv[2]
    read_sheet(spreadsheet_id, tab_name)
