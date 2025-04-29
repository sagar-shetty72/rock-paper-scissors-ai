from colorama import Fore, Style
import random
import sys
import os

header = "=== ROCK PAPER SCISSORS AI ==="

logo = r"""
     ___           ___           ___                    ___                 
    /\  \         /\  \         /\  \                  /\  \          ___   
   /::\  \       /::\  \       /::\  \                /::\  \        /\  \  
  /:/\:\  \     /:/\:\  \     /:/\ \  \              /:/\:\  \       \:\  \ 
 /::\~\:\  \   /::\~\:\  \   _\:\~\ \  \            /::\~\:\  \      /::\__\
/:/\:\ \:\__\ /:/\:\ \:\__\ /\ \:\ \ \__\          /:/\:\ \:\__\  __/:/\/__/
\/_|::\/:/  / \/__\:\/:/  / \:\ \:\ \/__/          \/__\:\/:/  / /\/:/  /   
   |:|::/  /       \::/  /   \:\ \:\__\                 \::/  /  \::/__/    
   |:|\/__/         \/__/     \:\/:/  /                 /:/  /    \:\__\    
   |:|  |                      \::/  /                 /:/  /      \/__/    
    \|__|                       \/__/                  \/__/                """

# Game state tracking scores and choice distribution
game_state = {
    "scoreboard" : {
        "player": 0,
        "ai": 0,
        "ties": 0
    },
    "player_choices" : {
        "rock": 0,
        "paper": 0,
        "scissor": 0
    },
    "ai_choices" : {
        "rock": 0,
        "paper": 0,
        "scissor": 0
    },
    "round_num" : 1
}

def main():

    print(Fore.CYAN + logo + Style.RESET_ALL)
    print() #Empty line for formatting

    print("1. Traditional (Turn-by-turn player input)")
    print("2. Simulated (Run any number of games and see results)")
    print("3. Exit Game (I'm sad to see you go)")
    print()

 
    while True:
        try:
            choice = int(input("Pick your poison (1, 2, 3): "))

            if choice == 1:
                play_rounds(game_state)
                break
            elif choice == 2:
                simulate(game_state)
                break
            elif choice == 3:
                clear_screen()
                sys.exit()
            else:
                continue  # Reprompt on invalid input
        except ValueError:
            continue 

def simulate():
    print("test")
def play_rounds(game_state):

    while True:
        player_choice = get_player_choice() #Player picks a choice

        if game_state["round_num"] != 1:
            clear_screen()

        print() #Empty line for formatting
        print(Fore.CYAN + header + Style.RESET_ALL)

        update_choice_counts(game_state, player_choice) # Player choices dictionary updated
        ai_choice = get_smart_ai_choice(game_state)  # Smart AI picks a choice

        winner = game(player_choice, ai_choice, game_state)  # Determine winner
        print_round_results(player_choice, ai_choice, winner) # Print round result
        update_scores(game_state, winner)  # Update the scoreboard
        print_scores(game_state) # Print latest scoreboard
        print_player_choices(game_state) # Print player choice distribution
        print_player_win_percent(game_state) # Print player win %
            
        game_state["round_num"] += 1


def get_player_choice():
    """ Prompts player for a choice, ensures input is valid. """

    valid_choices = {
        "rock":"rock",
        "r":"rock",
        "scissor":"scissor",
        "s":"scissor",
        "paper":"paper",
        "p":"paper"
    }

    while True:
        try:
            choice = input("Enter your choice (r/p/s or the full word or done): ").strip().lower()

            if choice == "done":
                clear_screen()
                sys.exit()  # Terminates game safely
            elif choice in valid_choices:
                return valid_choices[choice]
            else:
                continue  # Reprompt on invalid input

        except EOFError:
            print("Bye now!")
            sys.exit()  # Gracefully exits on unexpected termination


def get_ai_choice():
    """ AI picks a random move. """

    plays = ["rock", "paper", "scissor"]
    return random.choice(plays)


def get_smart_ai_choice(game_state):
    """ Determines AI move: 70% predictive, 30% random. """

    strategy = random.choices(["random", "predictive"], weights=[0.3, 0.7])[0]  # 70% predictive AI

    # AI plays randomly for the first round since no data exists
    if strategy == "random" or game_state["round_num"] == 1:
        return get_ai_choice()
    else:
        return predict_player_choice(game_state)


def predict_player_choice(game_state):
    """ Predicts player's most common move and counters it. """

    # Find the most common move
    player_move = sorted(game_state["player_choices"].items(), key=lambda item: item[1], reverse=True)[0][0]

    # Dictionary to counter predicted move
    counter = {
        "rock": "paper",
        "paper": "scissor",
        "scissor": "rock"
    }

    return counter[player_move]  # Returns the move that beats the player's most frequent choice


def game(player, ai, game_state):
    """ Runs a single round, determines the winner, and updates scores. """

    # Winning combinations (Player Move, AI Move) -> Winning Move
    winning_combinations = {
        ("rock", "scissor"): "rock",
        ("scissor", "paper"): "scissor",
        ("paper", "rock"): "paper"
    }

    if player == ai:
        winner = "ties"
    elif (player, ai) in winning_combinations:
        winner = "player"
    else:
        winner = "ai"

    return winner

def print_round_results(player, ai, winner):
    print() # Empty line for formatting
    
    if winner == "ties":
        print(Fore.YELLOW + f"You both chose {player}! It's a draw." + Style.RESET_ALL)
    elif winner == "player":
        print(Fore.GREEN + f"You chose {player} and computer chose {ai}. Player prevails." + Style.RESET_ALL)
    else:
        print(Fore.RED + f"Computer chose {ai} and you chose {player}! Computer is triumphant." + Style.RESET_ALL)

def update_scores(game_state, winner):
    """ Updates game state based on winner. """
    game_state["scoreboard"][winner] += 1


def print_scores(game_state):
    """ Prints the scoreboard in a clean format. """
    
    print(Fore.MAGENTA + f"\n---- Round {game_state["round_num"]} -------" + Style.RESET_ALL)
    for key, value in game_state["scoreboard"].items():
        print(f"{key.capitalize():<8} | {value}")
    print("--------------------\n")


def print_player_choices(game_state):
    """ Displays player's choice distribution percentages. """

    total = sum(game_state["player_choices"].values())
    # Prints choices sorted by most frequent, with percentages
    print(Fore.BLUE + "Your choice distribution" + Style.RESET_ALL)
    print(" | ".join(f"{k} : {(v / total * 100):.2f}%" 
                  for k, v in sorted(game_state["player_choices"].items(), key=lambda item: item[1], reverse=True)))
    print() # Empty line for formatting

def print_player_win_percent(game_state):

    win_percent = game_state["scoreboard"]["player"]/sum(game_state["scoreboard"].values())
    print(f"Your win %: {win_percent*100:.2f}%")
    print()

def update_choice_counts(game_state, player_choice):
    """ Updates player choice count dictionary. """
    game_state["player_choices"][player_choice] += 1 

def clear_screen():
    # Clears the terminal screen for better readability between rounds
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    main()  # Entry point for execution

