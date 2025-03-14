# Write your solution here
lista = []
ordered_list = []

while True:
    item = int(input("New item: "))
    if item == 0:
        print("Bye!")
        break
    lista.append(item)
    ordered_list = sorted(lista)
    print("The list now:", lista)
    print("The list in order:",ordered_list)