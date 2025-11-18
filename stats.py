# function to count words in a book
def count_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words


# fuction to return number of times a eacg character appears in the book
def count_characters(book_text):
    char_count = {}
    for char in book_text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_on_num(d):
    """
    Helper function for list.sort() method.
    Returns the value associated with the 'num' key.
    """
    return d["num"]


def get_sorted_char_counts(char_counts):
    char_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})

    char_list.sort(key=sort_on_num, reverse=True)

    return char_list
