import sys

import requests

from secrets import wufoo_key
from requests.auth import HTTPBasicAuth

base_url = 'https://pjean12.wufoo.com/api/v3/'
username = 'username'
password = 'ABC123'

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

wufootxt = open('wufoo.txt')
wufootxtt = open('wufoo.txt')


def get_data() -> dict:
    url = "https://pjean12.wufoo.com/api/v3/forms/project-proposal-submission/entries.json"
    response = requests.get(url, auth=HTTPBasicAuth(wufoo_key, 'pass'))

    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
    sys.exit(-1)

    jsonresponse = response.json()
    return jsonresponse  # json response will be either a dictionary or a list of dictionaries
    # each dictionary represents a json object


def data_entries():
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {wufoo_key}')  # Press ⌘F8 to toggle the breakpoint.

def get_form():



if __name__ == '__main__':
    print(main)