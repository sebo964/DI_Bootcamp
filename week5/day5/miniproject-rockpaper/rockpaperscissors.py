from game import Game


def get_user_menu_choice():
    while True:
        choice = input(
            "Enter your choice (n for new game, s for scores, or q to quit): "
        ).lower()
        if choice in ["n", "s", "q"]:
            return choice
        else:
            print("Invalid choice. Please try again.")


def print_results(results):
    print("Thank you for playing! Here are the results:")
    print(f"Total games played: {sum(results.values())}")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")


def main():
    results = {"win": 0, "loss": 0, "draw": 0}
    while True:
        choice = get_user_menu_choice()
        if choice == "n":
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == "s":
            print_results(results)
        else:
            print_results(results)
            break


if __name__ == "__main__":
    main()
