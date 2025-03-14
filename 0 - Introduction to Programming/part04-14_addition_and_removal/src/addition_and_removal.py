# Write your solution here

lista = []
while True:
    print("The list is now", lista)
    action = input("a(d)d, (r)emove or e(x)it:")
    if action == "x":
        break
    elif action =="d":
        lista.append(len(lista) + 1)
    elif action=="r":
        if len(lista) > 0:
            lista.pop(len(lista) - 1)

print("Bye!")