from stats import num_words, count_characters, sorted_characters
import sys

def get_book_text (file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents



def main():
    if len(sys.argv) == 2:
        text = get_book_text(sys.argv[1])
        character_count = [(count_characters(text).items)]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words(text)} total words")
        print("------- Character Count ---------")
        for item in sorted_characters(text):
            print(f"{item["char"]}: {item["num"]}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
main()
