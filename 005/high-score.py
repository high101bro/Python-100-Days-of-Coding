#! /usr/bin/env python3

student_scores = input(f"Enter the Student scores separated by spaces: ").split()
student = 0
for i in range(0, len(student_scores)):
    student += 1
    student_scores[i] = int(student_scores[i])
    print(f"Student #{student}'s score is {student_scores[i]}")

student = 0
student_highscore = 0
highscore = 0
for i in range(0, len(student_scores)):
    student += 1
    if student_scores[i] > highscore:
        # print(f"student {student} ... {student_scores[i]}")
        highscore = student_scores[i]
        student_highscore = student
print(f"Congratulations! Student #{student_highscore} has the highest score of {highscore}!")
