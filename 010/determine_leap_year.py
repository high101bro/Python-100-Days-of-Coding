#! /usr/bin/env python3

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
 

def days_in_the_month(year, month):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month == 2 and is_leap(year):
        return 29
    else:
        return month_days[month - 1]

year = int(input(f"Enter year: "))
if is_leap(year) == True:
    determine = "is a"
elif is_leap(year) == False:
    determine = "is not a"
print(f"The year {year} {determine} leap year.")
# month = int(input(f"Enter month as number: "))
# days = days_in_the_month(year,month)
# print(days)