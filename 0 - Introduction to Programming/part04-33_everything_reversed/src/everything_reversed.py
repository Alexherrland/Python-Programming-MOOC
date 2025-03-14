# Write your solution here

def ex_note(exercises):
    return exercises // 10

def check_pass(examen,total_points):
    if examen < 10:
        return 0
    elif total_points < 15:
        return 0
    elif total_points < 18:
        return 1
    elif total_points < 21:
        return 2
    elif total_points < 24:
        return 3
    elif total_points < 27:
        return 4
    else:
        return 5

def print_grade(grado_alumnos):
    for i in range(5, -1, -1):
        print(f"{i}: {"*"*grado_alumnos.count(i)}")



def print_stats(notas_alumnos, grado_alumnos):
    print(f"Points average: ", sum(notas_alumnos) / len(notas_alumnos))
    pass_percentaje = (grado_alumnos.count(0) / len(grado_alumnos))*100
    print("Pass percentage: ",pass_percentaje)
    print("Grade distribution: ")
    print_grade(grado_alumnos)

def main():
    notas_alumnos = []
    grado_alumnos = []
    while True:
        stats = input("Exam points and exercises completed:")
        if stats =="":
            break
        stats_list = stats.split()
        total_points = int(stats_list[0]) + ex_note(int(stats_list[1]))
        notas_alumnos.append(total_points)
        grado = check_pass(int(stats_list[0]),total_points)
        grado_alumnos.append(grado)

    print("Statistics: ")
    print_stats(notas_alumnos,grado_alumnos)
        
    


main()