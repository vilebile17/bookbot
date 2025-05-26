from stats import count_words
from stats import count_characters
from stats import sort_dict
from stats import check_alphabet

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    dictionary = get_book_text("books/frankenstein.txt")
    frankenstein = get_book_text("books/frankenstein.txt")
    word_count = count_words(frankenstein)
    character_count = count_characters(frankenstein)
    print(f"{word_count} words found in the document")
    character_count = sort_dict(character_count)
    print(character_count)


main()
