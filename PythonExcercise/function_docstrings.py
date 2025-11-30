def print_max(x,y):
    '''Prints the maximum of the two numbers.

    The two values must be integers'''
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is greater')
    else:
        print(y, 'is greater')

print_max(3, 5)
print(print_max.__doc__)

