import string
import random

def password_generator():
    while True: #Makes the program run until a valid input is detected
        try: #If the input is valid, the program will try this block
            password_input = int(input('''\nPlease enter the desired password length.
It must be between 8 and 16 characters: '''))

            if 8 <= password_input <= 16: #Ensures the password is between 8 and 16 characters

                lower = random.choice(string.ascii_lowercase) #Ensures we have at least one lowercase
                upper = random.choice(string.ascii_uppercase) #Ensures we have at least one uppercase
                digit = random.choice(string.digits) #Ensures we have at least one digit
                special = random.choice(string.punctuation) #Ensures we have at least one special sign
                start_character = random.choice(string.ascii_letters)  #Ensures the password starts with a letter

                password_remaining_amount = password_input - 5 #Calculates the remaining characters after the required parts are added.
                password_pool = string.ascii_letters + string.digits + string.punctuation #Makes a pool of characters for the remaining password
                password_remaining = random.choices(password_pool, k=password_remaining_amount) #Randomly selects 'password remaining amount' from characters in 'password_pool' to generate remaining password

                password_characters = [lower, upper, digit, special] + password_remaining #Ensures the required characters are added before the remaining characters

                random.shuffle(password_characters) #Shuffles the characters, so that the order of the required characters isn't predictable

                password = start_character + ''.join(password_characters) #Ensures the first character of the password is a letter, and appends the rest of the password. ''.join combines the characters to one string.

                print('Your password is:', password)

                return(password) #Gives the function the value

            else: #If the input is less than 8 or larger than 16, this prints
                print('Invalid input: Password length must be between 8 and 16 characters.')

        except ValueError: #If the input is invalid, the program will terminate the try-block, and run this instead
                print('''Invalid input:
Password must be a number, and be between 8 and 16 characters.''')

password_generator() #Calls the function

#I have used AI to explain the different functions in the string and random module, and to explain syntax errors.