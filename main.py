from stats import get_num_of_words
from stats import count_characters 
from stats import sort_alpha_char_counts
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    lots_of_words = get_book_text(sys.argv[1])
    num_of_words = get_num_of_words(lots_of_words)
    char_count = count_characters(lots_of_words)
    sorted_alpha = sort_alpha_char_counts(char_count)

    #print(f"{num_of_words} words found in the document")
    #print(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for item in sorted_alpha:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()