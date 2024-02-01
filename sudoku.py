from random import choice

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

def fill_square_with_random_numbers(i_start, i_end, j_start, j_end):
    used_numbers = ()
    for i in range(i_start, i_end):
        for j in range(j_start, j_end):
            number = choice(list(set(range(1, 10)) - set(used_numbers)))
            sudoku_board[i][j] = number
            used_numbers = used_numbers + (number,)


def create_sudoku_board():
    fill_square_with_random_numbers(0,3,0,3)
    fill_square_with_random_numbers(3,6,3,6)
    fill_square_with_random_numbers(6,9,6,9)

    print_board()

if __name__ == "__main__":
    create_sudoku_board()