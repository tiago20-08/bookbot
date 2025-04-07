def num_words(file):
    num = 0
    with open(file) as f:
        content = f.read()
    palabras = content.split()
    for i in palabras:
        num += 1
    print(f"{num} words found in the document")

num_words("books/frankenstein.txt")