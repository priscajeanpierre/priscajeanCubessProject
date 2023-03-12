import DatabaseStuff
import getData



db_name = "cubesProject.sqlite"

def main():  # comment for force workflow
    json_response = getData.get_wufoo_data()
    entries_list = json_response["Entries"]
    conn, cursor = DatabaseStuff.open_db(db_name)
    DatabaseStuff.create_entries_table(cursor)
    DatabaseStuff.add_entries_to_db(cursor, entries_list)
    DatabaseStuff.close_db(conn)


if __name__ == "__main__":
    main()