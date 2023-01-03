from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import googleapiclient.errors

'''This script outlined by chatgpt fails to read a Google Sheet and print the data to the console, because chatGPT is not that great yet as of 2022-12-20;)'''

creds = Credentials.from_client_secrets_file(
    'client_secret.json', ['https://www.googleapis.com/auth/spreadsheets.readonly']
)

service = build('sheets', 'v4', credentials=creds)

# Replace the file_id value with the actual file ID of the Google Sheets file
file_id = '1VwSFFilTROPRm0xtEz-P0lCKIdud6IwXyl4ubkrWI2g'

try:
    # Call the Sheets API to download the file
    sheet = service.spreadsheets().get(spreadsheetId=file_id).execute()

    # Print the file data
    print(sheet)

except HttpError as error:
    print(f'An error occurred: {error}')
    sheet = None