import databaseStuff
import unittest
import sqlite3


# Define the unit test
class test_database(unittest.TestCase):
    def test_connection_to_db(self):
        # Open connection to database
        conn = sqlite3.connect('wufoo_db.db')
        cursor = conn.cursor()

        # Execute a query to retrieve the entries from the database
        cursor.execute('SELECT * FROM entries')
        entries = cursor.fetchall()

        # Close the connection to the database
        conn.close()

        # Return the entries as a list
        return entries
    def test_get_database_entries(self):

        entries = databaseStuff.create_initial_entries()
        self.assertEqual(len(entries), 2)
        self.assertEqual(entries[0], (1, 'Entry 1', 10.0))
        self.assertEqual(entries[1], (2, 'Entry 2', 20.0))

    def test_close_db_connection(self):
        conn = sqlite3.connect('wufoo_db.db')
        cursor = conn.cursor()
        conn.commit()
        conn.close()

if __name__ == '__main__':
    unittest.main()






