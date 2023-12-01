#! /usr/bin/env python3

student_heights = input(f"Input student heights: ").split()
for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])

total_height = 0
for height in student_heights:
    total_height += height
print(f"Total height = {total_height}")

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"Number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"Average heigh = {average_height}")

