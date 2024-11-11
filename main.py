def main():

    with open ("books/frankenstein.txt") as f:
        print(word_count(f.read()))

def word_count(txt):
    word_count = len(txt.split())
    return word_count


if __name__ == "__main__":
    main()