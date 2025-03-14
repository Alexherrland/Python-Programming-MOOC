# tee ratkaisusi tänne
class CourseRecord:
    def __init__(self):
        self.__courses = {}

    def add_course(self, name: str, grade: int, credit: int):
        grade = int(grade)
        credit = int(credit)
        if name not  in self.__courses:
            self.__courses[name] = [grade, credit]
        else:
            if grade > self.__courses[name][0]:
                self.__courses[name] = [grade, credit]

    def get_course(self, name: str):
        if name in self.__courses:
            grade, credit = self.__courses[name]
            return f"{name} ({credit} cr) grade {grade}"
        return None

    def all_courses(self):
        return self.__courses


class CourseRecordsApplication:
    def __init__(self):
        self.__course = CourseRecord()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
            name = input("course: ")
            grade = input("grade: ")
            credit = input("credits: ")
            self.__course.add_course(name, grade,credit)

    def get_data(self):
        name = input("course: ")
        course = self.__course.get_course(name)
        if course:
            print(course)
        else:
            print(f"no entry for this course")
    
    def print_statistics(self):
        courses = self.__course.all_courses()
        total_courses = len(courses)
        total_credits = sum(course[1] for course in courses.values())
        if total_courses == 0:
            print("No courses registered.")
            return

        grades = [course[0] for course in courses.values()]
        mean_grade = sum(grades) / total_courses
        grade_distribution = {i: grades.count(i) for i in range(1, 6)}

        print(f"{total_courses} completed courses, a total of {total_credits} credits")
        print(f"mean {mean_grade:.1f}")
        print("grade distribution")
        for grade in range(5, 0, -1):
            print(f"{grade}: {'x' * grade_distribution.get(grade, 0)}")
        
    def execute(self):
        self.help()

        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_data()
            elif command == "3":
                self.print_statistics()
            else:
                self.help()


application = CourseRecordsApplication()
application.execute()