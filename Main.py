import tkinter as tk
from tkinter import messagebox

def check_winner():
    for line in win_combinations:
        a, b, c = line
        if board[a] == board[b] == board[c] and board[a] != "":
            buttons[a].config(bg="lightgreen")
            buttons[b].config(bg="lightgreen")
            buttons[c].config(bg="lightgreen")
            messagebox.showinfo("Game Over", f"{board[a]} wins!")
            reset_board()
            return True
    if "" not in board:
        messagebox.showinfo("Game Over", "It's a Draw!")
        reset_board()
        return True
    return False

def on_click(index):
    global current_player
    if board[index] == "" and not check_winner():
        board[index] = current_player
        buttons[index].config(text=current_player, state=tk.DISABLED)
        if not check_winner():
            current_player = "O" if current_player == "X" else "X"

def reset_board():
    global board, current_player
    board = ["" for _ in range(9)]
    current_player = "X"
    for button in buttons:
        button.config(text="", state=tk.NORMAL, bg="SystemButtonFace")

# Setup Tkinter Window
root = tk.Tk()
root.title("Tic-Tac-Toe")

current_player = "X"
board = ["" for _ in range(9)]
win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 24), width=5, height=2, command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

reset_btn = tk.Button(root, text="Restart", font=("Arial", 14), command=reset_board)
reset_btn.grid(row=3, column=0, columnspan=3)

root.mainloop()



