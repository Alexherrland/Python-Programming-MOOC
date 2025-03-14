# Write your solution here
from random import randint

def lottery_numbers(amount: int, lower: int, upper: int) -> list:
    numbers = []
    while len(numbers) < amount:
        new_number = randint(lower, upper)
        if new_number not in numbers:
            numbers.append(new_number)
    return sorted(numbers)