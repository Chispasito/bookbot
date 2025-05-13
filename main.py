import sys
from stats import get_book_word_count
from stats import get_book_characters
from stats import sort_book_character_count

def get_book_text(filepath):
    file_string = ""
    if filepath is None or filepath == "":
        raise Exception("No filepath")
    
    with open(filepath) as f:
        file_string = f.read()

    return file_string

def main():
    book_string = ""
    try:
        book_string = get_book_text("books/frankenstein.txt")
    except Exception as e:
        print("Couldn't find a book")
    
    print("============ BOOKBOT ============ " 
        + "\nAnalyzing book found at books/frankenstein.txt..."
        + "\n----------- Word Count ----------")
    print(get_book_word_count(book_string))
    
    book_char_dict = get_book_characters(book_string)
    # print(book_char_dict)

    print("--------- Character Count -------")
    sorted_char_list = sort_book_character_count(book_char_dict)
    for item in sorted_char_list:
        print(f"{item["char"]}: {item["nums"]}")

    print("============= END ===============")


main()