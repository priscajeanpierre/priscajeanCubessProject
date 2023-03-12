import sqlite3
from typing import Tuple


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    cursor = db_connection.cursor()  # get ready to read/write data
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()  # make sure any changes get saved
    connection.close()


def create_entries_table(cursor: sqlite3.Cursor):
    create_statement = """CREATE TABLE IF NOT EXISTS WuFooData(
    entryID INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT,
    website TEXT,
    phone_number INTEGER,
    guest_speaker BOOLEAN,
    site_visit BOOLEAN,
    networking_event BOOLEAN,
    project_topic BOOLEAN,
    summer_23 BOOLEAN,
    fall_23 BOOLEAN,
    spring_23 BOOLEAN,
    subject_area TEXT NOT NULL,
    funding BOOLEAN,
    created_date TEXT,
    created_by TEXT
   );"""
    cursor.execute(create_statement)


def add_entries_to_db(cursor: sqlite3.Cursor, entries_data: list[dict]):
    # the insert or ignore syntax will insert if the primary key isn't in use or ignore if the primary key is in the DB
    insertStatement = """INSERT OR IGNORE INTO WuFooData (entryID, first_name, last_name, email, website,
     phone_number, guest_speaker, site_visit, networking_event, project_topic, summer_23, fall_23, spring_23,
      subject_area,funding,created_date,created_by) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
    for entry in entries_data:
        entry_values = list(entry.values())  # get the list of values from the dictionary
        entry_values[0] = int(entry_values[0])  # the EntryID is a string, but I want it to be a number
        entry_values = entry_values[:17]
        cursor.execute(insertStatement, entry_values)