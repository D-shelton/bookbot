def main():
    hardcoded_book = "books/frankenstein.txt"
    text = get_the_book(hardcoded_book)
    word_count = count_the_words(text)
    raw_letters = count_the_letters(text)
    letter_count = organize_letters(raw_letters)
    print(f"{word_count} words in this text, and the letters used break down as: {letter_count} ")


#### sub functions below in call order####


def get_the_book(path):
    with open(path) as f:
        return f.read()

def count_the_words(text):
    words = text.split()
    return len(words) 

def count_the_letters(text):
    char_totals = {}
    for char in text:
        char = char.lower()
        if char in char_totals:
            char_totals[char] +=1
        else:
            char_totals[char] = 1
    return char_totals


### below here is all for the organize_letters function, organize in the future ###

def organize_letters(char_totals):
    char_list = [{'char': char, 'num': count} for char, count in char_totals.items()]
    char_list.sort(reverse=True, key=lambda char_dict:char_dict['num'])
    return char_list


def sort_on(char_totals):
    return char_totals["num"]

def organize_dictionaries(char_totals):
    char_totals.sort(reverse=True, key=sort_on)
    return char_totals
    

if __name__ == "__main__":
    main()
