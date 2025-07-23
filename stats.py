def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    return_dic = {}
    words = text.split()
    for word in words:
        for letter in word:
            if letter.lower() not in return_dic:
                return_dic[letter.lower()] = 1
            else:
                return_dic[letter.lower()] += 1
    return return_dic

def sort_on(items):
    return items["num"]

def format_counts(letter_dict):
    return_list = []
    for letter, count in letter_dict.items():
        if letter.isalpha():
            letter_entry = {"char": letter, "num": count}
            return_list.append(letter_entry)
    return_list.sort(reverse=True, key=sort_on)
    return return_list
    
    