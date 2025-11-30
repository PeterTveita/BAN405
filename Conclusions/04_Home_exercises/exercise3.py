# -*- coding: utf-8 -*-

def main():
    """
    Converts and displays temperatures between Fahrenheit and Celsius.
    """
    
    # Print program welcome
    print('*********** Temperature Conversion Program ***********')
    print('This program convert temperatures (Fahrenheit/Celsius)')
    print('******************************************************')
    
    # Get scale to convert from
    scale = getScale()
      
    # Get temperature to convert
    temp = getTemp()
          
    # Convert temperature
    converted_temp = tempConversion(temp, scale)
    
    # Display conversion
    if scale == 'F':
        print(f'\n{temp} degrees Fahrenheit equals {converted_temp:.1f} degrees Celsius.')
    else:
        print(f'\n{temp} degrees Celsius equals {converted_temp:.1f} degrees Fahrenheit.')
        
    print('\nThank you for using the Temperature Conversion Progam!')
    
    
def getScale():
    """
    Prompts the user for which scale to convert the temperature from. Input 
    must be "F" or "C". Returns the user-supplied scale.
    """
    
    print('\nEnter "F" to convert from Fahrenheit to Celsius')
    print('Enter "C" to convert from Celsius to Fahrenheit')
    
    # Prompt user for scale to convert from
    while True:
        scale = input('\nEnter selection: ').upper()  # Convert to uppercase
        if scale in ('F', 'C'):
            break  # Break loop if input is "F" or "C"
        else:
            print('Invalid input! Enter "F" or "C".')
    
    return scale
    

def getTemp():
    """
    Prompts the user for a temperature to convert. Input must be a number.
    Returns the user-supplied temperature.
    """
    
    # Prompt user for temperature
    while True:
        try:
            temp = float(input('\nEnter temperature to convert: '))  # Convert to a float
            break  # Break loop if input is a float
        except:
            print('Invalid input! Enter a number.')
                
    return temp


def tempConversion(temp, scale):
    """
    Converts temperatures between Fahrenheit and Celsius given a temperature 
    and scale. Returns the converted temperature.
    """
    
    # Convert temperature from F->C
    if scale == 'F':
        converted_temp = (5/9) * (temp - 32) 
    
    # Convert temperature from C->F
    else:
        converted_temp = (9/5) * temp + 32
        
    return converted_temp



# Note: it is good programming practise to place the function call to the main
# function inside an if-statement to ensure that the program is executed only
# if this is the main file.
if __name__ == '__main__':
    main()
    