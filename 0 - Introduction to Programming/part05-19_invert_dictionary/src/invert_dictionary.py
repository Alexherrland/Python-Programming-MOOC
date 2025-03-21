# Write your solution here
def invert(dictionary: dict):
    old_dictionary = {}

    for key, value in dictionary.items():
        old_dictionary[value] = key

    dictionary.clear()
    dictionary.update(old_dictionary)

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)