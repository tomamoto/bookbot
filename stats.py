def get_word_count(book_text):
    return len(book_text.split())

def get_character_count(book_text):
    character_count = {}
    for char_lower in book_text.lower():
        if char_lower in character_count:
            character_count[char_lower] += 1
        else:
            character_count[char_lower] = 1
    return character_count

def get_character_count_sorted(book_text):
    character_count = get_character_count(book_text)
    list_of_char_dicts = []
    for char, num in character_count.items():
        list_of_char_dicts.append({"char": char, "num": num})
    sorted_list_of_char_dicts = sorted(list_of_char_dicts, key=lambda x: x["num"], reverse=True)
    return sorted_list_of_char_dicts