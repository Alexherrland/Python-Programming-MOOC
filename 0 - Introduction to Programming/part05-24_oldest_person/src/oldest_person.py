# Write your solution here

def oldest_person(people: list):
    
    old_person = [people[0][0],people[0][1]]
    for i, value in enumerate(people):
        if value[1] < old_person[1]:
            old_person = [value[0], value[1]]
    
    return old_person[0]


if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))