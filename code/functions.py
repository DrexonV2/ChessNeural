from classes import *
from tkinter import *


def is_king_under_attack(color, board):
    for line in range(8):
        for cell in range(8):
            if board[line][cell]:
                if board[line][cell].color == color and board[line][cell].type == "king":
                    return is_cell_under_attack([line, cell], color, board)
    return "error"


def creating_chess_board(board):
    for i in range(8):
        pawn([i, 6], "White", board)
    for i in range(8):
        pawn([i, 1], "Black", board)
    rook([0, 7], "White", board)
    rook([7, 7], "White", board)
    knight([6, 7], "White", board)
    knight([1, 7], "White", board)
    bishop([5, 7], "White", board)
    bishop([2, 7], "White", board)
    queen([3, 7], "White", board)
    king([4, 7], "White", board)

    rook([0, 0], "Black", board)
    rook([7, 0], "Black", board)
    knight([6, 0], "Black", board)
    knight([1, 0], "Black", board)
    bishop([5, 0], "Black", board)
    bishop([2, 0], "Black", board)
    queen([4, 0], "Black", board)
    king([3, 0], "Black", board)
    pass


def draw_board(root, canvas, board, arr, chosed):
    canvas.pack()
    for i in range(8):
        for j in range(8):
            if (i + j) % 2:
                canvas.create_rectangle(i * 64, j * 64, (i + 1) * 64, (j + 1) * 64, fill="grey", outline="grey")
            else:
                canvas.create_rectangle(i * 64, j * 64, (i + 1) * 64, (j + 1) * 64, fill="white", outline="grey")
            if [i, j] in arr:
                if (i + j) % 2:
                    canvas.create_rectangle(i * 64, j * 64, (i + 1) * 64, (j + 1) * 64, fill="#419873", outline="grey")
                else:
                    canvas.create_rectangle(i * 64, j * 64, (i + 1) * 64, (j + 1) * 64, fill="#52bf90", outline="grey")
            if [i, j] in chosed:
                if (i + j) % 2:
                    canvas.create_rectangle(i * 64, j * 64, (i + 1) * 64, (j + 1) * 64, fill="#ffb21b", outline="grey")
                else:
                    canvas.create_rectangle(i * 64, j * 64, (i + 1) * 64, (j + 1) * 64, fill="#ffca16", outline="grey")
    img = []
    for line in range(8):
        for cell in range(8):
            if board[line][cell]:
                img.append(PhotoImage(file=board[line][cell].image_adress))
                canvas.create_image(32 + line * 64, 32 + cell * 64, image=img[-1])
    canvas.pack()
    root.update()


def all_movements(color, board):
    array = []
    pawns_transform = [knight, rook, bishop, queen]
    for line in range(8):
        for cell in range(8):
            if board[line][cell]:
                if board[line][cell].color == color:
                    movements = board[line][cell].allowed_positions()
                    match movements:
                        case ["choose_piece", *pos]:
                            for position in pos:
                                for piece in pawns_transform:
                                    new_board = [[None for i in range(8)] for j in range(8)]
                                    for a in range(8):
                                        for b in range(8):
                                            if board[a][b]:
                                                board[a][b].__class__([a, b], board[a][b].color, new_board, board[a][b].ismoved)
                                    piece([position[0], position[1]], color, new_board, True)
                                    new_board[line][cell] = None
                                    array.append(new_board)
                        case ["castling", *pos]:
                            i = 0
                            while pos[i] != "common":
                                new_board = [[None for i in range(8)] for j in range(8)]
                                for a in range(8):
                                    for b in range(8):
                                        if board[a][b]:
                                            board[a][b].__class__([a, b], board[a][b].color, new_board, board[a][b].ismoved)
                                movement = abs(pos[i][0] - line) // (pos[i][0] - line)
                                new_board[pos[i][0]][pos[i][1]] = None
                                new_board[line][cell] = None
                                rook([line + movement, cell], color, new_board, True)
                                king([line + 2 * movement, cell], color, new_board, True)
                                if not is_king_under_attack(color, new_board):
                                    array.append(new_board)
                                i += 1
                            for j in range(i + 1, len(pos)):
                                new_board = [[None for i in range(8)] for j in range(8)]
                                for a in range(8):
                                    for b in range(8):
                                        if board[a][b]:
                                            board[a][b].__class__([a, b], board[a][b].color, new_board, board[a][b].ismoved)
                                new_board[line][cell] = None
                                board[line][cell].__class__([pos[j][0], pos[j][1]], color, new_board, True)
                                if not is_king_under_attack(color, new_board):
                                    array.append(new_board)
                            pass
                        case pos:
                            for position in pos:
                                new_board = [[None for i in range(8)] for j in range(8)]
                                for a in range(8):
                                    for b in range(8):
                                        if board[a][b]:
                                            board[a][b].__class__([a, b], board[a][b].color, new_board, board[a][b].ismoved)
                                new_board[line][cell] = None
                                board[line][cell].__class__([position[0], position[1]], color, new_board, True)
                                if not is_king_under_attack(color, new_board):
                                    array.append(new_board)
    return array
