# Print 1+2+3+...n

n = int(input('Enter the Number'))

x = 0
seriesstr = ''
for i in range(1, n+1):
    x = x + 1
    if i < n:
        addsign = ' + '
    else:
        addsign =''
    seriesstr =seriesstr + str(i) + addsign

print(seriesstr + ' = ' + str(x))