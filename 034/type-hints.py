#! /usr/bin/env python3

number: int
decimal: float
word: str

# PyCharm with provide highlighted notifications of these, as they don't match their type hint
number = 'ten'
decimal = 'pie'
word = 10

# Can even use type hints within a function
# The -> is used to inform you of what the function is suppose to output
def can_drive(age: int) -> bool:
    if age > 16:
        return True
    else:
        return False
    
    # The following would provide a notification that the function is returning a string and not boolean
    # return 'yes'
