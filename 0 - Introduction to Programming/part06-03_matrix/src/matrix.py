# write your solution here
def obtain_file():
    with open("src/matrix.txt") as file:
        matrix = [line.strip().split(",") for line in file]
    return matrix

def matrix_sum():
    matrix = obtain_file()
    total = 0
    for row in matrix:
        total += sum(int(num) for num in row) 
    return total

def matrix_max():
    matrix = obtain_file()
    max_value = float('-inf')
    for row in matrix:
        row_max = max(int(num) for num in row)
        if row_max > max_value:
            max_value = row_max
    return max_value

def row_sums():
    matrix = obtain_file()
    return [sum(int(num) for num in row) for row in matrix]

if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())