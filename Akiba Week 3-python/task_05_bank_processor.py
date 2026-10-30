
# STEP 1: Opening balance
opening_balance = float(input("Enter opening balance: "))
balance = opening_balance

# Store all successful transactions
history = []


# STEP 2: Deposit money
def deposit(balance, amount):

    if amount <= 0:
        return balance, False

    balance += amount

    return balance, True


# STEP 3: Withdraw money
def withdraw(balance, amount):

    if amount <= 0 or amount > balance:
        return balance, False

    balance -= amount

    return balance, True


# STEP 4: Check current balance
def check_balance(balance):

    print(f"Current Balance: {balance:.2f}")


# STEP 5: Record a successful transaction
def record_transaction(history, transaction_type, amount, balance):

    transaction = {
        "type": transaction_type,
        "amount": amount,
        "balance_after": balance
    }

    history.append(transaction)


# STEP 6: Generate transaction summary
def transaction_summary(history):

    total_deposited = 0
    total_withdrawn = 0

    for transaction in history:

        if transaction["type"] == "deposit":
            total_deposited += transaction["amount"]

        elif transaction["type"] == "withdrawal":
            total_withdrawn += transaction["amount"]

    print("\n========== TRANSACTION SUMMARY ==========")

    print(f"Total Deposited: {total_deposited:.2f}")
    print(f"Total Withdrawn: {total_withdrawn:.2f}")
    print(f"Number of Transactions: {len(history)}")


# STEP 7: Main program
while True:

    print("\n========== BANK MENU ==========")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Transaction Summary")
    print("5. Transaction History")
    print("6. Exit")

    choice = input("Choose an option: ")

    # Deposit
    if choice == "1":

        amount = float(input("Enter deposit amount: "))

        balance, success = deposit(balance, amount)

        if success:
            record_transaction(history, "deposit", amount, balance)
            print("Deposit successful!")
        else:
            print("Invalid deposit amount!")

    # Withdrawal
    elif choice == "2":

        amount = float(input("Enter withdrawal amount: "))

        balance, success = withdraw(balance, amount)

        if success:
            record_transaction(history, "withdrawal", amount, balance)
            print("Withdrawal successful!")
        else:
            print("Invalid amount or insufficient balance!")

    # Check balance
    elif choice == "3":

        check_balance(balance)

    # Transaction summary
    elif choice == "4":

        transaction_summary(history)

    # Transaction history
    elif choice == "5":

        print("\n========== TRANSACTION HISTORY ==========")

        if len(history) == 0:
            print("No transactions yet.")

        else:
            for transaction in history:
                print(transaction)

    # Exit
    elif choice == "6":

        print("\nFinal Balance:", balance)
        print("Thank you for using our banking system!")
        break

    else:
        print("Invalid choice. Please try again.")
