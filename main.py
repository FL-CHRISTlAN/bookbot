def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    report(book_path,text)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def get_leters(text):
    dic_char = {}
    characters = text.lower()
    for char in characters:
        if char in dic_char:
            dic_char[char] += 1
        else:
            dic_char[char] = 1
    return dic_char

def report(path, text):
    print(f"--- Begin report of {path} ---")
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document\n")
    leters = get_leters(text)
    for leter in leters:
        if leter.isalpha():
            print(f"The '{leter}' was found {leters[leter]} times.")
    print("--- End report ---")



main()
    
