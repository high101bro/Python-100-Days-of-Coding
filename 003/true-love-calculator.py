#! /usr/bin/env python3

print("This is a love calculator for determining your compatability solely based off names given...")
name1 = input("Person 1's name: ")
name2 = input("Person 2's name: ")

combined_names = name1 + name2
lower_names = combined_names.lower()

t = lower_names.count('t')
r = lower_names.count('r')
u = lower_names.count('u')
e = lower_names.count('e')
first_digit = t + r + u + e

l = lower_names.count('l')
o = lower_names.count('o')
v = lower_names.count('v')
e = lower_names.count('e')
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if score < 10:
    print(f"Your score is {score}, you go there like a peanut alergy and snickers candy bar.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you're alright together like warm soda.")
else:
    print(f"Your score is {score}, you two are perfect like peanut butter and jelly!")
