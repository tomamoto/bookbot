from stats import get_word_count, get_character_count_sorted
import sys

def get_book_text(book_path):
    with open(book_path, 'r') as file:
        return file.read()

def main():

    #Check sys.argv for at least two arguments
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    

    book_text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {book_path}...')
    print('----------- Word Count ----------')
    print(f'Found {get_word_count(book_text)} total words')
    print('--------- Character Count -------')
    character_count_sorted = get_character_count_sorted(book_text)
    for char_dict in character_count_sorted:
        print(f'{char_dict["char"]}: {char_dict["num"]}')
    print('============= END ===============')

if __name__ == "__main__":
    main()
