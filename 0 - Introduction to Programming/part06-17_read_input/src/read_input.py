# Write your solution here

def read_input(answer,x1,x2):
    while True:
        try:
            number = int(input(answer))
            if number >= x1 and number <= x2:
                return number
            else:
                print(f"You must type in an integer between {x1} and {x2}")
        except ValueError:
            print(f"You must type in an integer between {x1} and {x2}")
            

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 95, 105)
    print("You typed in:", number)