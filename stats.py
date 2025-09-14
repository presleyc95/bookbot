

def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        alpha = c.isalpha()
        if lowered in chars and alpha:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_chars_dict(text):
    new_dict = {}
    for k in text:
        new_dict[text[k]] = k
    sort_text = sorted(new_dict, key=None, reverse=True)
    for i in sort_text:
        key = new_dict[i]
        value = i
        print(f"{key}: {value}")
