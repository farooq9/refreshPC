# 1program to calculate the area of a circle
import math
r = float(input('Enter radius: '))
area = math.pi*r**2
print('Area of circle =', area)
print('Area of circle = {:02f}'.format(area))

# output
# Enter radius: 6
# Area of a circle = 113.097335529232
# Area of a circle = 113.097335529232

# 2porgram to test whether a given number is between 1 & 10
x = int(input('Enter a number: '))
if x >= 1 and x<= 10:
    print('You typed', x, 'which is between 1 & 10')
else:
    print('you typed', x, 'which is below 1 or above 10')

# output
# Enter a number: 8
# You typed 8 which is between 1 & 10

# 3program that displays stars in right angled triangle using nested Loop  
for i in range(1, 11):
    for g in range(1, i+1):
        print('*', end= ' ')
    print()

# output
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * * * *
# * * * * * * * *
# * * * * * * * * *
# * * * * * * * * * *

# 4program to display numbers from 1 to 100 in a proper format 
for x in range(1, 11):
    for y in range(1, 11):
        print('{:8}'.format(x*y), end= ' ')
    print()

# output
#        1        2        3        4        5        6        7        8        9       10 
#        2        4        6        8       10       12       14       16       18       20 
#        3        6        9       12       15       18       21       24       27       30
#        4        8       12       16       20       24       28       32       36       40
#        5       10       15       20       25       30       35       40       45       50
#        6       12       18       24       30       36       42       48       54       60
#        7       14       21       28       35       42       49       56       63       70
#        8       16       24       32       40       48       56       64       72       80
#        9       18       27       36       45       54       63       72       81       90
#       10       20       30       40       50       60       70       80       90      100

# 5program to reverse an array using array index 
x = ('i', [10, 20, 30, 40, 50])
n = len(x)
for i in range(n):
    print(x[i], end=' ')

# output

# 6program to accept element in the form of a tuple and display their sum & average
num = eval(input('Enter elements in (): '))
sum = 0
n = len(num)
for i in range(n):
    sum += num(i)
print('Sum of number: ', sum)
print('Average of numbers:', sum/n)

# output

# 7program to create a dictionary from keyboard & display elements
x = {}
print('how many elements?', end=' ')
n = int(input())
for i in range(n):
    print('Enter key:', end=' ')
    k = input()
    print('Enter its value: ', end=' ')
    v = int(input())
    x.update({k:v})
print('The dictionary is: ', x)

# output
# how many elements? 2
# Enter key: hello
# Enter its value:  5
# Enter key: farooq
# Enter its value:  4
# The dictionary is:  {'hello': 5, 'farooq': 4}

# 8program to create list using range()
list1 = range(10)
for i in list1:
    print(i, end=' ')

# output
# 0 1 2 3 4 5 6 7 8 9

# 9program to understand list processing methods 
num = [10, 20, 30, 40, 50]
n = len(num)

print('No. of elements in num: ', n)
num.append(60)
print('num after appending 60: ', num)
num.insert(0, 5)
print('num after inserting 5 at 0th place: ', num)
num.extend(num)
print('num after appending num: ', num)
n = num.count(50)
print('number of times 50 found in the list num: ', n)
num.remove(50)
print('num after removing 50: ', num)
num.pop()
print('num after removing ending element: ', num)
num.sort()
print('num after sorting: ', num)
num.reverse()
print('num after reversing: ', num)

# # output
# No. of elements in num:  5
# num after appending 60:  [10, 20, 30, 40, 50, 60]
# num after inserting 5 at 0th place:  [5, 10, 20, 30, 40, 50, 60]
# num after appending num:  [5, 10, 20, 30, 40, 50, 60, 5, 10, 20, 30, 40, 50, 60]
# number of times 50 found in the list num:  2
# num after removing 50:  [5, 10, 20, 30, 40, 60, 5, 10, 20, 30, 40, 50, 60]
# num after removing ending element:  [5, 10, 20, 30, 40, 60, 5, 10, 20, 30, 40, 50]
# num after sorting:  [5, 5, 10, 10, 20, 20, 30, 30, 40, 40, 50, 60, 5, 5, 10, 10, 20, 20, 30, 30, 40, 40, 50, 60]
# num after reversing:  [60, 50, 40, 40, 30, 30, 20, 20, 10, 10, 5, 5, 60, 50, 40, 40, 30, 30, 20, 20, 10, 10, 5, 5]

# 10A function that accepts two values and finds their sum 
def sum(a, b):
    c = a+b
    print('sum = ', c)
sum(10, 15)
sum(1.5, 10.75)

# output
# sum = 25
# sum = 12.5