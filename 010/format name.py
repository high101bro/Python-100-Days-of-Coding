#! /usr/bin/env python3

def format_name(first,last):
    name = f"{first.title()} {last.title()}"
    return name

print(
    format_name('dan',"KOMNICK")
)