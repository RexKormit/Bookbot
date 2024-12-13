path_to_file = "books/frankenstien.txt"

def get_word_count(text):
    return len(text.split())

def number_of_characters(text):
    text = text.lower()
    character_dict = {}
    for letter in text:
        if letter in character_dict:
            character_dict[letter] += 1
        else:
            character_dict[letter] = 1
    return character_dict

with open(path_to_file) as f:
    file_contents = f.read()

#print(get_word_count(file_contents))
print(number_of_characters(file_contents))