# Write your solution here
def length_of_longest(my_list):
    best_value = ""
    for item in my_list:
        if len(item) > len(best_value):
            best_value = item
    return len(best_value)

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)