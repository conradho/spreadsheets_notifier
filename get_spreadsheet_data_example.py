import gspread
from oauth2client.service_account import ServiceAccountCredentials


def get_sheet():
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://www.googleapis.com/auth/spreadsheets']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    return client.open("Automated Spreadsheet").sheet1


def notify(message):
    pass


def main():
    sheet = get_sheet()
    # only consider non-empty Ticker rows
    watchlist = (row for row in sheet.get_all_records() if row['Ticker'])

    for row in watchlist:
        if row['Current'] < row['Lower']:
            notify(f"{row['Ticker']} dropped below {row['Lower']}, current {row['Current']}. Buy for value?")
        if row['Current'] > row['Upper']:
            notify(f"{row['Ticker']} rose above {row['Upper']}, current {row['Current']}. Chase?")



if __name__ == '__main__':
    main()
