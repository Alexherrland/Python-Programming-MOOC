# write your solution here

def largest():
    with open("src/numbers.txt") as file:
        largest = 0
        for line in file:
            if int(line) > largest:
                largest = int(line)

    print("Total length of lines:", largest)
    return largest



if __name__ == "__main__":
    largest()