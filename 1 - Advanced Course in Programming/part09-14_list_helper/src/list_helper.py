# WRITE YOUR SOLUTION HERE:
class ListHelper:

    @classmethod
    def greatest_frequency(cls, my_list: list):
        frequency = {}
        for item in my_list:
            frequency[item] = frequency.get(item, 0) + 1
            print(frequency)
        return max(frequency, key=frequency.get)

    @classmethod
    def doubles(cls, my_list: list):
        frequency = {}
        for item in my_list:
            frequency[item] = frequency.get(item, 0) + 1

        return sum(1 for count in frequency.values() if count >= 2)
