from stats import get_book_words
from stats import dictionary_maker

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
        

def main():
    word_count = get_book_words("books/frankenstein.txt")
    book_text = get_book_text("books/frankenstein.txt")
    print(f"{word_count} words found in the document")
    print(dictionary_maker(book_text))

main()