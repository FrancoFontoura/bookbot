#bookbot code

def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)

#reading the book
def get_text(path):
    with open(path) as f:
        return f.read()


main()