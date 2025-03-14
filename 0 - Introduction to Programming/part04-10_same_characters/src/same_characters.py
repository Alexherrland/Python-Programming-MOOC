# Write your solution here
# You can test your function by calling it within the following block

def same_chars(word, index1, index2):
    if index2 < len(word) and  index1 < len(word):
        if word[index1] == word[index2]:
            return True
        else:
            return False
    else:
        return False
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))