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
    def get_user_item(self):
        while True:
            user_item = input("Please choose rock, paper, or scissors: ")
            if user_item in ["rock", "paper", "scissors"]:
                return user_item
            else:
                print("Invalid choice. Please try again.")

    def get_computer_item(self):
        return random.choice(["rock", "paper", "scissors"])

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (
            (user_item == "rock" and computer_item == "scissors")
            or (user_item == "paper" and computer_item == "rock")
            or (user_item == "scissors" and computer_item == "paper")
        ):
            return "win"
        else:
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        print(
            f"You selected {user_item}. The computer selected {computer_item}. You {result}!"
        )
        return result
