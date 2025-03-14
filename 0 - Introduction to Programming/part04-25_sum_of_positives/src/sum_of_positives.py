# Write your solution here
def sum_of_positives(my_list):
    index = -1
    my_list.sort()
    for i in my_list:
        if i > 0:
            index = my_list.index(i)
            break
    if index != -1:
        return sum(my_list[index:])
    else:
        return 0

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)