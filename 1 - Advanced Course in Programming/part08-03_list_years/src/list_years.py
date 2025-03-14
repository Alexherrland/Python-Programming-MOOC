# Write your solution here
# Remember the import statement
from datetime import date

def list_years(dates: list):
    #new_list = sorted(dates, key=lambda x:date.month(x))
    new_list = [date.year for date in sorted(dates)]
    
    for date in sorted(dates):
        print(date)
        #new_list.append(date.year)
    return new_list

if __name__ == "__main__":
    date1 = date(2019, 2, 3)
    date2 = date(2006, 10, 10)
    date3 = date(1993, 5, 9)

    years = list_years([date1, date2, date3])
    print(years)