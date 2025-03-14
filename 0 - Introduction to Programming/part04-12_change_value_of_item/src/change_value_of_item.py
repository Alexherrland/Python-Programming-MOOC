# Write your solution here

list = [1,2,3,4,5]

while True:
    index = int(input("Index: "))

    if index < len(list) and index != -1:
        value = int(input("Value: "))
        list[index] = value
        print(list)
    else:
        break