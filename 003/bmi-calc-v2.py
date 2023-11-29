#! /usr/bin/env python3

# Say what?!?! python will remove the _ in large numbers, akin to coma's (,) for ease of reading?
# print(1_000 + 50)

height = int(input('What is your height? '))
weight = int(input('What is your weight? '))
bmi = weight / (height ** 2) * 703
if bmi < 18.5:
    print(f"Your BMI is {round(bmi,2)}. You're considered underweight.")
elif bmi < 25:
    print(f"Your BMI is {round(bmi,2)}. You're considered to have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {round(bmi,2)}. You're considered to be slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {round(bmi,2)}. You're considered to be obese.")
else:
    print(f"Your BMI is {round(bmi,2)}. You're considered to be morbidly obese.")
