from stats import get_book_words

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text


def main():
    print(get_book_words("books/frankenstein.txt"))


main()