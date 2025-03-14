# Write your solution here
def add_student(students: dict, name: str):
    students[name] = []

def add_course(students: dict, name: str, completion: tuple):
    if name in students:
        if completion[1] != 0:
            if len(students[name]) > 0:
                valid = True
                for course in students[name]:
                    if completion[0] == course[0]:
                        if completion[1] > course[1]:
                            index_to_delete = students[name].index((course[0], course[1]))
                            del students[name][index_to_delete]
                            students[name].append(completion)
                        valid = False
                        break
                if valid == True:
                    students[name].append(completion)
            else:
                students[name].append(completion)
            


def print_student(students: dict, name: str):
    for student, values in students.items():
        if name in student:
            print(f"{student}: ")
            if values:
                average = 0
                print(f" {len(values)} completed courses:")
                for key in values:
                    print(f"  {key[0]} {key[1]}")
                    average += key[1]
                print(f" average grade {average/len(values)}")
            else:
                print(" no completed courses")
    if name not in students:
        print(f"{name}: no such person in the database")

def summary(students: dict):
    most_courses = []
    best_average = []
    print("students", len(students))
    for student, values in students.items():
        if most_courses == [] or len(values) > most_courses[1]:
            most_courses = [student,len(values)]
        total_course = 0
        for curso , nota in values:
            total_course += nota
        if len(values) > 0:
            average_course = total_course/len(values)
            if best_average == [] or average_course > best_average[1]:
                best_average = [student,average_course]
    print(f"most courses completed {most_courses[1]} {most_courses[0]}")
    print(f"best average grade {best_average[1]} {best_average[0]}")
if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    #print_student(students, "Peter")
    #print_student(students, "Eliza")
    #print_student(students, "Jack")
    summary(students)