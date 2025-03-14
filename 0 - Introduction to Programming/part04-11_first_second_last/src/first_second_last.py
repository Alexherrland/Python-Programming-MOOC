# Write your solution here
# You can test your function by calling it within the following block

def first_word(sentence):
    space = sentence.find(" ")
    return sentence[:space]

def second_word(sentence):
    space = sentence.find(" ")
    next_space = sentence.find(" ", space + 1)
    if next_space != -1:
        return sentence[space+1:next_space]
    else:
        return sentence[space+1:]

def last_word(sentence):
    index = sentence.find(" ")

    while index != -1:
        last_space = index
        index = sentence.find(" ", index + 1)
    
    return sentence[last_space+1:]

if __name__ == "__main__":
    sentence = "first second"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))