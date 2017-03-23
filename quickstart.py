from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Quickstart'

def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?''version=v4')
    service = discovery.build('sheets', 'v4', http=http,discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1BNxDSG1P3oXIrDWssG7zR3du8sndWgEiBa8X-PcdOFc'

    #//////////////////////////////////////
    from fieldbook_py import fieldbook

    fbc = fieldbook.FieldbookClient('key-2','ttZYeH1e83BYY9a28aKR','https://api.fieldbook.com/v1/58d3689100aae203002b83f9')

    returned_rows = fbc.get_all_rows('contacts')
    values = []
    for val in returned_rows:
        row = [val["name"],val["company"],val["role"],val["phone"],val["notes"],val["email"]]
        values.append(row)
    #//////////////////////////////////////

    result2 = service.spreadsheets().values().append(spreadsheetId=spreadsheetId, range="Sheet1", insertDataOption="OVERWRITE",valueInputOption="USER_ENTERED", body={'values': values}, responseValueRenderOption="FORMULA").execute()
    print ("spreadsheetId : ",result2["spreadsheetId"])
    print ("updates updatedRange :",result2["updates"]["updatedRange"])
    print ("updates updatedCells :",result2["updates"]["updatedCells"])
    print ("updates updatedRows :",result2["updates"]["updatedRows"])
    print ("updates updatedColumns :",result2["updates"]["updatedColumns"])


if __name__ == '__main__':
    main()
