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
        if not character.isalpha():
            continue
        if character not in return_object:
            return_object[character] = 0
        return_object[character] += 1
    return return_object

def get_sorted_list(letter_dictionary):
    return_object = []
    for key in letter_dictionary:
        temp_dict = {"char": key, "num": letter_dictionary[key]}
        return_object.append(temp_dict)
    return_object.sort(key=lambda item: item["num"], reverse=True)
    return return_object

def print_report(file_path):
    book_text = get_book_text(file_path)
    num_words = get_num_words(book_text)
    word_dictionary = get_word_dictionary(book_text)
    sorted_list = get_sorted_list(word_dictionary)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dictionary in sorted_list:
        print(f"{dictionary['char']}: {dictionary['num']}")
    print("============= END ===============")




