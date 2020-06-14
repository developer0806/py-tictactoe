from array import *


def main():
    initialize_board()
    print_board()


def initialize_board():
    global board
    size_of_board = 3
    for i in range(size_of_board):
        row = array('b', [])
        for j in range(size_of_board):
            row.insert(j, -1)
        board.insert(len(board), row)
    return board


def is_not_used(cell_location):
    print("Cell @loc [" + str(cell_location) + "] has value [" + format(board[cell_location[0]][cell_location[1]]) + "]")
    return board[cell_location[0]][cell_location[1]] == -1


def assign_cell(value, cell_location):
    print("assign_cell(" + format(value) + ", " + str(cell_location) + "]")
    if is_not_used(cell_location):
        board[cell_location[0]][cell_location[1]] = value
    else:
        raise Exception("cell " + str(cell_location) + " already used.")


def get_board():
    return board


def print_board():
    global board
    for i in range(len(board)):
        row = board[i]
        row_str = ""
        for j in range(len(row)):
            row_str += str(row[j]) + " "
        print(row_str)


board = []
