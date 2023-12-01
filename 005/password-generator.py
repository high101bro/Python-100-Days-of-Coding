#! /usr/bin/env python3

import random

print(f"Welcome to password generator!")

letters_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters_lower = letters_upper.lower()
letters = []
letters.extend(letters_upper)
letters.extend(letters_lower)
# print(letters)

numbers = list('1234567890')
# print(numbers)

special = list("!@#$%^&*()_+-=[]\{}|;':\",./<>? ")
# print(special)

nr_letters = int(input(f"How many letters would you like in your password? "))
nr_numbers = int(input(f"How many numbers would you like?"))
nr_special = int(input(f"How many special characters would you like?"))

password = ""
for i in range(1, nr_letters + 1):
    password += random.choice(letters)
    # print(password)
for i in range(1, nr_numbers + 1):
    password += random.choice(numbers)
    # print(password)
for i in range(1, nr_special + 1):
    password += random.choice(special)
    # print(password)

# print(password)
shuffle = list(password)
random.shuffle(shuffle)
new_pass = ''.join(shuffle)
print(new_pass)
