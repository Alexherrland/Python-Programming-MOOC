# Write your solution here:

class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    
    def tick(self):
        if self.seconds < 59:
            self.seconds += 1
        elif self.seconds == 59:
            self.seconds = 0
            if self.minutes < 59:
                self.minutes += 1
            else:
                self.minutes = 0 
                self.hours+= 1
                if self.hours == 24:
                    self.hours = 0
    
    def set(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

