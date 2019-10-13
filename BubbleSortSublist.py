# This is a Python Program to sort the list according to the second element in the sublist.

A = [['s',23],['h',15],['j',65],['d',5]]

for i in range(0,len(A)):
    for j in range(0,len(A)-1-i):
        if A[j][1] > A[j+1][1]:
            temp = A[j]
            A[j] =A[j+1]
            A[j+1] = temp

print(A)