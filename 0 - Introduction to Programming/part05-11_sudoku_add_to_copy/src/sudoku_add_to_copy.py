# Write your solution her
# Write your solution here
def print_sudoku(sudoku: list):
    for i, row in enumerate(sudoku):
        if i % 3 == 0:
            print()
        for j, char in enumerate(row):
            if j % 3 == 0 and j != 0:
                print(" ",end="")
            if char != 0:
                print(f"{char}",end=" ")
            else:
                print("_",end=" ")
        print()
    print()
        
def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
    new_sudoku = [row[:] for row in sudoku]
    new_sudoku[row_no][column_no] = number
    return new_sudoku

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)