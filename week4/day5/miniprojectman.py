# What You Will Create

# Create a TicTacToe game in python, where two users can play together.

# tic tac toe


# Instructions

# The game is played on a grid that’s 3 squares by 3 squares.
# Players take turns putting their marks (O or X) in empty squares.
# The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
# When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.


# Hint

# To do this project, you basically need to create four functions:

# display_board() – To display the Tic Tac Toe board (GUI).
# player_input(player) – To get the position from the player.
# check_win() – To check whether there is a winner or not.
# play() – The main function, which calls all the functions created above.
# Note: The 4 functions above are just an example. You can implement many more helper functions or choose a completely different appoach if you want.


# Tips : Consider The Following:

# What functionality will need to accur every turn to make this program work?
# After contemplating the question above, think about splitting your code into smaller pieces (functions).
# Remember to follow the single responsibility principle! each function should do one thing and do it well!

# input dictionary

list_of_inputboxes = {
    "col_1_row_1": " ",
    "col_1_row_2": " ",
    "col_1_row_3": " ",
    "col_2_row_1": " ",
    "col_2_row_2": " ",
    "col_2_row_3": " ",
    "col_3_row_1": " ",
    "col_3_row_2": " ",
    "col_3_row_3": " ",
}


# print board


def print_board(oxvalues):
    print(
        f" {oxvalues['col_1_row_1']} | {oxvalues['col_2_row_1']} | {oxvalues['col_3_row_1']}"
    )
    print("-----------")
    print(
        f" {oxvalues['col_1_row_2']} | {oxvalues['col_2_row_2']} | {oxvalues['col_3_row_2']}"
    )
    print("-----------")
    print(
        f" {oxvalues['col_1_row_3']} | {oxvalues['col_2_row_3']} | {oxvalues['col_3_row_3']}"
    )


# win conditions
def check_win(oxvalues):
    if (
        oxvalues["col_1_row_1"]
        == oxvalues["col_1_row_2"]
        == oxvalues["col_1_row_3"]
        != " "
        or oxvalues["col_2_row_1"]
        == oxvalues["col_2_row_2"]
        == oxvalues["col_2_row_3"]
        != " "
        or oxvalues["col_3_row_1"]
        == oxvalues["col_3_row_2"]
        == oxvalues["col_3_row_3"]
        != " "
        or oxvalues["col_1_row_1"]
        == oxvalues["col_2_row_1"]
        == oxvalues["col_3_row_1"]
        != " "
        or oxvalues["col_1_row_2"]
        == oxvalues["col_2_row_2"]
        == oxvalues["col_3_row_2"]
        != " "
        or oxvalues["col_1_row_3"]
        == oxvalues["col_2_row_3"]
        == oxvalues["col_3_row_3"]
        != " "
        or oxvalues["col_1_row_1"]
        == oxvalues["col_2_row_2"]
        == oxvalues["col_3_row_3"]
        != " "
        or oxvalues["col_1_row_3"]
        == oxvalues["col_2_row_2"]
        == oxvalues["col_3_row_1"]
        != " "
    ):
        return True

    else:
        #     if oxvalues.values() != " ":
        #         return print("Game Over No winner")
        return False


def validate_user_input(colrowuserinput):
    if int(colrowuserinput) < 0 or int(colrowuserinput) > 3:
        print("Invalid input")
        return False
    else:
        return True


def check_if_box_is_empty(list_of_inputboxes, player1):
    if list_of_inputboxes[player1] != " ":  # check if the box is empty
        print("This box is already filled you just lost your turn")
        return False
    else:
        return True


print("Welcome to Tic Tac Toe!")

print_board(list_of_inputboxes)


# Game Code

while check_win(list_of_inputboxes) == False:
    #  Player 1 action
    col_num_player1 = input("PLayer 1 select the columnt: ")
    row_num_player1 = input("Player 1 select the row: ")
    # checks if the user input is valid and asks for retry
    while (
        validate_user_input(col_num_player1) == False
        or validate_user_input(row_num_player1) == False
    ):
        col_num_player1 = input("PLayer 1 select the columnt: ")
        row_num_player1 = input("Player 1 select the row: ")

    player1 = f"col_{col_num_player1}_row_{row_num_player1}"

    while check_if_box_is_empty(list_of_inputboxes, player1) == True:
        list_of_inputboxes[player1] = "x"
        break

    if check_win(list_of_inputboxes) == True:
        print("Player 1 wins!")
        print_board(list_of_inputboxes)
        break
    print_board(list_of_inputboxes)

    # Player 2 action
    col_num_player2 = input("PLayer 2 select the columnt: ")
    row_num_player2 = input("Player 2 select the row: ")
    # checks if the user input is valid and asks for retry

    while (
        validate_user_input(col_num_player2) == False
        and validate_user_input(row_num_player2) == False
    ):
        col_num_player2 = input("PLayer 1 select the columnt: ")
        row_num_player2 = input("Player 1 select the row: ")

    player2 = f"col_{col_num_player2}_row_{row_num_player2}"

    while check_if_box_is_empty(list_of_inputboxes, player2) == True:
        list_of_inputboxes[player2] = "o"
        break

    if check_win(list_of_inputboxes) == True:
        print("Player 2 wins!")
        print_board(list_of_inputboxes)
        break
    print_board(list_of_inputboxes)

print("Game Over")
