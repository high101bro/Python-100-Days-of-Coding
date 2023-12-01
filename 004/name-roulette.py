#! /usr/bin/env python3

import random

name_list = []

def add_name():
    name = input(f"What is the name? ")
    return name_list.append(name)

def remove_name():
    name = input(f"What is the name? ")
    try:
        return name_list.remove(name)
    except:
        return print('That name was not in the list')

def random_name():
    random_choice = random.choice(name_list)
    return print(f"The person chosen is: {random_choice}")

def default():
    return "No match"

def make_choice(choice):
    return {
        '1' : add_name,
        '2' : remove_name,
        '3' : random_name
    }.get(choice, default)()

print(f"Welcome to name roulette! Enter some names and then this script will choose a random one.")

while True:
    menu = """
1   Add a name
2   Remove a name
3   Randomly choose a name
"""
    print(', '.join(name_list))
    print(menu)
    choice = input(f"What do you want to do? ")
    make_choice(choice)
    print('')