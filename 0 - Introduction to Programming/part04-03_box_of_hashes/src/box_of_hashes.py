# Copy here code of line function from previous exercise

def box_of_hashes(height):
    # You should call function line here with proper parameters
    for _ in range(height):
        line(10, "#")

def line(qty,character):
    print(character*qty)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
