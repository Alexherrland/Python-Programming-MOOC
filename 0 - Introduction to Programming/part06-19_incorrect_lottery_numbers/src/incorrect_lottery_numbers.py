# Write your solution here
def filter_incorrect():
    try:
        with open("lottery_numbers.csv") as source, open("correct_numbers.csv", "w") as target:
            for line in source:
                if is_valid_line(line.strip()):
                    target.write(line)
    except:
        pass

def is_valid_line(line):
    if ";" not in line:
        return False
    week_part, numbers_part = line.split(";")
    if not check_week_format(week_part):
        return False
    return check_numbers(numbers_part)

def check_week_format(week_part):
    if not week_part.startswith("week "):
        return False
    try:
        week_num = int(week_part[5:])
        return week_num > 0
    except ValueError:
        return False

def check_numbers(numbers_part):
    try:
        numbers = [int(num) for num in numbers_part.split(",")]
        
        if len(numbers) != 7:
            return False
        if not all(1 <= num <= 39 for num in numbers):
            return False

        if len(set(numbers)) != len(numbers):
            return False
        
        return True
        
    except ValueError:
        return False