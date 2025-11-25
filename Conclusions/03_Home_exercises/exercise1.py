# -*- coding: utf-8 -*-
"""
### 📚 Exercise 1: For loop versus while loop

In general, it is better to use a `for` loop instead of a `while` loop when 
the number of iterations is known in advance. However, in most cases it is 
possible to use either a `for` loop or a `while` loop to solve the same task.

To demonstrate this, write a program that prompts the user for a positive integer `N`, and then calculate and print the sum of the first `N` natural numbers (i.e., 1 + 2 + 3 + ... + N).

1. Solve this using a `for` loop.
2. Solve the same task using a `while` loop.

For simplicity, the program can ignore checking that the user-suppplied input 
is valid. 
"""

#%% Using a for loop:

N = int(input('Enter a positive integer: '))
total = 0
for i in range(1, N+1):
    total += i
print('Sum is:', total)


#%% Using a while loop:

N = int(input('Enter a positive integer: '))
total = 0
i = 1
while i <= N:
    total += i
    i += 1
print('Sum is:', total)