# Write your solution here


def new_person(name: str, age: int):
    if not name:
        raise ValueError("Name cannot be empty")
    
    if len(name.split()) < 2:
        raise ValueError("Name must contain at least two words")
    
    if len(name) > 40:
        raise ValueError("Name is too long")
    
    if age < 0:
        raise ValueError("Age cannot be negative")
    
    if age > 150:
        raise ValueError("Age cannot be greater than 150")
    
    return (name, age)