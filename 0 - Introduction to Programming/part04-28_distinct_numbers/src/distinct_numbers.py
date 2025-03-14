# Write your solution here

def distinct_numbers(my_list):
    my_list.sort()
    new_list = []
    for i in my_list:
        try: 
            new_list.index(i)
        except ValueError:
            new_list.append(i)
    return new_list

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]