# This is a Python Program to print all numbers in a range divisible by a given number.


divisor = int(input('enter the number (divisior)'))
n = int(input('enter the range number'))
num = []
for i in range(0, n+1):
    if i % divisor == 0:
        num.append(i)
print(num)

