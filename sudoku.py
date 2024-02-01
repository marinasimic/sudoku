from random import choice
import math 

sudoku_board = [[0,0,0, 0,0,0, 0,0,0],
                [0,0,0, 0,0,0, 0,0,0],
                [0,0,0, 0,0,0, 0,0,0],
                [0,0,0, 0,0,0, 0,0,0],
                [0,0,0, 0,0,0, 0,0,0],
                [0,0,0, 0,0,0, 0,0,0],
                [0,0,0, 0,0,0, 0,0,0],
                [0,0,0, 0,0,0, 0,0,0],
                [0,0,0, 0,0,0, 0,0,0]]

def print_board():
    for i in range(0, 9):
        for j in range(0, 9):
            print(sudoku_board[i][j], end=" ")

        print('\n')


def is_used_in_square(row, col, number):
    row_start = row - math.floor(row/3)
    column_start = col - math.floor(col/3)

    for i in range(3):
        for j in range(3):
            if number == sudoku_board[row_start + i][column_start + j]:
                return True

    return False

def is_used_in_row(row, number):
    return number in set(sudoku_board[row])

def is_used_in_column(col, number):
    for row in range(0, 9):
        if sudoku_board[row][col] == number:
            return True

    return False

def is_number_used(row, col, number):
    return is_used_in_row(row, number) or is_used_in_column(col, number) or is_used_in_square(row, col, number)

def fill_diagonal_squares_with_random_numbers():
    diagonal_squares = [(0,3), (3,6), (6,9)]
    for start, end in diagonal_squares:
        used_numbers = ()
        for i in range(start, end):
            for j in range(start, end):
                number = choice(list(set(range(1, 10)) - set(used_numbers)))
                sudoku_board[i][j] = number
                used_numbers = used_numbers + (number,)


def create_sudoku_board():
    fill_diagonal_squares_with_random_numbers()

    print_board()


if __name__ == "__main__":
    create_sudoku_board()