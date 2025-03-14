# Write your solution here
# You can test your function by calling it within the following block
def line(int,string):
    if string == "":
        print("*"*int)
    else:
        print(string[0]*int)
    
if __name__ == "__main__":
    line(5, "XXX")