#! /usr/bin/env python3


def prime_checker(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"Prime number")
    else:
        print(f"Not a prime")

n = int(input(f"Enter a number to check if it's prime: "))

prime_checker(number=n)
