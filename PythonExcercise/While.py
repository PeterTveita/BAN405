def while_test1():
    number = 23
    running = True

    while running:
        guess = int(input('Enter an integer : '))

        if guess == number:
            print('Congratulations, you guessed it.')
            running = False
        elif guess < number:
            print('No, it is a little higher than that.')
        else:
            print('No, it is a little lower than that.')
    print('Done')

def while_test2():
    number = 0

    while number < 5:
        number += 1
        if number == 3:
            continue
        print(number)
    else:
        print('No longer < 5')
while_test2()