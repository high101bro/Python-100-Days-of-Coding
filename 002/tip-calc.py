#! /usr/bin/env python3

bill = float(input("How much was your bill? "))
tip = float(input("What percentage would you like to tip? "))
split = int(input("How many people are paying? "))
total_tip = round(bill * (tip / 100),2)
split_pay = round((bill + total_tip) / split,2)
print(f"Your total tip should be ${total_tip} dollars.")
print(f"Each person, including the tip, should pay ${split_pay}.")
