from stats import *

# file_path = "/home/presleyc95/workspace/github.com/presleyc95/bookbot/books/frankenstein.txt"


def main():
    book_path = "books/frankenstein.txt"
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


main()
