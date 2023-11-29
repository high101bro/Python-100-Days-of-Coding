#! /usr/bin/env python3

year = int(input("What year is it? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It's a leap year.")
        else:
            print("It's NOT a leap year.")
    else:
        print("It's a leap year.")
else:
    print("It's NOT a leap year.")