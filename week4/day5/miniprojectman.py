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

col1_row1 = "o"
col1_row2 = "x"
col1_row3 = "o"
col2_row1 = "x"
col2_row2 = "o"
col2_row3 = "x"
col3_row1 = "o"
col3_row2 = "x"
col3_row3 = "0"

list_of_inputboxes = {
    col1_row1: "col1_row1",
    col1_row2: "col1_row2",
    col1_row3: "col1_row3",
    col2_row1: "col2_row1",
    col2_row2: "col2_row2",
    col2_row3: "col2_row3",
    col3_row1: "col3_row1",
    col3_row2: "col3_row2",
    col3_row3: "col3_row3",
}

print("Welcome to Tic Tac Toe!")


def print_board(
    col1_row1="",
    col1_row2="",
    col1_row3="",
    col2_row1="",
    col2_row2="",
    col2_row3="",
    col3_row1="",
    col3_row2="",
    col3_row3="",
):
    print(" col1_row1          | col2_row1          | col3_row1    ")
    print(
        "                 "
        + col1_row1
        + " |          "
        + col2_row1
        + "        | "
        + col3_row1
    )
    print("                   |                   |             ")
    print("-----------------------------------------------------")
    print(" col1_row2          | col2_row2          | col3_row3    ")
    print(
        "                 "
        + col1_row2
        + " |         "
        + col2_row2
        + "         | "
        + col3_row2
    )
    print("                   |                   |             ")
    print("-----------------------------------------------------")
    print(" col1row3          | col2row3          | col3row3    ")
    print(
        "                 "
        + col1_row3
        + " |         "
        + col2_row3
        + "         | "
        + col3_row3
    )
    print("                   |                   |             ")


# win conditions
def check_win(
    col1_row1="",
    col1_row2="",
    col1_row3="",
    col2_row1="",
    col2_row2="",
    col2_row3="",
    col3_row1="",
    col3_row2="",
    col3_row3="",
):
    if (
        col1_row1 == col1_row2 == col1_row3
        or col2_row1 == col2_row2 == col2_row3
        or col3_row1 == col3_row2 == col3_row3
        or col1_row1 == col2_row1 == col3_row1
        or col1_row2 == col2_row2 == col3_row2
        or col1_row3 == col2_row3 == col3_row3
        or col1_row1 == col2_row2 == col3_row3
        or col1_row3 == col2_row2 == col3_row1
    ):
        return True

    else:
        return False


print_board()

while check_win() == False:
    player1 = input(
        "Player 1, type in the col and row you want to place your mark example col1_row3: "
    )

    list_of_inputboxes[player1] = "x"
    if check_win():
        print("Player 1 wins!")
        print_board()
        break
    print_board()

    player2 = input(
        "Player 2, type in the col and row you want to place your mark example col1_row3: "
    )

    list_of_inputboxes[player2] = "o"
    if check_win():
        print("Player 1 wins!")
        print_board()
        break
    print_board()


print("Game Over")
