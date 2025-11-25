# -*- coding: utf-8 -*-

"""
### 📚 Exercise 3: The prisoner’s dilemma

The prisoner’s dilemma is a common example used in game theory. One example of the game is illustrated in the table below:

<img src="images/dilemma2.jpg" width = "50%" align="center"/>

Write a program that implements the game. The program should do the following:
1. Prompt player A for their choice: Press "1" to stay silent or "2" to confess
2. Prompt player B for their choice: Press "1" to stay silent or "2" to confess
3. Display the outcome of the game, i.e., the prison sentences of player A and B

The program should ensure that the user-supplied inputs are valid ("1" or "2"). If inputs are not valid, display a message stating that the inputs were invalid.
"""

# Dict that maps numbers to choices
d = {
     '1' : 'confess',
     '2' : 'stay silent'
     }


# Print welcome message
print('**********************************')
print("Welcome to the Prisoner's Dilemma.")
print('**********************************')

# Prompt user for inputs
choiceA = input('\nPrisoner A, you are up.\nPress 1 for "confess", press 2 for "stay silent": ')
choiceB = input('\nPrisoner B, you are up.\nPress 1 for "confess", press 2 for "stay silent": ')

# Check that choices are valid
if choiceA in d.keys() and choiceB in d.keys():
    
    # Print choices using dict
    print(f'\nPrisoner A chose to {d[choiceA]} and prisoner B chose to {d[choiceB]}.\n')

    if choiceA == '1' and choiceB == '1':
        print('You both get 2 years.')
        
    elif choiceA == '1' and choiceB == '2':
        print('Prisoner A gets 3 years, prisoner B goes free.')
        
    elif choiceA == '2' and choiceB == '1':
        print('Prisoner A goes free, prisoner B gets 3 years.')
    
    elif choiceA == '2' and choiceB == '2':
        print('You both get 1 year.')
   
# Print that choices are invalid
else:
    print('\nInvalid inputs!')
    print('You can only press "1" or "2"')

