#bookbot code

def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    word_number = word_counter(text)
    print(f"This book has {word_number} words")

#reading the book
def get_text(path):
    with open(path) as f:
        return f.read()
    
#counting the number of words in the book
def word_counter(text):
    words = text.split()
    return len(words)


main()