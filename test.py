import unittest



class MyTestCase(unittest.TestCase):
    def test_show_database_entries(self):
        # Call the function to show the database entries
        entries = show_database_entries()

        # Verify that the correct entries are returned
        expected_entries = [(1, 'John'), (2, 'Jane')]
        self.assertEqual(entries, expected_entries)







