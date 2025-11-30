# -*- coding: utf-8 -*-
"""
### 📚 Exercise 2: Random number generator

Modify the random number generator from the previous notebook to instead draw 
a random *code*.

The program should do the following:
1. Initialize an empty list to store the code in
2. Prompt the user for the length of the code and check that the input is valid (must be a non-negative integer)
3. Use a `for` loop and `randint` from `random` to draw random integers between 0 and 9 and store each number in the list
4. Display the random code to the user
"""

import random

#%% Solution 1: simple for loop + simple print statement

# Print welcome message
print('*' * 47)
print('**** Welcome to the Random Code Generator! ****')
print('*' * 47)
print('This program generates a random code of digits between 0 and 9.\n')

# Prompt user for the length of the code
code_len = input('Enter the length of the code: ')

# Initialize an empty list to store the generated code
code_lst = []

# Check if the user input is a digit
if code_len.isdigit():
    code_len = int(code_len)  # Convert input to an integer

    # Generate random digits and append them to the code list
    for i in range(code_len):
        num = random.randint(0, 9)  # Generate a random digit between 0 and 9
        code_lst.append(num)

    # Print the generated code
    print(f'Your code is: {code_lst}')

else:
    # Handle invalid input
    print('Invalid input. Code length must be a non-negative integer.')


#%% Solution 2: list comprehension + for loop to print code

# Print welcome message
print('*' * 47)
print('**** Welcome to the Random Code Generator! ****')
print('*' * 47)
print('This program generates a random code of digits between 0 and 9.\n')

# Prompt user for the length of the code
code_len = input('Enter the length of the code: ')

# Initialize an empty list to store the generated code
code_lst = []

# Check if the user input is a digit
if code_len.isdigit():
    code_len = int(code_len)  # Convert input to an integer

    # Use list comprehension to generate random digits inside list  
    code_lst = [random.randint(0, 9) for i in range(code_len)]

    # Print the generated code with a for loop
    print('Your code is:', end = ' ')
    for i in code_lst:
        print(i, end = '')  # Use end parameter to print digit side-by-side

else:
    # Handle invalid input
    print('Invalid input. Code length must be a non-negative integer.')
    
    