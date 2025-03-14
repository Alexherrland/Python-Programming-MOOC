
def shortest(my_list):
    best_value = my_list[0]
    for item in my_list:
        if len(item) < len(best_value):
            best_value = item
    return best_value

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)