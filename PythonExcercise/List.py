def list_test1():
    shopping_list = ['mango', 'apple', 'milk', 'carrot', 'banana']

    print('I have', len(shopping_list), 'items on my shopping list')

    print('These items are:')
    for item in shopping_list:
        print(item)

    print('\nI also have to buy rice.')
    shopping_list.append('rice')
    print('My shopping list is now:', shopping_list)

    # Sorting the list
    shopping_list.sort()
    print('\nShopping list is:', shopping_list)

    print('The first item i will buy is:', shopping_list[0])
    olditem = shopping_list[0]
    del shopping_list[0]
    print('\nI bought the', olditem)
    print('My shopping list is now:', shopping_list)


def tuples_test1():
    zoo = ('python','elephant','penguin')
    print('Number of animals in the zoo is', len(zoo))

    new_zoo = ('monkey','camel', zoo)
    print('\nNumber of cages in the new zoo is', len(new_zoo))
    print('\nAll animals in the new zoo are', new_zoo)
    print('\nAnimals brought from the old zoo are', new_zoo[2])
    print('\nThe last animal brought from the old zoo is the', new_zoo[2][2])
    print('\nNumber of animals in the new zoo is',len(new_zoo)-1+len(new_zoo[2]))

def nested_sum():
    nested_list = [[1,2,3], [4,5,6], [7,8,9]]
    total_sum = 0
    for sublist in nested_list:
        total_sum += sum(sublist)
    return total_sum

def cumsum(numbers):
    cumulative_sum_list = []
    current_sum = 0

    for num in numbers:
        current_sum += num
        cumulative_sum_list.append(current_sum)

    return cumulative_sum_list

t = [1,2,3]
result = cumsum(t)
print(f'Original list: {t}')
print(f'Cumulative sum: {result}')



cumsum(t)