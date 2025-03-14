# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight
    
    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

class Suitcase:
    def __init__(self, max_weight: int):
        self.__items = {}
        self.__max_weight = max_weight
    
    def add_item(self, item: Item):
        if sum(i.weight() for i in self.__items.values()) + item.weight() <= self.__max_weight:
            self.__items[item.name()] = item
    def __str__(self):
        return f"{len(self.__items)} item{'s' if len(self.__items) != 1 else ''} ({self.weight()} kg)"

    def print_items(self):
        for item in self.__items.values():
            print(f"{item}")

    def weight(self):
        return sum(item.weight() for item in self.__items.values())
    
    def heaviest_item(self):
        heaviest_item = max(self.__items.values(), key=lambda item: item.weight())
        return heaviest_item 

class CargoHold:
    def __init__(self, max_weight: int):
        self.__suitcases = []
        self.__max_weight = max_weight

    def add_suitcase(self, suitcase: Suitcase):
        if self.__max_weight - suitcase.weight() > 0:
            self.__suitcases.append(suitcase)
            self.__max_weight -= suitcase.weight()

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()

    def __str__(self):
        return f"{len(self.__suitcases)} suitcase{'s' if len(self.__suitcases) != 1 else ''}, space for {self.__max_weight} kg"

if __name__ == "__main__":
    suitcase = Suitcase(25)
    item = Item("ABC Book", 2)
    suitcase.add_item(item)
    suitcase.print_items()
