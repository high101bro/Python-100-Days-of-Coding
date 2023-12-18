#! /usr/bin/env

import random,os

def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
        
def evaluate(guess_count,status,word_to_guesss,message1,message2):
    if guess_count <= 0:
        message1 = 'Game Over'
        message2 = 'Too bad you lost...'
        return message1, message2
    elif status == word_to_guesss:
        message1 = 'Congratulations!'
        message2 = 'You won the game!'
        return message1, message2
    else:
        return message1,message2
    

def hangman_0(status,word_to_guesss,guesses,message1,message2):
    message1, message2 = evaluate(guess_count,status,word_to_guesss,message1,message2)
    hangman = f"""
   _____ 
   |   |     Hangman: {status}
   |         Guesses: {guesses}
   |         
   |         {message1}
   |         {message2}
   |
==========
"""
    return hangman
def hangman_1(status,word_to_guesss,guesses,message1,message2):
    message1, message2 = evaluate(guess_count,status,word_to_guesss,message1,message2)
    hangman = f"""
   _____ 
   |   |     Hangman: {status}
   |   O     Guesses: {guesses}
   |   
   |         {message1}
   |         {message2}
   |
==========
"""
    return hangman
def hangman_2(status,word_to_guesss,guesses,message1,message2):
    message1, message2 = evaluate(guess_count,status,word_to_guesss,message1,message2)
    hangman = f"""
   _____ 
   |   |     Hangman: {status}
   |   O     Guesses: {guesses}
   |   | 
   |         {message1}
   |         {message2}
   |
==========
"""
    return hangman
def hangman_3(status,word_to_guesss,guesses,message1,message2):
    message1, message2 = evaluate(guess_count,status,word_to_guesss,message1,message2)
    hangman = f"""
   _____ 
   |   |     Hangman: {status}
   |   O     Guesses: {guesses}
   |  /|
   |         {message1}
   |         {message2}
   |
==========
"""
    return hangman
def hangman_4(status,word_to_guesss,guesses,message1,message2):
    message1, message2 = evaluate(guess_count,status,word_to_guesss,message1,message2)
    hangman = f"""
   _____ 
   |   |     Hangman: {status}
   |   O     Guesses: {guesses}
   |  /|\ 
   |         {message1}
   |         {message2}
   |
==========
"""
    return hangman
def hangman_5(status,word_to_guesss,guesses,message1,message2):
    message1, message2 = evaluate(guess_count,status,word_to_guesss,message1,message2)
    hangman = f"""
   _____ 
   |   |     Hangman: {status}
   |   O     Guesses: {guesses}
   |  /|\ 
   |   |     {message1}
   |         {message2}
   |
==========
"""
    return hangman
def hangman_6(status,word_to_guesss,guesses,message1,message2):
    message1, message2 = evaluate(guess_count,status,word_to_guesss,message1,message2)
    hangman = f"""
   _____ 
   |   |     Hangman: {status}
   |   O     Guesses: {guesses}
   |  /|\ 
   |   |     {message1}
   |  /      {message2}
   |
==========
"""
    return hangman
def hangman_7(status,word_to_guesss,guesses,message1,message2):
    message1, message2 = evaluate(guess_count,status,word_to_guesss,message1,message2)
    hangman = f"""
   _____ 
   |   |     Hangman: {status}
   |   O     Guesses: {guesses}
   |  /|\  
   |   |     {message1}
   |  / \    {message2}
   |
==========
"""
    return hangman

def hangman(guess_count,status,word_to_guesss,guesses,message1,message2):
    if guess_count >= 7:
        hangman = hangman_0(status,word_to_guesss,', '.join(guesses),'Welcome','Enter a letter')
    if guess_count == 6:
        hangman = hangman_1(status,word_to_guesss,', '.join(guesses),message1,message2)
    if guess_count == 5:
        hangman = hangman_2(status,word_to_guesss,', '.join(guesses),message1,message2)
    if guess_count == 4:
        hangman = hangman_3(status,word_to_guesss,', '.join(guesses),message1,message2)
    if guess_count == 3:
        hangman = hangman_4(status,word_to_guesss,', '.join(guesses),message1,message2)
    if guess_count == 2:
        hangman = hangman_5(status,word_to_guesss,', '.join(guesses),message1,message2)
    if guess_count == 1:
        hangman = hangman_6(status,word_to_guesss,', '.join(guesses),message1,message2)
    if guess_count <= 0:
        hangman = hangman_7(status,word_to_guesss,', '.join(guesses),'Game Over','Too bad you lost...')
    print(hangman)
    if 'Congratulations' in hangman:
        return 'exit'

def display_word(word):
    to_display = []
    for char in word:
        if char in guesses:
            to_display.append(char)
        else:
            to_display.append('_')
    to_display = ''.join(to_display)
    return to_display

words = ['Daniel','Lisa','Nathanael','Kaitlyn','Amelia','James','Steven','Marie','Robert','Nicole','Dian','William','Komnick','Burden','Mark','John','Lovena','Larry','Lonnie','Leonard','Susie','Nicolas','Linsa','Lloyd','Pelayo','Rivernider','Fox','Russel','Francis','Fuentes','Eric']
word_to_guesss = random.choice(words)
guesses = []
guess_count = 7
message1 = ''
message2 = ''

while guess_count > 0:
    clear_screen()
    status = display_word(word_to_guesss)

    result = hangman(guess_count,status,word_to_guesss,guesses,message1,message2)
    if result == 'exit':
        break
    guess = input(f"Guess a single letter: ")
    if guess in guesses:
        print(f"[!] You have already guessed {guess}. Please make another guess.")
    elif len(guess) > 1:
        print(f"[!] Please only enter one character at a time. Please make another guess.")
    else:
        if guess in word_to_guesss:
            print(f"[+] Good job! The letter {guess} is in the word.")

        else:
            print(f"[-] Too bad... The letter {guess} is not in the word.")
            guess_count -= 1
        guesses.append(guess)

clear_screen()
hangman(guess_count,status,word_to_guesss,guesses,message1,message2)

