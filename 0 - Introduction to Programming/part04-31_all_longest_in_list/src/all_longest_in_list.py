# Write your solution here
def all_the_longest(my_list):
    best_value = ""
    list_values = []
    for item in my_list:
        if len(item) > len(best_value):
            best_value = item

    for item in my_list:
        if len(item) >= len(best_value):
            list_values.append(item)
    return list_values

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)