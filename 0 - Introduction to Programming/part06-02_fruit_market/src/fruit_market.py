# write your solution here

def read_fruits():
    fruit_dic = {}
    with open("src/fruits.csv") as frutas:
        for line in frutas:
            line = line.replace("\n", "")
            parts = line.split(";")
            fruit_dic[parts[0]] = float(parts[1])
    print(fruit_dic)
    return fruit_dic




if __name__ == "__main__":
    read_fruits()