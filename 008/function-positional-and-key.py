#! /usr/bin/env python3

def fullname(last,first):
    print(f"Hello, {first} {last}.")

fullname('Daniel','Komnick')
print(f"The above is backwards...")
fullname(first='Daniel',last='Komnick')
print(f"The above is correct!")