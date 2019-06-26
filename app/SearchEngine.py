from os import listdir
from os.path import isfile, join
import sys
import operator
from collections import defaultdict
import re


class SearchEngine(object):

    def __init__(self, folder_path):
        self.folder_path = folder_path


    # Create a list of all text files names
    def load_path_files(self):
        text_files = [join(self.folder_path, f) for f in listdir(self.folder_path) if isfile(join(self.folder_path, f)) and '.txt' in f and '~' not in f]
        return text_files


    # Create inverted index of all text tokens found in text_files
    def create_inverted_index(self, text_files_list):
        text_inverted_index = defaultdict(set)
        for file_idx, file_name in enumerate(text_files_list):
            with open(file_name, 'r') as file_reader:
                for line in file_reader:
                    line_words = [s for s in re.split("\W", line.lower()) if s != '']
                    for word in line_words:
                        text_inverted_index[word].add(file_idx)

        return text_inverted_index

    # Searching in inverted index based on user query
    def search(self, text_files_list, text_inverted_index, query):

        # Tokenize input string, applying the same preprocessing as inverted index
        tokenized_query = [s for s in re.split("\W", query.lower()) if s != '']
        all_files_list = []
        for term in tokenized_query:
            list_files = text_inverted_index[term]
            all_files_list.extend(list_files)

        # Get unique values of matched docs idx
        all_files_set = set(all_files_list)
        final_list = []
        # Construct final matched files with their scores
        for item in all_files_set:
            score = float(all_files_list.count(item))/float(len(tokenized_query))*100
            final_list.append((text_files_list[item], round(score, 2)))

        # Sorting matched files according to matching score
        final_list = sorted(final_list, key=operator.itemgetter(1), reverse=True)

        return final_list


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 1:
        print 'No path passed to application'
        exit(1)

    if len(args) > 2:
        print 'Application accepts only one argument'
        exit(1)

    search_engine = SearchEngine(args[1])
    text_files_list = search_engine.load_path_files()
    inverted_index = search_engine.create_inverted_index(text_files_list)

    while True:
        input_query = str(raw_input('search (:exit to close the engine) > '))
        if input_query == ':exit':
            exit(0)
        results = search_engine.search(text_files_list, inverted_index, input_query)

        # Printing results
        if len(results) == 0:
            print 'no matches found'
        else:
            for match_file in results[:10]:
                print match_file[0], ' --> ', match_file[1], '%'
