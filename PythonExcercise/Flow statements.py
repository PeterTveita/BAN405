def check_number(number):
    if number %2==0:
        print(f'{number} er et partall.')
    else:
        print(f'{number} er et oddetall.')

def loop_down(number):
    original_number = number
    while number >= 2:
        number = number -2
    if number == 0:
        print(f'{original_number} was a even number.')
    else:
        print(f'{original_number} was a odd number.')

def break_loop():
    while True:
        line = input('> ')
        if line == 'done':
            break
        print(line)

def minutes_and_seconds():
    minutes = 42
    seconds = 42
    total_seconds = (minutes*60) + seconds
    print(total_seconds)

def miles():
    kilometers = 10
    miles = kilometers * 0.621371
    print(miles)

def volume_of_sphere1(r):
    volume = (4/3)*3.14*(r**2)
    print(volume)

def volume_of_sphere2():
    r = 5
    volume = (4/3)*3.14*(r**2)
    print(volume)

def price_of_book():
    price = 24.95
    discount = 0.4
    shipping_cost = 3
    additional_shipping_cost = 0.75
    copies = 60
    discounted_price = price * (1-discount)
    book_cost = discounted_price * copies
    total_shipping_cost = shipping_cost + (59*additional_shipping_cost)
    total_cost = book_cost + total_shipping_cost
    print(book_cost)
    print(total_shipping_cost)
    print(total_cost)

def right_justify(s):
    num_spaces = 70 - len(s)
    print(' ' * num_spaces + s) #Adds 70 dashes - 'input' to the line

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_spam():
    print('spam')


def print_beam():
    print('+ - - - -' * 2 + '+')

def print_post():
    print('|         ' * 2 +'|')

def print_beam():
    print('+ - - - - ' * 2 + '+')

def draw_grid():
    print_beam()
    print_post()
    print_post()
    print_post()
    print_post()
    print_beam()
    print_post()
    print_post()
    print_post()
    print_post()
    print_beam()
