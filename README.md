# simple-search-engine

This repository contains a very simple search engine.

The app 
    - is taking a folder path from the terminal
    - search for all text files inside that folder
    - create inverted index for all tokens found in text files

Then user enter a query, and the app
    - is tokenizing the query
    - search for tokens in inverted index
    - return matched documents sorted by their matching score

Matching score is the percentage between length of query, and how many tokens from query have been found in file.
For example, if we have a query "Q" consists of 4 tokens, and 5 different files, the calculations will be as follows:
- If file #1 has 3 tokens, then its score will be 3/4*100
- If file #2 has 4 tokens, then its score will be 4/4*100
- If file #3 has 1 token, then its score will be 1/4*100
and so forth

To run the engine:
(from application root folder) pyhton SearchEngine.py <path_To_folder>

To run test cases:
(from application root folder) python -m unittest discover -v

