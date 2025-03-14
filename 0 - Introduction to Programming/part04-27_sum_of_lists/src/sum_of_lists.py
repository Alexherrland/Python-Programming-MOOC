# Write your solution here
def list_sum(a, b):
    list_result = []
    for index in range(len(a)):
        list_result.append(a[index] + b[index])
    return list_result

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]