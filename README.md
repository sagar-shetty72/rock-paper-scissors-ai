# Rock Paper Scissors AI

A Python-based Rock Paper Scissors game featuring an AI opponent that adapts to player behavior using basic prediction. Future updates will introduce advanced strategies, including Markov chains and game simulations.

## Features
- **Traditional Gameplay**: Play against an AI opponent.
- **Basic AI Strategy**: AI uses a weighted mix of random (30%) and predictive (70%) choices.
- **Player Choice Tracking**: Tracks the frequency of player choices and displays percentages.
- **Smart Counterplay**: AI attempts to counter the player's most frequent move.

## Future Improvements
1. ~~**UI Enhancements**: Improve game output for clarity and user experience.~~
2. ~~**Simulated Games**: Add an option to simulate games instead of manual play.~~
3. **Advanced AI (Markov Chains)**: Implement predictive modeling for better AI decisions.
4. **Custom Strategy Weights**: Allow users to adjust the AI’s strategy mix (e.g., 40% random, 60% predictive/Markov).
5. **Difficulty Levels**: Introduce selectable difficulty settings based on AI intelligence.
6. **Game Data Logging**: Store match results for trend analysis.
7. **Adaptive AI**: AI dynamically adjusts its strategy over multiple games.

## What's New (April 5, 2025)
- Added player win percentage display
- Improved round and result formatting
- Integrated color-coded CLI output (using Colorama)
- Added shorthand input support (r/p/s)
- Cleaned up scoreboard and game flow
- Added .gitignore and requirements.txt for environment management

## What's New (April 29, 2025)
- Added a new main menu and logo
- Refactored for function reusability
- Added a game_state variable to simplify tracking
- Added the ability to simulate games

## Installation & Usage
1. Clone this repository:
   ```sh
   git clone https://github.com/sagar-shetty72/rock-paper-scissors-ai.git
   ```
2. Navigate to the project directory:
   ```sh
   cd rock-paper-scissors-ai
   ```
3. Create a virtual environment and activate it:
   ```
   python3 -m venv venv
   ```
   ```
   source venv/bin/activate

   ```
4. Install dependencies
   ```
   pip install -r requirements.txt
   ```
5. Run the game
   ```
   python game.py
   ```

## Contributions
Open to suggestions! Feel free to fork, improve, and submit PRs.

## License
MIT License
