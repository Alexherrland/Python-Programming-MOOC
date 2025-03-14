# Write your solution here

def count_matching_elements(matrix, number):
    cont = 0
    for row in matrix:
        for col in row:
            if col == number:
                cont += 1
    return cont

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))