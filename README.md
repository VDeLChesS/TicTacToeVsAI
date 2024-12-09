# Tic Tac Toe Game (User vs AI)

This is a simple command-line implementation of Tic Tac Toe, where a user can play against an AI. The game uses color-coded output for better readability:  
- **Red (`X`)** for player moves  
- **Blue (`O`)** for AI moves  

The AI makes random valid moves, ensuring unpredictability.

## Features
- Playable in the terminal.
- Select who goes first: Player or AI.
- Simple and intuitive input system (1-9 grid).
- Highlights moves using colored text.

## How to Play

1. Run the script using Python 3.
2. Choose whether you want to be `X` or `O`.  
   - If you select **`X`**, you go first.
   - If you select **`O`**, the AI goes first.
3. Input your move by selecting a number between **1-9**.  
   The board is numbered as follows:
```
1 | 2 | 3
--|---|--
4 | 5 | 6
--|---|--
7 | 8 | 9
```

4. The game alternates turns between you and the AI.
5. The game ends when:
- A player wins (three in a row).
- The board is full (tie).

## Setup

### Prerequisites
- Python 3.x installed.
- `colorama` library for colored output. Install it using:

```bash
pip install colorama
```

## Running the Game
1. Save the script to a file, e.g., tic_tac_toe.py.
2. Run the script from the terminal:

```bash
python tic_tac_toe.py
```

3. Follow the prompts to play.

## Example Gameplay

### Starting the Game
```mathematica
Choose X or O: X
```
### Board after a few moves:
```diff
 X | O | 3
---|---|---
 4 | X | 6
---|---|---
 O | 8 | 9
```

### Ending:
```diff
 X | O | 3
---|---|---
 4 | X | 6
---|---|---
 O | 8 | X
X wins!
```

## Customization
Feel free to modify the code to:
  - Improve the AI's decision-making.
  - Add more features like score tracking or difficulty levels.

    
# Enjoy the game!
