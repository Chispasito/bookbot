import sys
from stats import get_book_word_count
from stats import get_book_characters
from stats import sort_book_character_count

global_path = sys.argv

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
        book_string = get_book_text(global_path[1])
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
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