def does_cell_exist(x, y):
    if 0 <= x <= 7 and 0 <= y <= 7:
        return True
    return False


def transform_array(array):
    result = []
    for line in range(8):
        for cell in range(8):
            if array[line][cell] == 1:
                result.append([line, cell])
    return result


def is_cell_under_attack(pos, color, board):
    under_attack = [[0 for i in range(8)] for j in range(8)]
    for line in range(8):
        for cell in range(8):
            if board[line][cell]:
                if board[line][cell].color != color:
                    if board[line][cell].type != "king":
                        for position in board[line][cell].allowed_positions():
                            if type(position) != str:
                                under_attack[position[0]][position[1]] = 1
                    else:
                        array = []
                        data = [[1, 1], [-1, -1], [-1, 1], [1, -1], [1, 0], [-1, 0], [0, 1], [0, -1]]
                        for pos in data:
                            if does_cell_exist((line + pos[0]), (cell + pos[1])):
                                if not board[line + pos[0]][cell + pos[1]]:
                                    array.append([line + pos[0], cell + pos[1]])
                                elif board[line + pos[0]][cell + pos[1]].color != color:
                                    array.append([line + pos[0], cell + pos[1]])
    if pos in transform_array(under_attack):
        return True
    else:
        return False


def reverse_color(color):
    match color:
        case "Balck":
            return "White"
        case _:
            return "Black"


class pawn:
    def __init__(self, coords, color, board, ismoved = False):
        self.color = color
        self.board = board
        self.type = "pawn"
        self.x = coords[0]
        self.y = coords[1]
        self.ismoved = ismoved
        self.image_adress = r"images\ "[:-1] + self.type + self.color[0] + ".png"
        board[self.x][self.y] = self
        pass

    def allowed_positions(self):
        array = []
        y_movement = 1
        if self.color == "White": y_movement = -1
        start_position = (7 - 5 * y_movement) // 2
        finish_position = (7 + 7 * y_movement) // 2
        for i in range(-1, 2, 2):
            if does_cell_exist(self.x + i, self.y + y_movement):
                if self.board[self.x + i][self.y + y_movement]:
                    if self.board[self.x + i][self.y + y_movement].color != self.color:
                        array.append([self.x + i, self.y + y_movement])
        if self.board[self.x][self.y + y_movement] == None:
            array.append([self.x, self.y + y_movement])
            if self.y == start_position:
                if self.board[self.x][self.y + 2 * y_movement] == None:
                    array.append([self.x, self.y + 2 * y_movement])
        if abs(self.y - finish_position) == 1 and array != []:
            array = ["choose_piece"] + array
        return array
        pass


