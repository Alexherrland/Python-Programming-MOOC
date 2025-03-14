# write your solution here

def combine_csv(students_csv,exercises_csv):
    data = {}
    with open(students_csv) as students_file:
        for line in students_file:
            line = line.strip().split(";")
            if line[0] != "id":
                data[line[0]] = [line[1],line[2]]

    with open(exercises_csv) as exercises_file:
        for line in exercises_file:
            line = line.strip().split(";")
            if line[0] != "id":
                data[line[0]].append(sum([int(x) for x in line[1:len(line)]]))
    
    for estudiante, values in data.items():
        print(f"{values[0]} {values[1]} {values[2]}")



def main():
    if False:
        student_info = input("Student information: ")
        exercise_data = input("Exercises completed: ")
        exam_data = input("Exam points:")
    else:
        student_info = "students1.csv"
        exercise_data = "exercises1.csv"
        exam_data = ""

    data = combine_csv(student_info,exercise_data)


main()