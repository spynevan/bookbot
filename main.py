def get_book_text(file_path):
    with open(file_path) as file:
        file_content = file.read()
        return file_content

def main():

    file_path = 'books/frankenstein.txt'
    data = get_book_text(file_path)
    print(data)
    
main()
