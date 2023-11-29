#! /usr/bin/env python3

# Say what?!?! python will remove the _ in large numbers, akin to coma's (,) for ease of reading?
# print(1_000 + 50)

height = int(input('What is your height? '))
weight = int(input('What is your weight? '))
bmi = weight / (height ** 2) * 703
print(round(bmi,2))