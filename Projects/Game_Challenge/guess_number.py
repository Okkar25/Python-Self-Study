import sys
import random


def guess_number(player_name="Ready Player One"):
    game_count = 0
    player_wins = 0

    def play_guess_number():
        nonlocal player_name
        nonlocal player_wins

        player_choice = input(
            f"\n{player_name}, guess which number I'm thinking of ... 1. 2 or 3.\n\n"
        )

        if player_choice not in ["1", "2", "3"]:
            print(f"{player_name}, please enter 1,2 or 3.")
            return play_guess_number()

        computer_choice = random.choice("123")

        print(f"\n{player_name}, you chose {player_choice}.")
        print(f"I was thinking about the number {computer_choice}.\n")

        player = int(player_choice)
        computer = int(computer_choice)

        def decide_winner(player, computer):
            nonlocal player_name
            nonlocal player_wins

            if player == computer:
                player_wins += 1
                return f"Congratulations {player_name}, you win!"
            else:
                return f"Sorry, {player_name}. Better luck next time."

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"{player_name}'s wins: {player_wins}")
        print(f"Your winning percentage: {player_wins/game_count:.2%}")

        print(f"\nPlay again, {player_name}?")

        while True:
            play_again = input("\nY for Yes or Q to Quit : ")
            if play_again.lower() not in ["q", "y"]:
                continue
            else:
                break

        if play_again.lower() == "y":
            return play_guess_number()
        else:
            print(f"Thank you for playing, {player_name}.")

            if __name__ == "__main__":
                sys.exit(f"Bye {player_name}!")
            else:
                return # go back to arcade interface

    return play_guess_number


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person playing the game.",
    )

    args = parser.parse_args()
    guess_my_number = guess_number(args.name)
    guess_my_number()
    

