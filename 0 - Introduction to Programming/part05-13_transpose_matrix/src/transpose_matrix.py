# Write your solution here

def transpose(matrix: list):
    old_matrix = [row[:] for row in matrix]
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            matrix[i][j] =  old_matrix[j][i]


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transpose(matrix)
    print(matrix)