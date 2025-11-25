# -*- coding: utf-8 -*-
"""
### 📚 Exercise 4: phonebook

Write a program that creates a phonebook where names and phone numbers are stored.

The program should do the following:
1. Create an empty dictionary to store the names and numbers as key-value pairs
2. Use a `while` loop to prompt the user for name and phone numbers and store them in the dictionary
3. The loop should terminate when the user decides to quit, e.g., press «enter» to quit
4. Use a `for` loop to display the final phonebook to the user
"""

# Initialize an empty dictionary to store the phonebook
phonebook = {}

# Initialize a variable to control the loop
continue_input = True  

while continue_input:
    # Prompt the user for a name
    name = input('Enter a name (or press "enter" to exit): ')

    if name == '':
        continue_input = False  # Set the condition to False to terminate the loop
    else:
        # Prompt the user for a phone number
        phone_number = input(f'Enter the phone number for {name}: ')

        # Add the name and phone number to the phonebook
        phonebook[name] = phone_number

        print(f'Added {name} with phone number {phone_number} to the phonebook.\n')


# Print the final phonebook
print('\nFinal Phonebook:')
for name, number in phonebook.items():
    print(f'{name}: {number}')


