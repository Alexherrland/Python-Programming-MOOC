import random

def word_generator(characters: str, length: int, amount: int):
    for _ in range(amount):
        yield ''.join(random.choices(characters, k=length))
