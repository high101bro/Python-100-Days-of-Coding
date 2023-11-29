#! /usr/bin/env python3

print("Welcome to my rollercoaster!")
height = int(input("How tall are you? "))

if height > 48:
    print(f"You're tall enough! Enjoy the ride.")
elif height == 48:
    print(f"You're barely tall enough. Have fun!")
else:
    print(f"Sorry... you're too short. Go away!")
