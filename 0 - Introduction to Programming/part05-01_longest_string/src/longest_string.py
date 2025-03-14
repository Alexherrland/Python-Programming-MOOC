# Write your solution here

def longest(strings):
    long_string =""
    for word in strings:
        if len(word) > len(long_string):
            long_string = word
    return long_string

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
