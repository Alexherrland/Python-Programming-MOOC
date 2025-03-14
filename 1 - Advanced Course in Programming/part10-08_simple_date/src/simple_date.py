# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __repr__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __eq__(self, other):
        return (self.day, self.month, self.year) == (other.day, other.month, other.year)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)

    def __gt__(self, other):
        return (self.year, self.month, self.day) > (other.year, other.month, other.day)

    def __add__(self, days):
        day = self.day + days
        month = self.month
        year = self.year
        
        while day > 30:
            day -= 30
            month += 1
            if month > 12:
                month = 1
                year += 1
        
        return SimpleDate(day, month, year)
    
    def __sub__(self, other):
        days_self = self.year * 360 + self.month * 30 + self.day
        days_other = other.year * 360 + other.month * 30 + other.day
        return abs(days_self - days_other)
