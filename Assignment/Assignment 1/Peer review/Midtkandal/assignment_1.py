import string
import random

# Takes an integer length and returns a random password string of that length
def generate_random_password(length: int) -> str: 
    """
    Password requirements:
    - be between 8 and 16 characters long (inclusive)
    - contain at least one uppercase letter
    - contain at least one lowercase letter
    - contain at least one digit
    - contain at least one special character (!@#$%^&*()-_=+)
    - cannot begin with a digit or special character
    """
    
    # Define character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = "!@#$%^&*()-_=+"
    all_characters = uppercase + lowercase + digits + special_characters
    
    # Ensure the password meets all requirements
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with random choices from all characters
    while len(password) < length:
        password.append(random.choice(all_characters))

    # Shuffle the password list to ensure randomness
    random.shuffle(password)
    
    # Ensure the first character is not a digit or special character
    # If it is, reshuffle until it's not
    while password[0] in digits + special_characters:
        random.shuffle(password)    

    # Join the list into a string and return
    return ''.join(password)

def main():
    # Boolean to make a loop until valid input is given
    pass_length_valid = False
    while not pass_length_valid: # Said loop
        try:
            pass_length = int(input("Enter the desired password length (8-16): ")) # Get user input
            if 8 <= pass_length <= 16: # If the input is valid, break the loop
                pass_length_valid = True
            else:
                print("Error: Password length must be between 8 and 16 characters.") # Else, print an error message and loop again
        except ValueError:
            print("Error: Please enter a valid number.") # Catch non-integer inputs and print an error message, to prevent crashing 
    
    print("Generated password:", generate_random_password(pass_length)) # Print the generated password
    
main()