#The program takes a number n and computes n+nn+nnn

n = int( input('enter your number'))
num = ''
total = 0
for i in range(0,n+1):
    num = num + str(n)
    print (num)
    total = total + int(num)

print(total)