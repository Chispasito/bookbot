def get_book_word_count(book_string):
    book_split_array = book_string.split()
    word_count = len(book_split_array)
    return str(f"Found {word_count} total words")

def get_book_characters(book_string):
    book_string = book_string.lower()
    char_dict = {}
    quick_count = 0

    for c in book_string:
        if not c in char_dict:
            char_dict[c] = 1
        else:
            char_dict[c] += 1

    return char_dict

def sort_on(dict):
    return dict["nums"]

def sort_book_character_count(book_char_dict):
    sorted_char_list = []
    for char, num in book_char_dict.items():
        if char.isalpha():
            sorted_char_list.append({"char": char, "nums": num})

    sorted_char_list.sort(reverse = True, key = sort_on)
    return sorted_char_list