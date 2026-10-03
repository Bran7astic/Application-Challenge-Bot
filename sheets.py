import json
import os
import gspread
from dotenv import load_dotenv

load_dotenv()

creds_json = os.getenv('GOOGLE_CREDS')
creds_dict = json.loads(creds_json)

gc = gspread.service_account_from_dict(creds_dict)
sh = gc.open("OCTOBER APPLICATION CHALLENGE")

count_cell = 'B4'

def get_application_counts():

    counts = {
        sheet.title : sheet.acell(count_cell).value
        for sheet in sh.worksheets()
    }

    return counts
