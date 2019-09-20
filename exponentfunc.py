# Exponential Function
def raised_to_power(num, power):
    base=num
    for index in range(power):
        if index == 0:
            num = num*1
        else:
            num = num*base
    return num
print(raised_to_power(2, 3))
