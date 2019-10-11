# This is a Python Program to put the even and odd elements in a list into two different lists.


n = int(input('enter the number of elements in list'))
numlist = []
EvenList = []
OddList = []
while n > 0:
    num = int(input('enter the number'))
    numlist.append(num)
    n = n-1

EvenList = [a for a in numlist if a % 2 == 0]
print('Even list is:{0} '.format(EvenList))
OddList = [a for a in numlist if a % 2 != 0]
print('Odd list is:{0} '.format(OddList))

