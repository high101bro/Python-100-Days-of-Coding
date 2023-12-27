#! /usr/bin/env python3

number = 2

def new_number():
    number = 4

print('The number printed is not 4 because of scope:', number)

######################

def inside():
    stuff = 'table'

try:
    print(stuff)
except:
    print('Stuff does not print table because scope')

######################
    
health = 10

def add_health():
    global health
    health += 2

add_health()
print('Health should be 10 + 2 = 12, because of global scope variable', health)