from googleapiclient.discovery import build
import pandas as pd

def list_user_sheets(credentials):
    """List available Google Sheets for the authenticated user."""
    service = build('drive', 'v3', credentials=credentials)
    results = service.files().list(
        q="mimeType='application/vnd.google-apps.spreadsheet'",
        fields="files(id, name)"
    ).execute()
    return results.get('files', [])

def read_google_sheet(credentials, spreadsheet_id, range_name):
    """Read data from the specified Google Sheet."""
    service = build('sheets', 'v4', credentials=credentials)
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=range_name
    ).execute()
    values = result.get('values', [])
    return pd.DataFrame(values[1:], columns=values[0]) if values else pd.DataFrame()
