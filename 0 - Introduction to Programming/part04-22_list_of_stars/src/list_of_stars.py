# Write your solution here
def list_of_stars(lista):
    for i in lista:
        print("*"*i)
        
if __name__ == "__main__":
    lista = [3, 7, 1, 1, 2]
    list_of_stars(lista)