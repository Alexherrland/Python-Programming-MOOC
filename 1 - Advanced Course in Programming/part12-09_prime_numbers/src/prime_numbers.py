# Write your solution here


def prime_numbers():
    num = 2 
    while True:
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):  
            yield num
        num += 1
