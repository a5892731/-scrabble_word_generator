def search_words_in_file(letters_list, file_address):
    file = open(file_address, 'r')
    list_of_possible_words = []

    for line in file:

        if word_in_line_check(line.upper().rstrip("\n"), letters_list) == True:
            try:
                list_of_possible_words += [line.rstrip("\n").upper()]
            except AttributeError:
                continue

    file.close()
    return list_of_possible_words

def word_in_line_check(line, letters_list):
    for letter in line:
        if letter in letters_list:
            status = True
            continue
        else:
            status = False
            break
    return status