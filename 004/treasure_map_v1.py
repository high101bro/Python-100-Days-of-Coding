#! /usr/bin/env python3

line1 = ['.','.','.']
line2 = ['.','.','.']
line3 = ['.','.','.']
#map = [line1,line2,line3]
print("hiding your treasure: X marks the spot.")
position = input("Where do you want to put the treasure? ex: B2 is dead center ")

column = position[0].lower()
row = position[1].lower()

if column == 'a' and row == '1':
    print(f"Placed X at: a1")
    line1[0] = 'X'
elif column == 'a' and row == '2':
    print(f"Placed X at: a2")
    line1[1] = 'X'
elif column == 'a' and row == '3':
    print(f"Placed X at: a3")
    line1[2] = 'X'
elif column == 'b' and row == '1':
    print(f"Placed X at: b1")
    line2[0] = 'X'
elif column == 'b' and row == '2':
    print(f"Placed X at: b2")
    line2[1] = 'X'
elif column == 'b' and row == '3':
    print(f"Placed X at: b3")
    line2[2] = 'X'
elif column == 'c' and row == '1':
    print(f"Placed X at: c1")
    line3[0] = 'X'
elif column == 'c' and row == '2':
    print(f"Placed X at: c2")
    line3[1] = 'X'
elif column == 'c' and row == '3':
    print(f"Placed X at: c3")
    line3[2] = 'X'

print(f"Columns are A, B, C - Rows are 1, 2, 3")
print(f"{line1}\n{line2}\n{line3}")
