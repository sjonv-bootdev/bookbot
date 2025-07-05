def get_num_of_words(string_o_words):
    words = string_o_words.split()
    return len(words)

def count_characters(text: str) -> dict:
    text = text.lower()
    char_counts = {}

    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1

    return char_counts

def sort_alpha_char_counts(char_dict):
    items = [{"char": char, "num": count} for char, count in char_dict.items() if char.isalpha()]
    items.sort(key=lambda x: x["num"], reverse=True)
    return items

