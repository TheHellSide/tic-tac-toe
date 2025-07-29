# tic-tac-toe with MiniMax
A simple Tic Tac Toe game with a graphical user interface built using Tkinter, featuring an intelligent AI opponent powered by the Minimax algorithm.

---
### Features
- Play classic Tic Tac Toe on a 3x3 grid.
- Challenge a computer opponent using the Minimax algorithm, which guarantees an optimal strategy.
- Clean and minimalist GUI created with Tkinter.
- End-of-game popups indicating win, loss, or draw.
- Custom pastel color scheme for a pleasant visual experience.

---
### Rules
- The game is played on a 3x3 grid.
- Two players take turns marking a cell, one with O (Human) and the other with X (Bot).
- The goal is to be the first player to place three of their marks in a horizontal, vertical, or diagonal row.
- If all nine cells are filled without either player achieving three in a row, the game ends in a draw.
- In this implementation, the Human always plays first with O.

---
### Minimax Algorithm
The AI opponent uses the Minimax algorithm, a decision rule commonly used in two-player turn-based games. It recursively explores all possible game states and selects the move that maximizes its chance of winning while minimizing the opponent's chance.
This ensures the bot never loses and plays optimally.

---
### Code Structure
- Game Logic: Manages the game board, player turns, move validation, terminal state detection, and scoring.
- Minimax AI: Implements recursive functions max_value and min_value to evaluate board states and choose the best move.
- GUI: The TicTacToeApp class handles drawing the grid, rendering X's and O's, capturing user clicks, and displaying result popups.
- Endgame Notifications: Popups inform the user of game results with a stylish colored interface.

---
### Requirements
- Python 3.x
- Tkinter (usually included with standard Python installations)

---
### It's Run-Time
1. Download the Python script or copy the source code into a file named tic_tac_toe.py.
2. Open a terminal or command prompt in the directory containing the file.
3. Run the script with the command:
```bash
python tic_tac_toe.py
```
4. A window will open showing the Tic Tac Toe board. Click on any empty cell to place your O and start the game.
5. Have fun ;)
