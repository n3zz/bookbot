def get_book_words(filepath):
    with open(filepath) as f:
        book_text = f.read()
    
    text_list = book_text.split()
    no_of_words = len(text_list)

    return f"{no_of_words} words found in the document"