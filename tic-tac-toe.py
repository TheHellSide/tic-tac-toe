import tkinter as tk
from tkinter import messagebox

HUMAN = -1
BOT = 1

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

# WHICH PLAYER IS MOVING IN THE STATE (s).
def player(state):
    moves = [0, 0]
    for row in state:
        for col in row:
            if col == BOT:
                moves[0] += 1
            elif col == HUMAN:
                moves[1] += 1
    return BOT if moves[0] <= moves[1] else HUMAN

# ALL THE LEGAL MOVES IN THE STATE (s).
def actions(state):
    possible_actions = []
    for row in range(3):
        for col in range(3):
            if state[row][col] == 0:
                possible_actions.append((row, col))

    return possible_actions

# RETURN THE STATE FATER ACTION (a) TAKEN IN STATE (s).
def result(state, action, move_player):
    row, col = action
    new_state = [r[:] for r in state]
    new_state[row][col] = move_player

    return new_state

# ALL THE TERMINAL STATES (s).
def terminal(state):
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]

    if [BOT, BOT, BOT] in win_state or [HUMAN, HUMAN, HUMAN] in win_state:
        return True
    
    for row in state:
        for cell in row:
            if cell == 0:
                return False
            
    return True


# SET WHO IS THE WINNER: X or O (or DRAW)
def utility(state):
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]

    if [BOT, BOT, BOT] in win_state:
        return BOT
    
    elif [HUMAN, HUMAN, HUMAN] in win_state:
        return HUMAN
    
    else:
        return 0

# MINIMAX
def max_value(state):
    if terminal(state):
        return utility(state)
    
    v = -float('inf')
    for action in actions(state):
        v = max(v, min_value(result(state, action, BOT)))

    return v

def min_value(state):
    if terminal(state):
        return utility(state)
    
    v = float('inf')
    for action in actions(state):
        v = min(v, max_value(result(state, action, HUMAN)))

    return v

def minimax(state):
    current = player(state)
    if current == BOT:
        best_score = -float('inf')
        best_action = None

        for action in actions(state):
            score = min_value(result(state, action, BOT))

            if score > best_score:
                best_score = score
                best_action = action

    else:
        best_score = float('inf')
        best_action = None

        for action in actions(state):
            score = max_value(result(state, action, HUMAN))

            if score < best_score:
                best_score = score
                best_action = action

    return best_action

# GUI
class TicTacToeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tic Tac Toe")
        self.geometry("360x360")
        self.resizable(False, False)
        self.configure(bg="#66B2AA")  # sfondo pastello azzurro-verde
        self.state = [row[:] for row in board]
        self.cell_size = 100
        self.canvas = tk.Canvas(self, width=300, height=300, bg="#66B2AA", highlightthickness=0)
        self.canvas.pack(pady=30)
        self.canvas.bind("<Button-1>", self.click)
        self.draw_grid()
        self.update_board()

    def draw_grid(self):
        line_color = "#408080"

        # Verticali
        self.canvas.create_line(100, 0, 100, 300, width=4, fill=line_color)
        self.canvas.create_line(200, 0, 200, 300, width=4, fill=line_color)

        # Orizzontali
        self.canvas.create_line(0, 100, 300, 100, width=4, fill=line_color)
        self.canvas.create_line(0, 200, 300, 200, width=4, fill=line_color)

    def click(self, event):
        if terminal(self.state):
            return
        
        row = event.y // self.cell_size
        col = event.x // self.cell_size

        if self.state[row][col] == 0:
            self.state = result(self.state, (row, col), HUMAN)
            self.update_board()

            if terminal(self.state):
                self.finish_game()
                return
            
            self.after(300, self.bot_move)

    def bot_move(self):
        move = minimax(self.state)

        if move:
            self.state = result(self.state, move, BOT)

        self.update_board()

        if terminal(self.state):
            self.finish_game()

    def update_board(self):
        self.canvas.delete("piece")
        for r in range(3):
            for c in range(3):
                x = c * self.cell_size + self.cell_size//2
                y = r * self.cell_size + self.cell_size//2

                if self.state[r][c] == BOT:
                    self.draw_x(x, y)

                elif self.state[r][c] == HUMAN:
                    self.draw_o(x, y)

    def draw_x(self, x, y):
        offset = 30
        color = "#333333"

        self.canvas.create_line(x - offset, y - offset, x + offset, y + offset,
                                width=6, fill=color, capstyle=tk.ROUND, tags="piece")
        
        self.canvas.create_line(x - offset, y + offset, x + offset, y - offset,
                                width=6, fill=color, capstyle=tk.ROUND, tags="piece")

    def draw_o(self, x, y):
        radius = 28
        color = "#C0BFBF"

        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius,
                                width=6, outline=color, tags="piece")

    def finish_game(self):
        winner = utility(self.state)
        if winner == BOT:
            self.show_winner_popup("BOT wins!", "#333333", button_fg="#333333")  # popup grigio chiaro, bottone grigio scuro

        elif winner == HUMAN:
            self.show_winner_popup("YOU wins!", "#C0BFBF", button_fg="#C0BFBF")  # popup azzurro, bottone bianco

        else:
            self.show_winner_popup("It's a DRAW!", "#797979", button_fg="#7E7E7E")

    def show_winner_popup(self, message, bg_color, button_fg):
        popup = tk.Toplevel(self)
        popup.title("Game Over")
        popup.geometry("280x130")
        popup.configure(bg=bg_color)
        popup.resizable(False, False)

        label = tk.Label(popup, text=message, font=("Helvetica", 24, "bold"),
                         bg=bg_color, fg="white" if bg_color != "#D3D3D3" else "black")
        
        label.pack(expand=True, pady=(20, 10))

        btn = tk.Button(popup, text="OK", font=("Helvetica", 14, "bold"),
                        bg="white" if button_fg != "white" else bg_color,
                        fg=button_fg,
                        activebackground="#ddd",
                        activeforeground=button_fg,
                        relief="flat",
                        cursor="hand2",
                        width=8,
                        command=popup.destroy)
        
        btn.pack(pady=(0, 20))

# MAIN
def main():
    app = TicTacToeApp()
    app.mainloop()

if __name__ == "__main__":
    main()