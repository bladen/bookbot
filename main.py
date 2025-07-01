from stats import get_num_words, get_num_chars, sort_dict
import sys

def get_book_text(book):
    with open(book) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    words = get_book_text(sys.argv[1])
    word_count = get_num_words(words)
    charsnums = get_num_chars(words)
    sorted_dict = sort_dict(charsnums)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in sorted_dict:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["nums"]}")
    print("============= END ===============")

main()