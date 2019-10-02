# This is a Python Program to check if a number is a Perfect number.

num = int(input('Enter the number'))
divlst = []
for i in range(1, num):
    if num % i ==0:
        divlst.append(i)

print(divlst)
if sum(divlst) == num:
    print('{} is perfect number'.format(num))
else:
    print('{} is not perfect number'.format(num))