class knight:
    def __init__(self, coords, color, board, ismoved = False):
        self.color = color
        self.board = board
        self.type = "knight"
        self.x = coords[0]
        self.y = coords[1]
        self.ismoved = ismoved
        self.image_adress = r"images\ "[:-1] + self.type + self.color[0] + ".png"
        board[self.x][self.y] = self
        pass

    def allowed_positions(self):
        array = []
        data = [[2, 1], [-2, 1], [2, -1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]
        for cell in data:
            if does_cell_exist((self.x + cell[0]), (self.y + cell[1])):
                if not self.board[self.x + cell[0]][self.y + cell[1]]:
                    array.append([self.x + cell[0], self.y + cell[1]])
                elif self.board[self.x + cell[0]][self.y + cell[1]].color != self.color:
                    array.append([self.x + cell[0], self.y + cell[1]])
        return array
        pass


class rook:
    def __init__(self, coords, color, board, ismoved = False):
        self.color = color
        self.board = board
        self.type = "rook"
        self.x = coords[0]
        self.y = coords[1]
        self.ismoved = ismoved
        self.image_adress = r"images\ "[:-1] + self.type + self.color[0] + ".png"
        board[self.x][self.y] = self
        pass

    def allowed_positions(self):
        array = []
        data = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in data:
            delta = [0, 0]
            delta[0] += i[0]
            delta[1] += i[1]
            while does_cell_exist(self.x + delta[0], self.y + delta[1]):
                if not self.board[self.x + delta[0]][self.y + delta[1]]:
                    array.append([self.x + delta[0], self.y + delta[1]])
                elif self.board[self.x + delta[0]][self.y + delta[1]].color != self.color:
                    array.append([self.x + delta[0], self.y + delta[1]])
                    break
                else:
                    break
                delta[0] += i[0]
                delta[1] += i[1]
        return array
        pass


class bishop:
    def __init__(self, coords, color, board, ismoved = False):
        self.color = color
        self.board = board
        self.type = "bishop"
        self.x = coords[0]
        self.y = coords[1]
        self.ismoved = ismoved
        self.image_adress = r"images\ "[:-1] + self.type + self.color[0] + ".png"
        board[self.x][self.y] = self
        pass

    def allowed_positions(self):
        array = []
        data = [[1, 1], [-1, -1], [-1, 1], [1, -1]]
        for i in data:
            delta = [0, 0]
            delta[0] += i[0]
            delta[1] += i[1]
            while does_cell_exist(self.x + delta[0], self.y + delta[1]):
                if not self.board[self.x + delta[0]][self.y + delta[1]]:
                    array.append([self.x + delta[0], self.y + delta[1]])
                elif self.board[self.x + delta[0]][self.y + delta[1]].color != self.color:
                    array.append([self.x + delta[0], self.y + delta[1]])
                    break
                else:
                    break
                delta[0] += i[0]
                delta[1] += i[1]
        return array
        pass


class queen:
    def __init__(self, coords, color, board, ismoved = False):
        self.color = color
        self.board = board
        self.type = "queen"
        self.x = coords[0]
        self.y = coords[1]
        self.ismoved = ismoved
        self.image_adress = r"images\ "[:-1] + self.type + self.color[0] + ".png"
        board[self.x][self.y] = self
        pass

    def allowed_positions(self):
        array = []
        data = [[1, 1], [-1, -1], [-1, 1], [1, -1], [1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in data:
            delta = [0, 0]
            delta[0] += i[0]
            delta[1] += i[1]
            while does_cell_exist(self.x + delta[0], self.y + delta[1]):
                if not self.board[self.x + delta[0]][self.y + delta[1]]:
                    array.append([self.x + delta[0], self.y + delta[1]])
                elif self.board[self.x + delta[0]][self.y + delta[1]].color != self.color:
                    array.append([self.x + delta[0], self.y + delta[1]])
                    break
                else:
                    break
                delta[0] += i[0]
                delta[1] += i[1]
        return array
        pass


class king:
    def __init__(self, coords, color, board, ismoved = False):
        self.color = color
        self.board = board
        self.type = "king"
        self.x = coords[0]
        self.y = coords[1]
        self.ismoved = ismoved
        self.image_adress = r"images\ "[:-1] + self.type + self.color[0] + ".png"
        board[self.x][self.y] = self
        pass

    def is_castling_possible(self):
        array = []
        movement = [1, -1]
        if is_cell_under_attack([self.x, self.y], self.color, self.board):
            return []
        if not self.ismoved:
            for x in movement:
                x_movement = x
                while does_cell_exist(self.x + x_movement, self.y):
                    if self.board[self.x + x_movement][self.y]:
                        if self.board[self.x + x_movement][self.y].type == "rook" and (
                        not self.board[self.x + x_movement][self.y].ismoved) and (
                        not is_cell_under_attack([self.x + x_movement, self.y], self.color, self.board)):
                            array.append([self.x + x_movement, self.y])
                        else:
                            break
                    x_movement += x
        return array
        pass

    def allowed_positions(self):
        array = []
        castling = self.is_castling_possible()
        if castling:
            array = ["castling"]
            for i in castling:
                array.append(i)
            array.append("common")

        data = [[1, 1], [-1, -1], [-1, 1], [1, -1], [1, 0], [-1, 0], [0, 1], [0, -1]]
        for cell in data:
            if does_cell_exist((self.x + cell[0]), (self.y + cell[1])):
                if not self.board[self.x + cell[0]][self.y + cell[1]]:
                    array.append([self.x + cell[0], self.y + cell[1]])
                elif self.board[self.x + cell[0]][self.y + cell[1]].color != self.color:
                    array.append([self.x + cell[0], self.y + cell[1]])

        return array
