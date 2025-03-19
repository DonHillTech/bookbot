from stats import get_num_words, get_character_counts, organize_dict, get_book_text
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    content = get_book_text(sys.argv[1])
    print("----------- Word Count ----------")
    num_words = get_num_words(content)
    print(f"Found {num_words} total words")
    character_count = get_character_counts(content)
    print("--------- Character Count -------")
    organize_dict(character_count)
    print("============= END ===============")

if __name__ == "__main__":
    main()