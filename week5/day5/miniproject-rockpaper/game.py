# # rock paper scissors game

# import random


# def validate_useriteminput(useritem):
#     while useritem.lower() not in options:
#         print("Invalid input")
#         useritem = input("Choose rock, paper or scissors: ")
#         useritem = useritem.lower()
#     return True


# def game(useritem, computeritem):
#     global count_useritem_wins
#     global count_computer_wins
#     global count_ties
#     global count_total_games
#     if useritem == computeritem:
#         print("It's a tie")
#         count_ties = +1
#     elif useritem == "rock":
#         if computeritem == "paper":
#             print("You lose")
#             count_computer_wins += 1
#         else:
#             print("You win")
#             count_useritem_wins += 1
#     elif useritem == "paper":
#         if computeritem == "scissors":
#             print("You lose")
#             count_computer_wins += 1
#         else:
#             print("You win")
#             count_useritem_wins += 1
#     elif useritem == "scissors":
#         if computeritem == "rock":
#             print("You lose")
#             count_computer_wins += 1
#         else:
#             print("You win")
#             count_useritem_wins += 1
#     else:
#         print("Invalid input")
#     count_total_games += 1


# options = ["rock", "paper", "scissors"]

# useritem = str(input("Choose rock, paper or scissors: ")).lower()


# computeritem = random.choice(options)
# count_useritem_wins = 0
# count_computer_wins = 0
# count_ties = 0
# count_total_games = 0

# game(useritem, computeritem)

# useritem_play_again = str(input("Do you want to play again? (y/n): "))

# if useritem_play_again == "y":
#     while useritem_play_again == "y":
#         useritem = str(input("Choose rock, paper or scissors: ")).lower()
#         computeritem = random.choice(options)
#         game(useritem, computeritem)
#         useritem_play_again = str(input("Do you want to play again? (y/n): "))
#         if useritem_play_again == "n":
#             break

# print(
#     f"Computer wins {count_computer_wins}, useritem wins {count_useritem_wins}, Count ties {count_ties}, Count total games {count_total_games}"
# )

import random


class Game:
    def __init__(self):
        self.count_useritem_wins = 0
        self.count_computer_wins = 0
        self.count_ties = 0
        self.count_total_games = 0
        self.options = ["rock", "paper", "scissors"]
        self.useritem = ""
        self.computeritem = ""
        self.useritem_play_again = ""

    def get_useritem_item(self):
        while self.options.lower() not in self.options:
            print("Invalid input")
            self.options = input("Choose rock, paper or scissors: ")
            self.options = self.lower()
        return True

    def get_computer_item(self):
        self.computeritem = random.choice(self.options)

    def get_game_result(self, useritem, computeritem):
        if useritem == computeritem:
            print("It's a tie")
            self.count_ties = +1
        elif useritem == "rock":
            if computeritem == "paper":
                print("You lose")
                self.count_computer_wins += 1
            else:
                print("You win")
                self.count_useritem_wins += 1
        elif useritem == "paper":
            if computeritem == "scissors":
                print("You lose")
                self.count_computer_wins += 1
            else:
                print("You win")
                self.count_useritem_wins += 1
        elif useritem == "scissors":
            if computeritem == "rock":
                print("You lose")
                self.count_computer_wins += 1
            else:
                print("You win")
                self.count_useritem_wins += 1
        else:
            print("Invalid input")
        self.count_total_games += 1

        def get_useritem_play_again(self):
            self.useritem_play_again = str(input("Do you want to play again? (y/n): "))
            if self.useritem_play_again == "y":
                while self.useritem_play_again == "y":
                    self.get_useritem_item()
                    self.useritem_play_again = str(
                        input("Do you want to play again? (y/n): ")
                    )
                    if self.useritem_play_again == "n":
                        break
