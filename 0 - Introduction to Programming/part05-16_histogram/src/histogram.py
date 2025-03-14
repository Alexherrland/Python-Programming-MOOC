# Write your solution here
def histogram(string: str):
    groups= {}
    for char in string:
        if char not in groups:
            groups[char] = 0
        groups[char] += 1
    for key , value in groups.items():
        print(f"{key} {"*"*value}")
        


if __name__ =="__main__":
    histogram("abba")