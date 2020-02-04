# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

from datetime import date

name = input("Please enter your name.")
age = int(input("Please enter your age"))
copy = int(input("how many copies to print"))
current_year = int( date.today().year)
hundred_year = current_year + (100 - age)
n = 0
while n<copy:
    print ("Hello {0}, you will be hundred in {1} \n ".format(name, hundred_year))
    n = n+1
