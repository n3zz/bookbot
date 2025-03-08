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

def process_list(raw_dict):
    char_list = []
    for char, count in raw_dict.items():
        char_list.append({"char": char, "count": count})
    return char_list

def sort_on(list):
    new_list = sorted(list, key=lambda item: item["count"], reverse=True)
    return new_list

def filtering_list(sorted_list):
    filtered_list = []
    for list in sorted_list:
        if list["char"].isalpha() == True:
            filtered_list.append(list)
        else:
            pass
    return filtered_list

def display_list(final_list):
    for item in final_list:
        print(f"{item["char"]}: {item["count"]}")