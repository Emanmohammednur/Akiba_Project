class BankAccount:
    def __init__(self,account_holder, balance):
        self.account_holder = account_holder

        if balance >= 0:
            self.__balance = balance
        else:
            self.__balance = 0
            print("Invalid Starting Balance!")

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be Positive")
        else:
            print("Deposit Successful!")
            self.__balance += amount


    def withdraw(self,amount):
        if amount <= 0:
            print("Amount must be Positive")

        elif amount > self.__balance:
            print("Insufficient Balance")

        else:
            print("Withdraw Successful")
            self.__balance -= amount

    
    def get_balance(self):
        return self.__balance


account1 = BankAccount("Sara", 0)

account1.deposit(500)
account1.withdraw(2000)
account1.deposit(10)
account1.withdraw(100)

print("Final Balance:", account1.get_balance())



#Theory part

#1. What is encapsulation?

"""Encapsulation is an OOP principle that combines data and methods inside a class while controlling how the data is accessed and modified.
"""
# 2. Why do we use private attributes?

"""We use private attributes to protect an object's data from accidental direct modification and ensure it is accessed through controlled methods.
"""
# 3. What is name mangling?

"""Name mangling is Python's automatic renaming of attributes that begin with two leading underscores. It helps prevent accidental access and naming conflicts.
"""
# 4. Difference between public, protected, and private attributes?
-""" Public (name): Can be accessed directly from anywhere.
- Protected (_name): Conventionally intended for internal use and subclasses.
- Private (__name): Triggers name mangling to help prevent accidental direct access."""