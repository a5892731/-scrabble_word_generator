def list_wards_filter(input_letters, list_of_potential_words):
    list_of_words = list_of_potential_words
    letters_dictionary = {}
    delete_list = []

    for letter in input_letters:
        letters_dictionary[letter] = input_letters.count(letter)

    for word in list_of_potential_words:
        for key in letters_dictionary:

            if word.count(key) > letters_dictionary[key]:
                delete_list.append(word)
                break

    for word in delete_list:
        list_of_words.remove(word)

    return list_of_words