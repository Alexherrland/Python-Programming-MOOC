def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = set()
    start_row = row_no
    start_col = column_no

    for i in range(3): 
        for j in range(3): 
            value = sudoku[start_row + i][start_col + j]
            if value > 0:
                if value in numbers:
                    return False
                numbers.add(value)
    
    return True

def column_correct(sudoku: list, column_no: int):
    nuevo_array = []
    for value in sudoku:
        if value[column_no] > 0 and value[column_no] in nuevo_array:
            return False
        nuevo_array.append(value[column_no])
    
    return True

def row_correct(sudoku: list, row_no: int):
    for value in sudoku[row_no]:
        if value != 0:
            if sudoku[row_no].count(value) > 1:
                return False
    return True

def sudoku_grid_correct(sudoku: list):
    for i in range(9):
        if not row_correct(sudoku,i) or not column_correct(sudoku,i):
            return False
    block_positions = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    for row, col in block_positions:
        if not block_correct(sudoku, row, col):
            return False
    return True




if __name__ == "__main__":
    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]
    print(sudoku_grid_correct(sudoku2))