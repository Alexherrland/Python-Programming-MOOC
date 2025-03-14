# Write your solution here
# You can test your function by calling it within the following block

def spruce(qty):
    print("a spruce!")
    char = "*"
    for i in range(qty):
        qty_char = (i+1) + i
        qty_space = qty - (i+1)
        print(" "*qty_space +char*qty_char)
    print(" "*(qty - 1)+ char)
if __name__ == "__main__":
    spruce(3)