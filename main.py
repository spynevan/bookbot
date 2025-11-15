def get_book_text(file_path):
    with open(file_path) as file:
        file_content = file.read()
        return file_content

def get_num_of_words(string_input):
    string_list = string_input.split()
    return len(string_list)

def main():
    file_path = 'books/frankenstein.txt'
    data = get_book_text(file_path)
    num_words = get_num_of_words(data)
    print(f"Found {num_words} total words")
    
main()
