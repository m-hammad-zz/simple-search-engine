import unittest
from app.SearchEngine import SearchEngine
import os

class SearchEngineTests(unittest.TestCase):

    def setUp(self):
        self.BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

    def test_full_match(self):
        search_engine = SearchEngine(self.BASE_DIR + '/test/data_set/')
        text_files_list = search_engine.load_path_files()
        inverted_index = search_engine.create_inverted_index(text_files_list)
        results = search_engine.search(text_files_list, inverted_index, 'data scientists')
        self.assertEqual("100.0", str(results[0][1]))

    def test_partial_match(self):
        search_engine = SearchEngine(self.BASE_DIR + '/test/data_set/')
        text_files_list = search_engine.load_path_files()
        inverted_index = search_engine.create_inverted_index(text_files_list)
        results = search_engine.search(text_files_list, inverted_index, 'testing data')
        self.assertEqual("50.0", str(results[0][1]))

    def test_non_match(self):
        search_engine = SearchEngine(self.BASE_DIR + '/test/data_set/')
        text_files_list = search_engine.load_path_files()
        inverted_index = search_engine.create_inverted_index(text_files_list)
        results = search_engine.search(text_files_list, inverted_index, 'ok')
        self.assertEqual("0", str(len(results)))


if __name__ == '__main__':
    unittest.main()