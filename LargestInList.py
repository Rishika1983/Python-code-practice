# This is a Python Program to find the largest number in a list.

n = int(input('enter the number of elements in list'))
numlist = []
while n > 0:
    num = int(input('enter the number'))
    numlist.append(num)
    n = n-1

print(numlist)
print('Largest Number is: {0}'.format(max(numlist)))
