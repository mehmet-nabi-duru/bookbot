def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_letters(text):
    letter_count = {}
    
    alpa = "abcdefghijklmnopqrstuvwxyz"

    for letter in alpa:
        count = text.lower().count(letter)
        letter_count[letter] = count

    return letter_count

def print_report(letter_count):
    for letter, count in letter_count.items():
        print(f"The '{letter}' character was found {count} times")

    print("--- End report ---")
def main():
    book_text = "books/frankenstein.txt"
    text = get_book_text(book_text)

    letter_count = count_letters(text)

    print_report(letter_count)


if __name__ == "__main__":
    main()