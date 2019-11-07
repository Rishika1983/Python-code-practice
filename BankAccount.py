# making a class and methods

class BankAccount:

    def __init__(self,owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"{self.owner} new balance is {self.balance} ")

    def withdraw(self,amount):
        if amount > self.balance:
            print(f"{self.owner} don't have enough balance. Your balance is {self.balance} ")
        else:
            self.balance = self.balance - amount
            print(f"{self.owner} new balance is {self.balance} ")


account1 = BankAccount('Jay', 1000)
account1.withdraw(800)
account1.deposit(400)
account1.withdraw(1000)



