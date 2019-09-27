# Lesser of two even
# Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd.


def lesser_of_two_even(num1,num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        if num1 < num2:
            return num1
        else:
            return num2
    elif num2 > num1:
        return num2
    else:
        return num1


#print(lesser_of_two_even(12,61))

