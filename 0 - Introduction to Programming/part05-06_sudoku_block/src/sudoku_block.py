


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






if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(block_correct(sudoku, 3, 6))