# This is a Python Program to create a list of of all numbers in a range
# which are perfect squares and the sum of the digits of the number is less than 10.

l = int(input('Enter the lower range'))
u = int(input('Enter the upper range'))

A = [x for x in range(l,u+1) if (int(x**0.5))**2 == x and sum(list(map(int,str(x)))) <10]

print(A)