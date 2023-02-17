# rock paper scissors game

import random


def validate_userinput(user):
    while user.lower() not in options:
        print("Invalid input")
        user = input("Choose rock, paper or scissors: ")
        user = user.strip()
        user = user.lower()
    return True


def game(user, computer_selection):
    global count_user_wins
    global count_computer_wins
    global count_ties
    global count_total_games
    if user == computer_selection:
        print("It's a tie")
        count_ties = +1
    elif user == "rock":
        if computer_selection == "paper":
            print("You lose")
            count_computer_wins += 1
        else:
            print("You win")
            count_user_wins += 1
    elif user == "paper":
        if computer_selection == "scissors":
            print("You lose")
            count_computer_wins += 1
        else:
            print("You win")
            count_user_wins += 1
    elif user == "scissors":
        if computer_selection == "rock":
            print("You lose")
            count_computer_wins += 1
        else:
            print("You win")
            count_user_wins += 1
    else:
        print("Invalid input")
    count_total_games += 1


options = ["rock", "paper", "scissors"]

user = str(input("Choose rock, paper or scissors: ")).lower()

computer_selection = random.choice(options)
count_user_wins = 0
count_computer_wins = 0
count_ties = 0
count_total_games = 0

game(user, computer_selection)

user_play_again = str(input("Do you want to play again? (y/n): "))

if user_play_again == "y":
    while user_play_again == "y":
        user = str(input("Choose rock, paper or scissors: ")).lower()
        computer_selection = random.choice(options)
        game(user, computer_selection)
        user_play_again = str(input("Do you want to play again? (y/n): "))
        if user_play_again == "n":
            break
print(
    f"Computer wins {count_computer_wins}, User wins {count_user_wins}, Count ties {count_ties}, Count total games {count_total_games}"
)
