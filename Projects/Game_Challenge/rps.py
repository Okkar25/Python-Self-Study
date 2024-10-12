import random
import sys
from enum import Enum


def rps(player_name="Ready Player One"):
    game_count = 0
    player_wins = 0
    computer_wins = 0
    
    print(f"\nHello {player_name}, Welcome to the game.")

    def play_rps():
        nonlocal player_name
        nonlocal player_wins
        nonlocal computer_wins
        
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        player_choice = input("\nPlease enter ... \n 1) for Rock \n 2) for Paper \n 3) for Scissors \n\n")
        
        # recursion
        if player_choice not in ["1","2","3"]:
            print(f"{player_name}, you must enter 1, 2 or 3")
            play_rps()
        
        player = int(player_choice)

        computer_choice = random.choice("123")
        computer = int(computer_choice)

        print(f"{player_name} chooses {str(RPS(player)).replace("RPS.", "").title()} and Computer chooses {str(RPS(computer)).replace("RPS.", "").title()}")

        def decide_winner(player, computer):
            nonlocal player_name
            nonlocal player_wins
            nonlocal computer_wins
            
            if (
                (player == 1 and computer == 3)
                or (player == 2 and computer == 1)
                or (player == 3 and computer == 2)
            ):  
                player_wins += 1
                return f"{player_name}, you win."
            elif player == computer:
                return "It is a Tie."
            else:
                computer_wins += 1
                return "Computer wins."
            
        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1
        
        print(f"\n{player_name}, you have played this game {game_count} {"times" if game_count > 1 else "time"}.")
        print(f"{player_name}'s wins : {player_wins} and Computer wins : {computer_wins}")
            
        # continue playing or not (similar to recursion)   
        while True:
            playagain = input(f"\nPlay Again, {player_name}? \nY for Yes or \nQ to Quit\n\n")
            if playagain.lower() not in ["y", "q"]:
                print(f"{player_name}, you must enter the valid keyword 'Y' or 'Q'.")
                continue
            else:
                break

        # recursion
        if playagain.lower() == "y":
            return play_rps()
        elif playagain.lower() == "q":
            print(f"Thank you for playing, {player_name}.")
            
            if __name__ == "__main__":    
                sys.exit("Bye! Come Back anytime to play.")
            else:
                return # go back to arcade interface
    
    return play_rps



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Provides a personalized game experience.")

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person playing the game.",
    )

    args = parser.parse_args()

    rock_paper_scissor = rps(args.name)
    rock_paper_scissor()
