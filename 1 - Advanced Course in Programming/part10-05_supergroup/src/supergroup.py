# Write your solution here:
class SuperHero:
    def __init__(self, name: str, superpowers: str):
        self.name = name
        self.superpowers = superpowers

    def __str__(self):
        return f'{self.name}, superpowers: {self.superpowers}'

class SuperGroup():
    def __init__(self, name: str, location: str):
        self._name = name
        self._location = location
        self._members = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    def add_member(self, hero: SuperHero):
        self._members.append(hero)

    def print_group(self):
        print(f"{self._name}, {self._location}")
        print("Members:")
        for hero in self._members:
            print(hero)


