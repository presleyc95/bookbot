from stats import *

import sys

num_args = len(sys.argv)


def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_chars_dict(text)
    # sorted_letters = sort_chars_dict(num_letters)
    # print(sorted_letters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")
    sort_chars_dict(num_letters)
    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


if num_args < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()
