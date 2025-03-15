def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def convert_dict_to_list(char_counts):
    char_list = []
    for char, count in char_counts.items():
        char_dict = {"char": char, "num": count}
        char_list.append(char_dict)
    return char_list

def sort_on(item):
    return item["num"]

def report(char_list):
    for a in char_list:
        if a["char"].isalpha():
            print(f"{a["char"]}: {a["num"]}")
    pass