class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be Positive!")
        else:
            print("Deposit successful!")
            self.balance += amount
    def withdraw(self,amount):
        if amount <= 0 :
            print("Amount must be Positive!")
        elif amount > self.balance:
            print("Insufficient Balance!")
        else:
            print("Withdrawal Successful!")
            self.balance -= amount
    def display_balance(self):
        print(f"Account Owner: {self.owner}")
        print(f"Current Balance: {self.balance} birr")    
        print("-" * 30)

account1 = BankAccount("Sara", 1000)
account2 = BankAccount("Ali", 800)

account1.deposit(100)
account1.withdraw(-500)
account1.withdraw(1700)
account1.display_balance()


account2.deposit(200)
account2.withdraw(400)
account2.withdraw(100)
account2.display_balance()
