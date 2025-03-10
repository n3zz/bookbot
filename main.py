from stats import get_book_words
from stats import dictionary_maker
from stats import process_list
from stats import sort_on
from stats import filtering_list
from stats import display_list

import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
        

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    word_count = get_book_words(filepath)
    book_text = get_book_text(filepath)
    print(f"Found {word_count} total words")
    # print(dictionary_maker(book_text))
    book_dict = dictionary_maker(book_text)
    processed_list = process_list(book_dict)
    sorted_list = sort_on(processed_list)
    
    display_list(sorted_list)

main()