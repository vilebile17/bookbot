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

def check_alphabet(dictionary):
    new_dict = {}
    for character in dictionary:
        if str(character).isalpha():
            new_dict[character] = dictionary[character]
    return new_dict


def sort_dict(dictionary):
    # takes the dictionary and sorts in from greatest to least
    # this was built completely from scratch without using the recommendations on boot.dev :)
    exclusions = []
    new_dict = {}
    for character in dictionary:
        max_so_far = {"":float("-inf")}
        for char in dictionary:
            key = get_key(max_so_far)
            if dictionary[char] > max_so_far[key] and (char not in exclusions) and str(char) != "":
                max_so_far = {char: dictionary[char]}

        exclusions.append(get_key(max_so_far))
        new_dict[get_key(max_so_far)] = max_so_far[get_key(max_so_far)]
    
    new_dict = check_alphabet(new_dict)
    return new_dict
        

    

