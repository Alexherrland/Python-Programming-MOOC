# Write your solution here
lista = []
while True:
    word = input("Word: ")
    if word in lista:
        print(f"You typed in {len(lista)} different words")
        break
    else:
        lista.append(word)