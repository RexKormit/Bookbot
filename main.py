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
    letters = [str(i) for i in "abcdefghijklmnopqrstuvwxyz"] #List comprehension to create list of letters
    print(f"--- Begin report of {file}---")
    print(f"{count} words were found in the document")

    for entry in chars:
        if entry in letters:
            print(f"The \'{entry}\' charcter was found \'{chars[entry]}\' times")

with open(path_to_file) as f:
    #Opens the selected file into f variable then puts the contents into file_contents
    file_contents = f.read()

make_report(file_contents,path_to_file)