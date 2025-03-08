def get_book_words(filepath):
    with open(filepath) as f:
        book_text = f.read()
    text_list = book_text.split()
    no_of_words = len(text_list)

    return no_of_words

def dictionary_maker(booktext):
    char_dict = {}
    
    for char in booktext:
        lowered_char = char.lower()
        if lowered_char in char_dict:
            char_dict[lowered_char] += 1
        else:
            char_dict[lowered_char] = 1
    return char_dict
