import time
from functions import *
from tkinter import *
from random import *

board = [[None for j in range(8)] for k in range(8)]

king([4,7], "White", board)
king([3,0], "Black", board)
rook([0,0], "Black", board)
rook([7,0], "Black", board)
rook([0,7], "White", board)
rook([7,7], "White", board)

arr = all_movements("White", board)

root = Tk()
canvas = Canvas(root, width=512, height=512)
canvas.pack()
draw_board(root, canvas, board, arr, [])
time.sleep(1)

for i in all_movements("White", board):
    draw_board(root, canvas, i, [], [])
    time.sleep(1)


draw_board(root, canvas, board, [], [])
time.sleep(60)
root.mainloop()
