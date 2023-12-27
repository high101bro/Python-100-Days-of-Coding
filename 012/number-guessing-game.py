#! /usr/bin/env python3
import random
from simple_term_menu import TerminalMenu
from random import randint


def make_guess(guess):
    global number_to_guess
    if guess > number_to_guess:
        print(f"Your guess is too high.")
        return False
    elif guess < number_to_guess:
        print(f"Your guess is too low.")
        return False
    elif guess == number_to_guess:
        print(f"Congratulations! You guessed {number_to_guess} correctly!")
        return True
    
levels = ['Easy','Medium','Hard']
difficult_level = TerminalMenu(levels,title="Choose a difficulty level:")
difficult_index = difficult_level.show()
difficult_selection = levels[difficult_index]
if   difficult_selection == 'Easy':
    max_guesses = 10
elif difficult_selection == 'Medium':
    max_guesses = 7
elif difficult_selection == 'Hard':
    max_guesses = 5

number_to_guess = randint(1,100)
number_of_guesses = 0
guessing = True

print(f"I'm thinking of a number for you to guess. You can make {max_guesses} guesses.")

while guessing == True:
    try:
        guess = int(input(f"What is your guess? "))
    except:
        print(f"Please enter an number.")

    guess_correctly = make_guess(guess)
    
    if guess_correctly:
        break

    number_of_guesses += 1
    if number_of_guesses >= max_guesses:
        print(f"You lost! You've made too many guesses.")
        print(f"The number was {number_to_guess}")
        break
