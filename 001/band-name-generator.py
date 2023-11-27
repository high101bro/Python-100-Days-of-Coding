#! /usr/bin/env python3

def main():
    print(f"Welcome to the Band Name Generator!")
    city = input("Where were you born? ")
    pet = input("What was your favorite pet's name? ")
    num = len(city) + len(pet)
    print(f"Too easy, your band's name is: {city} {pet} {num}")

main()
