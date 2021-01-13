'''
author a5892731
This is a word generator for scrabble
'''


from search_words_in_file import search_words_in_file
from list_wards_filter import list_wards_filter


# >>>>>>>>>>>>>>>>>>>> main <<<<<<<<<<<<<<<<<<<<<<<<


while True:
    list_of_words = ()
    input_letters = ""
    input_letters_list = []
    list_of_potential_words = []

    input_letters = input("Give me your letters: ")
    input_letters = input_letters.upper()

    list_of_potential_words = search_words_in_file(input_letters, "DICT_PL.txt")   # for polish
    list_of_potential_words = search_words_in_file(input_letters, "DICT_ENG.txt")  # for english


    list_of_words = list_wards_filter(input_letters, list_of_potential_words)

    list_of_words.sort(key = len)


    [print(word) for word in list_of_words]

    do_it_again = input("\n>>> do you want to play again? Y/N: ")
    if do_it_again == "y" or do_it_again == "Y":
        continue
    else:
        print("exit")
        break

