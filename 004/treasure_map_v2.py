#! /usr/bin/env python3

line1 = ['.','.','.','.','.','.','.','.','.']
line2 = ['.','.','.','.','.','.','.','.','.']
line3 = ['.','.','.','.','.','.','.','.','.']
line4 = ['.','.','.','.','.','.','.','.','.']
line5 = ['.','.','.','.','.','.','.','.','.']
line6 = ['.','.','.','.','.','.','.','.','.']
line7 = ['.','.','.','.','.','.','.','.','.']
line8 = ['.','.','.','.','.','.','.','.','.']
line9 = ['.','.','.','.','.','.','.','.','.']
map = [line1,line2,line3,line4,line5,line6,line7,line8,line9]
print("hiding your treasure: X marks the spot.")
position = input("Where do you want to put the treasure? column == A-I and row == 1-9 ")

letter = position[0].lower()
abc = ['a','b','c','d','e','f','g','h','i']
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[letter_index][number_index] = 'X'

print(f"Columns are A, B, C - Rows are 1, 2, 3")
print(f"{line1}\n{line2}\n{line3}\n{line4}\n{line5}\n{line6}\n{line7}\n{line8}\n{line9}")
