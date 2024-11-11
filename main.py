BOOK_PATH = "books/frankenstein.txt"


def main():
    text = get_text(BOOK_PATH)
    w_count = word_count(text)
    c_count = character_count(text)
    print(f"Word in book: {w_count}\n")
    print("Characters in book:")
    for char in c_count:
        print(f"    {char}: {c_count[char]}")

def get_text(path):
    with open (path) as f:
        return f.read()

def word_count(txt):
    word_count = len(txt.split())
    return word_count

def character_count(txt):    
    characters = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0 
     }

    for char in txt:
       char = char.lower()
       if char in characters:
            characters[char] += 1
    return characters





if __name__ == "__main__":
    main()