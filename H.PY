from google.auth import exceptions
from google.oauth2 import service_account
import gspread

json_keyfile_path = 'C:\\Users\\rajpa\\OneDrive\\Desktop\\generateGoogleSheet\\gsheet-416106-1e88be0a738f.json'

try:
    credentials = service_account.Credentials.from_service_account_file(
        json_keyfile_path,
        scopes=['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    )
except exceptions.GoogleAuthError as e:
    print(f"Error loading credentials: {e}")
    raise

gc = gspread.authorize(credentials)
spreadsheet_key = '1h1nIgLCQYuTNmuhbuvJHFmXm8w8enm7_ILFFFzAbfko' 
try:
    spreadsheet = gc.open_by_key(spreadsheet_key)
except gspread.exceptions.SpreadsheetNotFound as e:
    print(f"Spreadsheet not found: {e}")
    raise
except Exception as e:
    print(f"An error occurred: {e}")
    raise

sheet = spreadsheet.sheet1
data = [
    ['Raj', 'Patil', 'rajpatil14052003@gmail.com'],
    ['Richa', 'Patil', 'richapatil0401@gmail.com']
]

try:
    sheet.append_rows(data)
    print(f'{len(data)} rows appended.')
except gspread.exceptions.APIError as e:
    print(f"API error: {e}")
    raise
