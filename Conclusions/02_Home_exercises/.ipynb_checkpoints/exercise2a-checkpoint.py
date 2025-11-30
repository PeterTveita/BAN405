# -*- coding: utf-8 -*-

"""
### 📚 Exercise 2a: Temperature conversion program

Modify the temperature conversion program from the previous notebook to allow 
the user to choose whether to convert temperatures from Celsius or Fahrenheit.

Write a program that does the following:
1. Prompt the user for the selected conversion, e.g.:
   - Press "F" to select F->C or "C" to select C->F
2. Prompt the user for the temperature to convert
3. Convert the temperature using the following formulas:
   - $C = \left(\frac{5}{9}\right) \times (F - 32)$
   - $F = \left(\frac{9}{5}\right) \times C + 32$
4. Display the converted temperature

In addition, the program should ensure that the user selects either "F" or "C". 
If the user selects anything else, then the program should instead display a 
message that states that the user has made an invalid selection.
"""

print('This program will convert temperatures (Fahrenheit/Celsius)')
print('Enter "F" to convert from Fahrenheit to Celsius')
print('Enter "C" to convert from Celsius to Fahrenheit\n')

# Prompt user for selection
choice = input('Enter selection: ')

# Check that selection is valid
if choice.upper() in ('F', 'C'):
    
    # Prompt user for temperature
    temp = input('Enter temperature to convert: ')

    # Check that temperature is a number
    try:
        # Convert temperature to float
        temp = float(temp)   
        
        # Convert Fahrenheit -> Celsius
        if choice.upper() == 'F':
            converted_temp = (temp - 32) * 5 / 9
            print(f'\n{temp} degrees Fahrenheit equals {converted_temp:.1f} degrees Celsius.')

        # Convert Celsius -> Fahrenheit
        else:
            converted_temp = (9 / 5) * temp + 32
            print(f'\n{temp} degrees Celsius equals {converted_temp:.1f} degrees Fahrenheit.')
        
    # Print that temperature is not a number
    except:
        print('\nINVALID INPUT')
        print('Temperature must be a number')
    
# Print that selection is invalid
else:
    print('\nINVALID INPUT')
    print('You must select "F" or "C"')


