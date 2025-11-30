# -*- coding: utf-8 -*-

"""
### 📚 Exercise 2b: Temperature conversion program

Modify the temperature conversion program from Exercise 2b to also convert 
temperatures in Kelvin using the following formulas for conversion:
- $C = \left(\frac{5}{9}\right) \times (F - 32)$
- $K = \left(\frac{5}{9}\right) \times (F - 32) + 273.15$
- $F = \left(\frac{9}{5}\right) \times C + 32$
- $K = C + 273.15$
- $F = \left(\frac{9}{5}\right) \times (K - 273.15) + 32$
- $C = K - 273.15$


Write a program that does the following:
1. Prompt the user for a temperature to convert
2. Prompt the user for the scale to convert from (F, C or K)
3. Prompt the user for the scale to convert to (F, C or K)
4. Display the converted temperature

For simplicity, the program can ignore checking that the user-supplied inputs are valid.
"""

# Dict to map selection to temperature scale
d = {
     'F' : 'Fahrenheit',
     'C' : 'Celsius',
     'K' : 'Kelvin'
     }


print('This program converts temperatures between Fahrenheit/Celsius/Kelvin\n')

# Prompt user for temperature and convert to float
temp = float(input('Enter temperature: '))

# Prompt user for temperature scale to convert from and to
fromScale = input('Is this in (F)ahrenheit, (C)elsius or (K)elvin?: ').upper()
toScale = input('Convert to (F)ahrenheit, (C)elsius or (K)elvin?: ').upper()

# Converting from Fahrenheit...
if fromScale == 'F':
    # ...to Celsius
    if toScale == 'C':
        converted_temp = (temp - 32) * 5/9
    # ...to Kelvin
    elif toScale == 'K':
        converted_temp = (temp - 32) * 5/9 + 273.15
    # ...to Fahrenheit
    else:
        converted_temp = temp
        
# Converting from Celsius...
elif fromScale == 'C':
    # ...to Fahrneheit
    if toScale == 'F':
        converted_temp = (9/5 * temp) + 32
    # ...to Kelvin
    elif toScale == 'K':
        converted_temp = temp + 273.15
    # ...to Celsius
    else:
        converted_temp = temp
        
# Converting from Kelvin...   
else:
    # ...to Fahrenheit
    if toScale == 'F':
        converted_temp = (9/5 * (temp - 273.15)) + 32
    # ...to Celsius
    elif toScale == 'C':
        converted_temp = temp - 273.15
    # ...to Kelvin
    else:
        converted_temp = temp 
    
# Print conversion
print(f'{temp:.1f} degrees {d[fromScale]} equals {converted_temp:.1f} degrees {d[toScale]}')

