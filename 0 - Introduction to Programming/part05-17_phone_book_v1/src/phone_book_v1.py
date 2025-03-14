# Write your solution here
def addValue(phone_book: dict,name: str,number: str):
    phone_book[name] = number
    print("ok!")

def searchValue(phone_book: dict,name: str):
    if name not in phone_book:
        print("no number")
    else:
        print(phone_book[name])

def main():
    phone_book = {}
    while True:
        command = int(input("command (1 search, 2 add, 3 quit):"))
        if command == 3:
            print("quitting...")
            break
        name = input("name:")
        if command == 2: 
            number = input("number:")
            addValue(phone_book,name,number)
            
        else:
            searchValue(phone_book,name)


main()