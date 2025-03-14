# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
def palindromes(palindrome):
    if palindrome == palindrome[::-1]:
        print(palindrome,"is a palindrome!")
        return True
    else:
        print("that wasn't a palindrome")
        return False

while True:
    palindrome = input("Please type in a palindrome:")
    if palindromes(palindrome) == True:
        break



