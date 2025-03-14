# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []

    def add(self,person: Person):
        self.persons.append(person)
    
    def is_empty(self):
        return len(self.persons) == 0
    
    def print_contents(self):
        total_height = sum(person.height for person in self.persons)
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {total_height} cm")
        for person in self.persons:
            print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        if len(self.persons) == 0:
            return None
        short_person = self.persons[0]
        for person in self.persons:
            if person.height < short_person.height:
                short_person = person
        return short_person

    def remove_shortest(self):
        if len(self.persons) == 0:
            return None
        shortest_person = self.shortest()
        self.persons.remove(shortest_person)
        return shortest_person


if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.print_contents()

    print()

    removed = room.remove_shortest()

    print()

    room.print_contents()