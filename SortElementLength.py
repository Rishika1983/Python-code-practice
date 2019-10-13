# This is a Python Program to sort a list according to the length of the elements.

A = []
n = int(input('enter number of Elements'))

for i in range(0, n):
    s = input('Enter the element')
    A.append(s)

print('Entered List:', A)

for j in range(0,n):
    for k in range(0,n-j-1):
        if len(A[k]) > len(A[k+1]):
            temp = A[k]
            A[k] = A[k+1]
            A[k+1] = temp

print('Sorted List:', A)

