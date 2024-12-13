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

def make_report(text,file):
    count = get_word_count(text)
    chars = number_of_characters(text)
    letters = [str(i) for i in "abcdefghijklmnopqrstuvwxyz"]
    print(f"--- Begin report of {file}---")
    print(f"{count} words were found in the document")

    for entry in chars:
        #print("entry")
        if entry in letters:
            print(f"The \'{entry}\' charcter was found \'{chars[entry]}\' times")

with open(path_to_file) as f:
    file_contents = f.read()

#print(get_word_count(file_contents))
#print(number_of_characters(file_contents))
make_report(file_contents,path_to_file)