from stats import get_num_words
from stats import get_book_text 

def main():
    file_path = 'books/frankenstein.txt'
    data = get_book_text(file_path)
    num_words = get_num_words(data)
    print(f"Found {num_words} total words")
    
main()
