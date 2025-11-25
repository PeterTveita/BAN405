# -*- coding: utf-8 -*-

"""
### 📚 Exercise 1a: Random number generator

Write a Python program that draws a random integer between a lower and upper bound.

The program should do the following:
1. Use the `input` function to prompt the user for two integers: `lower` and `upper`
2. Use `randint` from the `random` module to draw a random integer between the user-supplied bounds (see the function documentation [here](https://docs.python.org/3/library/random.html#random.randint))
3. Display the random number

Note that the program will crash if the user-supplied inputs are not integers. 
To avoid this, the program should check that the user has in fact supplied integers 
for the bounds. If that is not the case, then the program should instead display a 
message stating the inputs must be integers.
"""

from random import randint

# Print welcome message
print('*'*49)
print('**** Welcome to the random number generator! ****')
print('*'*49)
print('This program draws a random number between an upper and lower bound.\n')

# Prompt user for upper and lower bounds
lower = input('Enter a lower bound: ')
upper = input('Enter an upper bound: ')

# Check that the inputs are positive or negative integer
if (lower.lstrip('-').isdigit() and upper.lstrip('-').isdigit()):
    
    # Convert bounds to integers
    lower = int(lower)
    upper = int(upper)

    # Draw and display random number
    rand_num = randint(lower, upper)
    print(f'\nYou asked for a random number between {lower} and {upper}.')
    print(f'Your random draw is... {rand_num}!')

else:
    print('\nInvalid inputs! Both bounds must be integers.')
