from stats import count_words, count_characters, sort_dict, check_alphabet

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    file_path = "books/frankenstein.txt"
    frankenstein = get_book_text(file_path)
    word_count = count_words(frankenstein)
    character_count = count_characters(frankenstein)
    character_count = sort_dict(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count -----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in character_count:
        print(f"{char}: {character_count[char]}")
    print("============= END ===============")

main()
