import DatabaseStuff
import unittest
import sqlite3



class test_database(unittest.TestCase):
    def test_connection_to_db(self):
        # Open connection to database
        conn = sqlite3.connect('wufoo_db.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM entries')
        entries = cursor.fetchall()

        conn.close()

        return entries
    def test_get_database_entries(self):

        entries = DatabaseStuff.create_initial_entries()
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






