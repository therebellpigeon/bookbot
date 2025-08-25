import sys
from stats import word_count
from stats import char_count
from stats import sort_char_count




def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    relative_path = sys.argv[1]
    booktxt = get_book_text(relative_path)
    count = word_count(booktxt)
    char_cnt = char_count(booktxt)
    sorted = sort_char_count(char_count(booktxt))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {relative_path}:")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("-------- Character Count --------")
    for char_dict in sorted:
        char = char_dict["char"]
        if char.isalpha():  # Check if THIS character is alphabetical
            count = char_dict["num"]
            print(f"{char}: {count}")
    print("============= END ===============")

main()

