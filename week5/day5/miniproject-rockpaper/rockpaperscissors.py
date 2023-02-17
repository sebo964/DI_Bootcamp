def get_user_menu_choice():
    userselection = int(input("Play new game (1), View highscores (2), Quit (3): "))
    if userselection == 1:
        return userselection == "play"
    if userselection == 2:
        return userselection == "highscores"
    if userselection == 3:
        return userselection == "quit"
    if userselection != 1 or 2 or 3:
        print("Invalid input")
        get_user_menu_choice()
    return userselection


userselction = get_user_menu_choice()


def print_results():
    print(
        f"Computer wins {count_computer_wins}, user wins {count_user_wins}, Count ties {count_ties}, Count total games {count_total_games}"
    )
