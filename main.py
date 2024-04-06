def main():
    hardcoded_book = "books/frankenstein.txt"
    text = get_the_book(hardcoded_book)
    word_count = count_the_words(text)
    print(f"{word_count} words in this text")

def get_the_book(path):
    with open(path) as f:
        return f.read()



def count_the_words(text):
    words = text.split()
    return len(words) 




if __name__ == "__main__":
    main()
