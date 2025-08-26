# Splits up the text into words and counts them
def num_words(text):
    words = text.split()
    return len(words)

# Counts the occurrences of each character in the text
def count_characters(text):
    text_lower = text.lower()
    char_count = {}
    for c in text_lower:
        if c not in char_count.keys():
            char_count[c] = 1
        else:
            char_count[c] += 1
    return char_count

def sort_on(item):
    return item["num"]

def sorted_characters(text):
    char_count = count_characters(text)

    list_chars = []
    for char in char_count:
        if char.isalpha():
            sorted_chars= {}
            sorted_chars["char"] = char
            sorted_chars["num"] = char_count[char]
            list_chars.append(sorted_chars)
    list_chars.sort(reverse=True, key=sort_on)
    return list_chars
