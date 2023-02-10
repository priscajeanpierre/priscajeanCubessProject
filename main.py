import json
import sqlite3
import sys
import requests
from secrets import wufoo_key
from requests.auth import HTTPBasicAuth



# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# add comment to test workflow

url = "https://pjean12.wufoo.com/api/v3/forms/project-proposal-submission/entries.json"

def get_data() -> dict:

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

def connect_database():
    db_connection = None
    try:
        db_connection = sqlite3.connect('wufoo_db.db')
        db_cursor = db_connection.cursor()
        print('Database connection successful')
        return db_connection, db_cursor
    except sqlite3.Error as db_error:
        print(f'Database Error has occurred: {db_error}')

def close_database(connection: sqlite3.Connection):
    connection.commit()
    connection.close()
    print('\n\nDatabase connection closed.')

def create_db(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS wufoo_db(
    entry_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    website_link TEXT,
    phone_number TEXT,
    collab_opportunities TEXT,
    project_topic TEXT,
    collab_year TEXT);
    ''')


def create_initial_entries(cursor: sqlite3.Cursor):
    entry_id = 1
    first_name  = 'Michelle'
    last_name = 'Jean'
    email = 'mjean@gmail.com'
    website_link = 'www.example.com'
    phone_number = '555-555-5555'
    collab_opportunities = 'Networking Event'
    project_topic = 'Communications'
    collab_year = '2023'
    cursor.execute()


def main():
    conn, cursor = connect_database()
    print(type(conn))
    create_db(conn)
    close_database(conn)



if __name__ == '__main__':
    main()