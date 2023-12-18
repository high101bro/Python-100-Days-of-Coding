#! /usr/bin/env python3


student_grades = {
    'Nathan': 98,
    'Kaitlyn':85,
    'Amelia':78,
    'James':67,
}
new_grades = {}

for student in student_grades:
    # print(student)
    if   student_grades[student] >= 90:
        new_grades[student] = 'A'
    elif student_grades[student] >= 80:
        new_grades[student] = 'B'
    elif student_grades[student] >= 70:
        new_grades[student] = 'C'
    elif student_grades[student] >= 60:
        new_grades[student] = 'D'
    else:
        new_grades[student] = 'F'

for student in new_grades:
    print(f"{student} has a grade letter of {new_grades[student]}")
