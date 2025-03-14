# Write your solution here
DIARY_FILE = "diary.txt"

try:
    with open(DIARY_FILE, "r", encoding="utf-8") as file:
        diary_entries = file.read().splitlines()
except FileNotFoundError:
    diary_entries = []

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    choice = input("Function: ")
    
    if choice == "1":
        entry = input("Diary entry: ")
        diary_entries.append(entry)
        with open(DIARY_FILE, "a", encoding="utf-8") as file:
            file.write(entry + "\n")
        print("Diary saved\n")
    
    elif choice == "2":
        print("Entries:")
        for entry in diary_entries:
            print(entry)
        print()
    
    elif choice == "0":
        print("Bye now!")
        break
