import json
import sys

import requests

from secrets import wufoo_key
from requests.auth import HTTPBasicAuth



# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# add comment to test workflow



def get_data() -> dict:
    url = "https://pjean12.wufoo.com/api/v3/forms/project-proposal-submission/entries.json"
    response = requests.get(url, auth=HTTPBasicAuth(wufoo_key, 'pass'))

    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
    sys.exit(-1)

    jsonresponse = response.json()
    return jsonresponse  # json response will be either a dictionary or a list of dictionaries
    # each dictionary represents a json object


def main():
    data = get_data()
    data1 = data['Entries']
    file_to_save = open("output.txt", 'w')
    save_data(data1, save_file=file_to_save)


def save_data(data_to_save: list, save_file=None):
    for entry in data_to_save:
        for key, value in entry.items():
            print(f"{key}: {value}", file=save_file)
        # now print the spacer
        print("+++++++++++++++++++++++++++++++++++++++++++++\n_______________________________________________",
              file=save_file)

if __name__ == '__main__':
    main()