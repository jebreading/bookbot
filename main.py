from stats import get_num_words, get_chars_dict, convert_dict_to_list, sort_on, report
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(sys.argv)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    numwords = get_num_words(text)
    chars_dict = get_chars_dict(text)
    char_list = convert_dict_to_list(chars_dict)
    char_list.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {numwords} total words")
    print("--------- Character Count -------")
    report(char_list)
    print("============= END ===============")

def get_book_text(path):
    with open(path) as p:
        return p.read()
    
main()