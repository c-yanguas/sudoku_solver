import time


def print_sudoku(sudoku):
    sudoku_size = int(len(sudoku) ** 0.5)
    square_size = int(sudoku_size ** 0.5)
    sudoku_print = ''
    # | antes de la nueva linea, el +, -, por el | y el ' '
    line_separator = '\n+-' + ('-' * square_size * 2 + '+') +\
                     ('-' * square_size * 2 + '-+') * (square_size - 1)

    for ele, value in enumerate(sudoku):
        if ele % (sudoku_size * square_size) == 0:
            # Separador cada N filas, en el normal 3
            if ele == 0:
                sudoku_print = sudoku_print + line_separator + '\n| ' + str(value)
            else:
                sudoku_print = sudoku_print + ' |' + line_separator + '\n| ' + str(value)

        elif ele % sudoku_size == 0:
            # Nueva fila
            sudoku_print = sudoku_print + ' |\n| ' + str(value)

        elif ele % square_size == 0:
            # Nuevo cuadro
            sudoku_print = sudoku_print + ' | ' + str(value)

        else:
            sudoku_print = sudoku_print + ' ' + str(value)
    sudoku_print = sudoku_print + ' |' + line_separator

    print(sudoku_print)



def get_ele_row(sudoku, pos, sudoku_size):
    first_row_ele = pos // sudoku_size * sudoku_size
    last_row_ele = first_row_ele + sudoku_size
    return sudoku[first_row_ele:last_row_ele]

def get_ele_col(sudoku, ele, sudoku_size):
    ele_col = []
    column  = ele % sudoku_size
    for num in range(len(sudoku)):
        if num % sudoku_size == column:
            ele_col.append(sudoku[num])
    return ele_col

def get_ele_square(sudoku, pos, sudoku_size, square_size):
    square_num       = pos // (sudoku_size * square_size) + pos // square_size
                       # pos por fila                                        + pos por columna
    first_ele_square = square_num // square_size * sudoku_size * square_size + square_num % square_size * square_size
    square = []
    for row in range(square_size):
        row_square = sudoku[first_ele_square + row * sudoku_size : first_ele_square + row * sudoku_size + square_size]
        square = square + row_square
    return square



def check_valid_sudoku(sudoku):
    sudoku_size  = int(len(sudoku) ** 0.5)
    square_size  = int(sudoku_size ** 0.5)
    valid_sudoku = True
    for pos in range(len(sudoku)):
        if sudoku[pos] != 0:
            ele_row    = get_ele_row(sudoku, pos, sudoku_size)
            ele_col    = get_ele_col(sudoku, pos, sudoku_size)
            ele_square = get_ele_square(sudoku, pos, sudoku_size, square_size)
            valid_sudoku = ele_row.count(sudoku[pos]) <= 1 and ele_col.count(sudoku[pos]) <= 1 and ele_square.count(sudoku[pos]) <= 1
            if not valid_sudoku:
                # print('Sudoku incorrecto')
                # print_sudoku(sudoku)
                break
    return valid_sudoku


def get_gap_in_sudoku(sudoku):
    gap_found = False
    for pos, value in enumerate(sudoku):
        if value == 0:
            gap_found = True
            break
    if not gap_found:
        pos = -1
    return pos



def solve_sudoku_aux(sudoku, visited, sudoku_solved):
    visited.append(sudoku.copy())
    pos = get_gap_in_sudoku(sudoku)
    cont = 1
    if pos != -1:
        while cont < 10 and not sudoku_solved:
            sudoku[pos] = cont
            if sudoku not in visited and check_valid_sudoku(sudoku):
                sudoku_solved = solve_sudoku_aux(sudoku.copy(), visited, False)
            cont = cont + 1
    else:
        print('=' * 50 + 'SUDOKU SOLVE' + '=' * 50)
        print_sudoku(sudoku)
        print('=' * 50 + 'SUDOKU SOLVE' + '=' * 50)
        sudoku_solved = True
    return sudoku_solved






def solve_sudoku(sudoku):
    if check_valid_sudoku(sudoku):
        start = time.time()


        print('Input sudoku: ')
        print_sudoku(sudoku)
        solve_sudoku_aux(sudoku, [], False)
        end = time.time()
        print('Time to solve:', round(end - start, 2), 's')
    else:
        print('That sudoku can not be solved')


sudoku =[
        7, 8, 0, 4, 0, 0, 1, 2, 0,
        6, 0, 0, 0, 7, 5, 0, 0, 9,
        0, 0, 0, 6, 0, 1, 0, 7, 8,
        0, 0, 7, 0, 4, 0, 2, 6, 0,
        0, 0, 1, 0, 5, 0, 9, 3, 0,
        9, 0, 4, 0, 6, 0, 0, 0, 5,
        0, 7, 0, 3, 0, 0, 0, 1, 2,
        1, 2, 0, 0, 0, 7, 4, 0, 0,
        0, 4, 9, 2, 0, 6, 0, 0, 7
    ]

sudoku = [
    1,0,0,3,0,0,0,0,0,
    0,0,8,0,5,0,0,0,0,
    0,0,7,0,0,0,0,4,3,
    0,0,0,5,9,6,0,0,0,
    0,0,0,0,0,8,7,1,0,
    0,0,0,0,0,1,0,2,0,
    9,6,0,0,0,0,0,0,1,
    0,0,0,0,0,0,9,0,0,
    0,5,0,8,0,0,6,0,0,
]


solve_sudoku(sudoku)
