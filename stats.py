def num_words(file):
    num = 0
    with open(file) as f:
        content = f.read()
    palabras = content.split()
    for i in palabras:
        num += 1
    return num

def char_count(text):
    with open(text) as n:
        contenido = n.read()
    small = contenido.lower()
    char = {}
    for i in small:
        if i in char:
            char[i] += 1
        else:
            char[i] = 1
    return char

def pair(dict):
    listdict = []
    for m in dict:
        dict1 = {}
        dict1["letra"] = m
        dict1["cantidad"] = dict[m]
        listdict.append(dict1)
    return listdict

def sorton(pares):
    return pares["cantidad"]

def report(file):
    words = num_words(file)
    letras = pair(char_count(file))
    letras.sort(reverse=True, key=sorton)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for m in letras:
        character = m["letra"]
        cantidad = m["cantidad"]
        if character.isalpha() == True:
            print(f"{character}: {cantidad}")
        else : pass
    print("============= END ===============")