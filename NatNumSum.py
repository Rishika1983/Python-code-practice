# This is a Python Program to read a number n and print the natural numbers summation pattern.


num = int(input('Enter the number'))

for i in range(1, num+1):
    sumstr = ''
    total = 0
    for j in range(1, i+1):
        total = total + j
        if j < i:
            addsign = ' + '
        else:
            addsign = ''
        sumstr = sumstr + str(j) + addsign
    print(sumstr + ' = ' + str(total))