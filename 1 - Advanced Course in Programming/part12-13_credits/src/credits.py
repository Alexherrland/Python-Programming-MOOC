from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

#sum_of_numbers = reduce(lambda reduced_sum, item: reduced_sum + item, my_list, 0)

def sum_of_all_credits(credits: list):
    return reduce(lambda reduced_sum, t : reduced_sum + t.credits , credits, 0)


def sum_of_passed_credits(credits: list):
    return reduce(lambda reduced_sum, t : reduced_sum + t.credits , filter(lambda t : t.grade > 1, credits), 0)

def average(credits: list):
    average = reduce(lambda avg_atemp, t : avg_atemp + t.grade, filter(lambda t: t.grade >= 1, credits), 0)
    return average/len(list(filter(lambda t: t.grade >= 1, credits)))
