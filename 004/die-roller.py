#! /usr/bin/env python3

import random


def roll_die(s):
    return random.randint(1,s)

while True:
    try:
        side_number = int(input(f"Input a number of sides: "))
        print(f"You rolled a: {roll_die(side_number)}")
    except:
        print('You need to provide an integer.')        
    print('')
