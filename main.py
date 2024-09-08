#bookbot code

def main():
    book_path = "books/frankenstein.txt"
    text = getText(book_path)
    word_number = wordCounter(text)
    print(f"This book has {word_number} words\n\n")
    char_dict = charCounter(text)
    char_dict = sortDict(char_dict)
    for key in char_dict:
        print(f"The letter {key} appears {char_dict[key]} times in the text\n")

#reading the book
def getText(path):
    with open(path) as f:
        return f.read()
    
#counting the number of words in the book
def wordCounter(text):
    words = text.split()
    return len(words)

#counting number of letter characters in the book
def charCounter(text):
    text = text.lower()
    char_dict = {}
    for c in text:
        if c.isalpha():
            if c not in char_dict:
                char_dict[c] = 1
            else:
                char_dict[c] += 1
    return char_dict

#sorts the char dict based on decreasing order of its values
def sortDict(char_dict):
    sorted_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict



main()