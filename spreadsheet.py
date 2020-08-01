import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']


creds = ServiceAccountCredentials.from_json_keyfile_name(
    'client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Sheffield wall data').worksheet('works')

pp = pprint.PrettyPrinter()
data = sheet.append_row([3,4])
pp.pprint(data)
