from stats import word_counter, char_counter, sort_dict
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def print_report(book_path, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item[0].isalpha():
            print(f"{item[0]}: {item[1]}")
    print("============= END ===============")

    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = word_counter(text)
    num_chars = char_counter(text)
    sorted_chars = sort_dict(num_chars)
    print_report(book_path, num_words, sorted_chars)


main()