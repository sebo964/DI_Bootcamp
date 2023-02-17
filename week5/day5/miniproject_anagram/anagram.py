#  Now create another Python file, called anagrams.py. This will contain all the UI (user interface) functionality of your program, and will rely on AnagramChecker for the anagram-related logic.

# It should do the following:
# Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.

# If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
# Only a single word is allowed. If the user typed more than one word, show an error message. (Hint: how do we know how many words were typed?)
# Only alphabetic characters are allowed. No numbers or special characters.
# Whitespace should be removed from the start and end of the user’s input.

# Once your code has decided that the user’s input is valid, it should find out the following:
# All possible anagrams to the user’s word.
# Create an AnagramChecker instance and apply it to the steps created above.
# Display the information about the word in a user-friendly, nicely-formatted message such as:


# YOUR WORD :”MEAT”
# this is a valid English word.
# Anagrams for your word: mate, tame, team.

import anagram_checker


def menu():
    print("1. Check an anagram")
    print("2. Exit")
    choice = input("Please choose an option: ")
    if choice == "1":
        return choice
    else:
        exit(0)


def main():
    print("Welcome to the anagram checker!")

    word_list = (
        open("./week5/day5/miniproject_anagram/sowpods.txt", "r").read().splitlines()
    )
    choice = menu()
    while choice == "1":
        word = input("Please enter a word: ").lower().strip()
        checker = anagram_checker.AnagramChecker(word_list)
        if checker.is_valid_word(word):
            print(f"{word} is a valid word.")
            anagrams = checker.get_anagrams(word)
            print(f"Anagrams for your word: {anagrams}")
        else:
            print(f"{word} is not a valid word.")
        choice = menu()


main()
