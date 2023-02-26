import databaseStuff
import json
import sqlite3
import sys
import requests
from secrets import wufoo_key
from requests.auth import HTTPBasicAuth




# def connect_database():
#     db_connection = None
#     try:
#         db_connection = sqlite3.connect('wufoo_db.db')
#         db_cursor = db_connection.cursor()
#         print('Database connection successful')
#         return db_connection, db_cursor
#     except sqlite3.Error as db_error:
#         print(f'Database Error has occurred: {db_error}')
#
# def close_database(connection: sqlite3.Connection):
#     connection.commit()
#     connection.close()
#     print('\n\nDatabase connection closed.')
#
# def create_db(cursor: sqlite3.Cursor):
#     cursor.execute('''CREATE TABLE IF NOT EXISTS wufoo_db(
#     entry_id INTEGER PRIMARY KEY,
#     first_name TEXT NOT NULL,
#     last_name TEXT NOT NULL,
#     email TEXT NOT NULL,
#     website_link TEXT,
#     phone_number TEXT,
#     collab_opportunities TEXT,
#     project_topic TEXT,
#     collab_year TEXT);
#     ''')
#
#
# def create_initial_entries(cursor: sqlite3.Cursor):
#     entry_id = 1
#     first_name  = 'Michelle'
#     last_name = 'Jean'
#     email = 'mjean@gmail.com'
#     website_link = 'www.example.com'
#     phone_number = '555-555-5555'
#     collab_opportunities = 'Networking Event'
#     project_topic = 'Communications'
#     collab_year = '2023'
#     cursor.execute(f'''INSERT INTO wufoo_db(entry_id,
#     first_name, last_name, email,website_link,phone_number,
#     collab_opportunities, project_topic, collab_year)VALUES ({entry_id},
#     '{first_name}','{last_name}','{email}','{website_link}',
#     '{phone_number}','{collab_opportunities}','{project_topic}','{collab_year}')''')


def main():
    conn, cursor = databaseStuff.connect_database()
    print(type(conn))
    databaseStuff.create_db(conn)
    databaseStuff.create_initial_entries(cursor)
    databaseStuff.close_database(conn)
    databaseStuff.create_new_window(conn)
    databaseStuff.show_entry_data(cursor)


db_name = "cubesProject.sqlite"


# def main():
#     json_response = getData.get_wufoo_data()
#     entries_list = json_response["Entries"]
#     conn, cursor = open_db(db_name)
#     databaseStuff.create_entries_table(cursor)
#     databaseStuff.add_entries_to_db(cursor, entries_list)
#     close_db(conn)


if __name__ == "__main__":
    main()