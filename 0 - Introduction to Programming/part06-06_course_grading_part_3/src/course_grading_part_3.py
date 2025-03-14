# tee ratkaisu tänne
def calculate_grade(nota):
    if nota < 15:
        return 0
    if nota < 18:
        return 1
    if nota < 21:
        return 2
    if nota < 24:
        return 3
    if nota < 28:
        return 4
    else:
        return 5


def combine_csv(students_csv, exercises_csv, exam_data):
    data = {}

    with open(students_csv) as students_file:
        for line in students_file:
            line = line.strip().split(";")
            if line[0] != "id":
                data[line[0]] = [line[1], line[2]] 

    with open(exercises_csv) as exercises_file:
        for line in exercises_file:
            line = line.strip().split(";")
            if line[0] != "id":
                total_exercises = sum([int(x) for x in line[1:]])  
                completed_percentage = total_exercises / 40.0 
                exercise_points = int(completed_percentage * 10)  
                exercise_points = min(exercise_points, 10)  
                data[line[0]].append(total_exercises) 
                data[line[0]].append(exercise_points) 

    with open(exam_data) as exam_notes:
        for line in exam_notes:
            line = line.strip().split(";")
            if line[0] != "id":
                student_id = line[0]
                if student_id in data:
                    exam_points = sum([int(x) for x in line[1:]]) 
                    data[student_id].append(exam_points) 

    print(f"{'name':<30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}{'grade':<10}")

    for student, values in data.items():
        total_points = values[3] + values[4]  
        grade = calculate_grade(total_points)
        print(f"{values[0] + ' ' + values[1]:<30}{values[2]:<10}{values[3]:<10}{values[4]:<10}{total_points:<10}{grade:<10}")


def main():
    if True:
        student_info = input("Student information: ")
        exercise_data = input("Exercises completed: ")
        exam_data = input("Exam points:")
    else:
        student_info = "src/students2.csv"
        exercise_data = "src/exercises2.csv"
        exam_data = "src/exam_points2.csv"

    data = combine_csv(student_info,exercise_data,exam_data)


main()