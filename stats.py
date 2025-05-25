def count_words(text):
    text_list = text.split()
    word_count = len(text_list)
    return word_count

def count_characters(book_string):
    characters = {}
    words = book_string.split()
    for word in words:
        word = word.lower()
        for i in range(len(word)):
            if word[i] in characters:
                characters[word[i]] += 1
            else:
                characters[word[i]] = 1
    return characters

def get_key(dict):
    for key in dict:
        return key

def sort_dict(dictionary):
    pass
