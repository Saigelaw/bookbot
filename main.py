import sys
from stats import count_words, count_characters, get_sorted_char_counts


def get_book_text(book_path):
    with open(book_path) as file:
        file_contents = file.read()
    return file_contents


def print_report(text, sorted_chars):
    num_words = len(text.split())

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


def main():
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(book_path)
    char_counts = count_characters(book_text)

    sorted_char_list = get_sorted_char_counts(char_counts)
    print_report(book_text, sorted_char_list)


if __name__ == "__main__":
    main()
