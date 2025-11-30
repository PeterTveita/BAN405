# -*- coding: utf-8 -*-

"""
### 📚 Exercise 1b: Random number generator

Note that the program in Exercise 1a will also crash if the user supplies an 
upper bound that is less than the lower bound. To avoid this, you should modify 
the program so that is also checks that the lower bound is less than the upper bound. 
If that is not the case, then the program should instead display a message stating 
that the lower bound is not less then the upper bound.
"""
    
import random

#%% Alternative 1: nested if-else statements


# Print welcome message
print('*'*49)
print('**** Welcome to the random number generator! ****')
print('*'*49)
print('This program draws a random number between an upper and lower bound.\n')

# Prompt user for upper and lower bounds
lower = input('Enter a lower bound: ')
upper = input('Enter an upper bound: ')

# Check that the user has entered digits only
if lower.lstrip('-').isdigit() and upper.lstrip('-').isdigit():
    
    # Convert inputs to int
    lower = int(lower)
    upper = int(upper)
    
    # Check that the user has entered valid bounds
    if lower > upper:
        print('\nInvalid inputs!')
        print('You must enter a lower bound that is smaller than the upper bound.')
    
    else:
        # Draw and display random number
        rand_num = random.randint(lower, upper)
        print(f'\nYou asked for a random number between {lower} and {upper}.')
        print(f'Your random draw is... {rand_num}!')

# Print invalid inputs
else:
    print('\nInvalid inputs!')
    print('You can only enter non-negative integers.')
    
    
    
#%% Alternative 2: try-except statement


# Print welcome message
print('*'*49)
print('**** Welcome to the random number generator! ****')
print('*'*49)
print('This program draws a random number between an upper and lower bound.\n')

# Prompt user for upper and lower bounds
lower = input('Enter a lower bound: ')
upper = input('Enter an upper bound: ')

# Assume that the user has entered digits only and that the bounds are valid
try:
    # Convert inputs to int
    lower = int(lower)
    upper = int(upper)
    
    # Check that the user has entered valid bounds
    if lower > upper:
        print('\nInvalid inputs!')
        print('You must enter a lower bound that is smaller than the upper bound.')
    
    else:
        # Draw and display random number
        rand_num = random.randint(lower, upper)
        print(f'\nYou asked for a random number between {lower} and {upper}.')
        print(f'Your random draw is... {rand_num}!')
    
# Print invalid inputs if exception (i.e., error) occurs
except:
    print('\nInvalid inputs!')
    print('You can only enter integers.')