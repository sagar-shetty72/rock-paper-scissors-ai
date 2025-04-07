import random
import sys
import os

header = "=== ROCK PAPER SCISSORS AI ==="

def main():
    """ Main function to handle game loop and tracking scores. """

    # Scoreboard tracking wins, losses, and ties
    score = {
        "player": 0,
        "ai": 0,
        "ties": 0
    }

    # Tracks how often the player picks each choice
    player_choice_counts = {
        "rock": 0,
        "paper": 0,
        "scissor": 0
    }

    round_num = 0  # Keeps track of game rounds

    while True:
        player_choice = get_player_choice()
        
        if round_num != 0:
            clear_screen()

        update_choice_counts(player_choice_counts, player_choice)
        
        ai_choice = get_smart_ai_choice(player_choice_counts, round_num)  # Smart AI picks a choice
        
        print(header)
        game(player_choice, ai_choice, score, player_choice_counts)  # Determine winner
        round_num += 1

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


def get_smart_ai_choice(player_choice_counts, round_num):
    """ Determines AI move: 70% predictive, 30% random. """

    strategy = random.choices(["random", "predictive"], weights=[0.3, 0.7])[0]  # 70% predictive AI

    # AI plays randomly for the first round since no data exists
    if strategy == "random" or round_num == 0:
        return get_ai_choice()
    else:
        return predict_player_choice(player_choice_counts)


def predict_player_choice(player_choice_counts):
    """ Predicts player's most common move and counters it. """

    # Find the most common move
    player_move = sorted(player_choice_counts.items(), key=lambda item: item[1], reverse=True)[0][0]

    # Dictionary to counter predicted move
    counter = {
        "rock": "paper",
        "paper": "scissor",
        "scissor": "rock"
    }

    return counter[player_move]  # Returns the move that beats the player's most frequent choice


def game(player, ai, score, player_choices):
    """ Runs a single round, determines the winner, and updates scores. """

    # Winning combinations (Player Move, AI Move) -> Winning Move
    winning_combinations = {
        ("rock", "scissor"): "rock",
        ("scissor", "paper"): "scissor",
        ("paper", "rock"): "paper"
    }

    if player == ai:
        print("Draw!")
        winner = "ties"
    elif (player, ai) in winning_combinations:
        print(f"{winning_combinations[(player, ai)]} wins! Player is triumphant.")
        winner = "player"
    else:
        print(f"{ai} wins! Computer is triumphant.")
        winner = "ai"

    update_scores(score, winner)  # Update the scoreboard
    print_scores(score)
    print_player_choices(player_choices)


def update_scores(score, winner):
    """ Updates score dictionary based on winner. """
    score[winner] += 1


def print_scores(score):
    """ Prints the scoreboard in a clean format. """
    
    print("\n---- Scoreboard ----")
    for key, value in score.items():
        print(f"{key.capitalize():<8} | {value}")
    print("--------------------\n")


def print_player_choices(player_choices):
    """ Displays player's choice distribution percentages. """

    total = sum(player_choices.values())

    # Prints choices sorted by most frequent, with percentages
    print(" | ".join(f"{k} : {(v / total * 100):.2f}%" 
                  for k, v in sorted(player_choices.items(), key=lambda item: item[1], reverse=True)))


def update_choice_counts(choice_counts, choice):
    """ Updates player choice count dictionary. """
    choice_counts[choice] += 1 

def clear_screen():
    # Clears the terminal screen for better readability between rounds
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    main()  # Entry point for execution

