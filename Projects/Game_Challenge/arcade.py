import sys
from rps import rps
from guess_number import guess_number


def play_game(player_name="Ready Player One"):
    
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"\n{player_name}, welcome back to the Arcade menu. 🤖 🎮 🕹️")

        player_choice = input(
            '\nPlease choose a game: \n1 = Rock Paper Scissors\n2 = Guess My Number\n\n Or press "X" to exit the arcade.\n\n'
        )

        if player_choice not in ["1", "2", "x", "X"]:
            print(f"\n{player_name}, please enter 1,2 or X.")
            return play_game(player_name)

        welcome_back = True

        if player_choice == "1":
            rock_paper_scissors = rps(player_name)
            rock_paper_scissors()
        elif player_choice == "2":
            guess_my_number = guess_number(player_name)
            guess_my_number()
        else:
            print("\nSee you next time!\n")
            sys.exit(f"Bye {player_name}!")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n",
        "--name",
        required=True,
        metavar="name",
        help="The name of the person playing the game.",
    )

    args = parser.parse_args()
    
    print(f"\n{args.name}, welcome to the Arcade! 🤖 🎮 🕹️")
    
    play_game(args.name)
