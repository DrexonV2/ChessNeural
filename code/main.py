import time
from functions import *
from tkinter import *
from random import *

board = [[None for j in range(8)] for k in range(8)]

creating_chess_board(board)

arr = all_movements("Black", board)

root = Tk()
canvas = Canvas(root, width=512, height=512)
canvas.pack()
draw_board(root, canvas, board, [], [])
time.sleep(1)
while all_movements("White", board):
    new_board = choice(all_movements("White", board))
    board = [[new_board[j][i] for i in range(8)] for j in range(8)]
    draw_board(root, canvas, board, [], [])
    time.sleep(1)
    if not all_movements("Black", board):
        break
    new_board = choice(all_movements("Black", board))
    board = [[new_board[j][i] for i in range(8)] for j in range(8)]
    draw_board(root, canvas, board, [], [])
    time.sleep(1)

draw_board(root, canvas, board, [], [])
time.sleep(60)
root.mainloop()
