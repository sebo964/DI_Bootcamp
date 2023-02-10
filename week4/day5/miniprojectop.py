# Instructions

# The computer choose a random word and mark stars for each letter of each word.
# Then the player will guess a letter.
# If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
# If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
# The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
# The player can’t guess the same letter twice.


# Starter Code

# Here is a piece of code that will give you a random word.

#     import random

#     wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
#     word = random.choice(wordslist)

#     ### YOUR CODE STARTS FROM HERE ###

import random

# generate a random word

computer_word = random.choice(
    [
        "correction",
        "childish",
        "beach",
        "python",
        "assertive",
        "interference",
        "complete",
        "share",
        "credit",
        "rush",
        "south",
    ]
)

print(computer_word)

list_letter = [*(computer_word)]

# replace the letters with stars

list_stars = ["*" for letter in list_letter]

stars_for_print = " ".join(list_stars)

print(stars_for_print)

# game

for i in range(15):
    guess_letter = input("Guess a letter: ")

    if guess_letter in list_letter:
        for letter in list_letter:
            if letter == guess_letter:
                list_stars[list_letter.index(letter)] = letter
                list_letter[list_letter.index(letter)] = "*"
                stars_for_print = " ".join(list_stars)
                print(stars_for_print)

    else:
        print("You died")
        i += 1

    if "*" not in list_stars:
        print("You win!")
        break
