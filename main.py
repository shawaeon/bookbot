BOOK_PATH = "books/frankenstein.txt"

def main():
    text = get_text(BOOK_PATH)
    count = word_count(text)
    print(f"Word in book: {count}")

def get_text(path):
    with open (path) as f:
        return f.read()

def word_count(txt):
    word_count = len(txt.split())
    return word_count


if __name__ == "__main__":
    main()