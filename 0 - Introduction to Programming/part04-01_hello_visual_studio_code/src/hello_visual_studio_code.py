# Write your solution here
editor = ""

while editor.lower() != "visual studio code":
    editor = input("Editor: ")
    if editor.lower() == "word" or editor.lower() == "notepad":
        print("awful")
    elif editor.lower() != "visual studio code":
        print("not good")

print("an excellent choice!")