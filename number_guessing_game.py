# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 02:26:43 2024

@author: SambesiweSli
"""

import random

print('''Hi, Welcome to my game. Here we will be playing a guessing game.
      \nYou have 7 attempts to guess the correct number.
      \nLET'S GET STARTED''')

guess = random.randrange(100)

attempts = 7

guess_counter = 0

while guess_counter < attempts:
    
    guess_counter += 1
    my_guess = int(input("Please guess the number : "))
    
    if my_guess == guess:
        print(f'''YOU GUESSED CORRECT! The number is {guess} and it took
              you {guess_counter} attempts''')
        break
    
    elif guess_counter >=  attempts and my_guess != guess:
        print(f'''OOPS! sorry, better luck next time. The number you
              were supposed to guess is {guess}''')
              
    elif my_guess > guess:
        print("TOO HIGH! try a lower number.")
        
    elif my_guess < guess:
        print("TOO LOW! try a higher number.")