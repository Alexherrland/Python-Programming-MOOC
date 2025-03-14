# Write your solution here
def anagrams(palabra1,palabra2):
    palabra1 = sorted(palabra1)
    palabra2 = sorted(palabra2)
    if palabra1 == palabra2:
        return True
    else:
        return False

if __name__ == "__main__":
    palabra_1 = "tame"
    palabra_2 = "meta"
    anagrams(palabra_1,palabra_2)