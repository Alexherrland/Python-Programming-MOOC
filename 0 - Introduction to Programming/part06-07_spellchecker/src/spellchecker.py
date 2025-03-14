# write your solution here

def spellchecker(words, text):
    for index, word in enumerate(text):
        if word.lower() not in words:
            text[index] = f"*{word}*"
    

    print(" ".join(text))



def main():
    with open("src/wordlist.txt") as wordlist:
          words = [line.strip() for line in wordlist]
    text = input("Write text: ")
    text =text.split(" ")
    spellchecker(words, text)
    


main()