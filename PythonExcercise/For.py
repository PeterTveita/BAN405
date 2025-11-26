def test_for():
    successful = True
    for number in range (3):
        print('Attempt')
        if successful:
            print('Successful')
            break
    else:
        print('Attempted 3 times and failed')

def test_for2():
count = 0
for number in range(1,10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f'We have {count} even numbers')
