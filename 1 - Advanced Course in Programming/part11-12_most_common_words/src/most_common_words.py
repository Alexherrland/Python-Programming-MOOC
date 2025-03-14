# WRITE YOUR SOLUTION HERE:
import string

def most_common_words(filename: str, lower_limit: int):
    word_count = {}
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.translate(str.maketrans('', '', string.punctuation))
            words = line.split()
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
    
    return {word: count for word, count in word_count.items() if count >= lower_limit}
