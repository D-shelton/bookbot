def count_the_words(text):
    words = text.split()
    wordcount = 0
    for word in words:
        wordcount +=1
    print(wordcount)    



def main():
    with open("books/frankenstein.txt") as frankenstein:
        text = frankenstein.read()
        count_the_words(text)


if __name__ == "__main__":
    main()
