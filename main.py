from stats import *

def main():
    file_path = 'books/frankenstein.txt'
    data = get_book_text(file_path)
    num_words = get_num_words(data)
    print(f"Found {num_words} total words")
    word_dict = get_word_dictionary(data)
    print(word_dict)

    
main()
