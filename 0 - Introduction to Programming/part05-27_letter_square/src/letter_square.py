# Write your solution here

def square(letters, layers):
    size = 2 * layers - 1 
    grid = [[''] * size for _ in range(size)] 
    
    for i in range(layers):
        letter = letters[layers - i] 
        for j in range(i, size - i):
            grid[i][j] = letter 
            grid[size - i - 1][j] = letter 
            grid[j][i] = letter  
            grid[j][size - i - 1] = letter 
    
    for row in grid:
        print("".join(row))


def main():
    letters = {i: chr(64 + i) for i in range(1, 27)}
    layers = int(input("Layers: "))
    square(letters,layers)


main()