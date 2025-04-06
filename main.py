from stats import get_num_words
from stats import get_characters
from stats import sort_dictionary
import sys 

def get_book_path():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit with an error if no argument is provided
    return sys.argv[1]  # Return the second argument (the book path)

#This function takes the filepath of the book and converts it into a string
def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents



#Main function
def main():
    book_path = get_book_path()
    filetext = get_book_text(book_path)
    num_characters = sort_dictionary(filetext)
    num_words = get_num_words(filetext)
    print(f"{num_words} words found in the document")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in num_characters:
        if char['char'].isalpha() == True:
            print(f"{char['char']}: {char['count']}")
    print("============= END ===============")

main()