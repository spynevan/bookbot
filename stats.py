def get_book_text(file_path):
    with open(file_path) as file:
        file_content = file.read()
        return file_content

def get_num_words(string_input):
    string_list = string_input.split()
    return len(string_list)

def get_word_dictionary(string_input):
    return_object = dict()
    for character in string_input.lower():
        if character not in return_object:
            return_object[character] = 0
        return_object[character] += 1
    return return_object

