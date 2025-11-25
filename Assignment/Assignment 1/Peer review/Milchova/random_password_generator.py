"""
This is a program that generates a secure random password based on user input. 
It is built using functions, loops, and conditionals.
No generative AI was used for assistance in writing this code. 
"""

# Import modules
import string
import random

""" Prompt the user until a valid password length (8–16) is entered. """
def password_length():
    while True:
        user_input = input('Enter the desired password length (8-16):')
        if not user_input.isdigit():  # Non-numeric input
            print('Error: Please enter a number.')
            continue

        length = int(user_input)
        if 8 <= length <= 16:
            return length
        elif length < 8:
            print('Error: Password length must be at least 8 characters.')
        else:
            print('Error: Password length cannot exceed 16 characters.')
            

""" Generate a random password that satisfies all requirements. """
def generate_password(length): 
    # Required characters for the password 
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    specials = "!@#$%^&*()-_=+"

    # Pick the first character as a letter
    first_char = random.choice(lowercase + uppercase)

    # Add one of each required character type
    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(specials),
    ]
    
    # Add random characters from all categories until we reach the desired length
    all_chars = lowercase + uppercase + digits + specials
    while len(password_chars) < length - 1:  # since first_char already counts as one character
        password_chars.append(random.choice(all_chars))

    # Shuffle the rest of the characters
    random.shuffle(password_chars)
    
    # Build the final password
    password = first_char + "".join(password_chars)
    return password

""" Final program flow. """
def password_generator():
    # Print welcome message
    print('══════════════════════════════════════════════════')
    print('     Welcome to the Random Password Generator')
    print('══════════════════════════════════════════════════')
    
    # Run the program
    length = password_length()
    password = generate_password(length)
    print(f'Generated password: {password}')
    print('Done! Keep this password safe and private.')

password_generator()