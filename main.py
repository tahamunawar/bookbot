import sys
from stats import get_num_words, get_character_count, get_sorted_dict

book_location = ""

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_location = sys.argv[1]

    with open(book_location) as f:
        file_contents = f.read()
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_location}...")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(file_contents)} total words")
        print("--------- Character Count -------")
        dic = get_character_count(file_contents)
        sorted_dict = get_sorted_dict(dic)
        for key in sorted_dict:
            if key.isalpha():
                print(f"{key}: {sorted_dict[key]}")

main()
