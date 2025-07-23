import sys

# the purpose of this program is to read a book
# it then counts the words and letters in the book
# then prints a report of all info

### subfunctions ###
from stats import *

def get_book(path):
    with open(path) as f:
        return f.read()


### MAIN ###
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book = get_book(path)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path}...")
    word_count = count_words(book)
    print(f"----------- Word Count ----------\nFound {word_count} total words")
    letter_count = count_letters(book)
    formated_count = format_counts(letter_count)
    print("--------- Character Count -------")
    for letter in formated_count:
        print(f"{letter["char"]}: {letter["num"]}")
    print("============= END ===============")

### entrypoint ###
if __name__ == "__main__":
    main()