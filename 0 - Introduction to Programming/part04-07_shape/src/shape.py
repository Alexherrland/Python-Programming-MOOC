# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block

def shape(witdh,char_triangle,qty_rectangle, char_rectangle):
    for i in range(witdh):
        line(i+1, char_triangle)
    for _ in range(qty_rectangle):
        line(witdh,char_rectangle)


def line(size, character):
    print(character*size)

if __name__ == "__main__":
    shape(5, "x", 2, "o")