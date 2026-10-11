
correct_pin = 1234
attempts = 3

while attempts > 0:
    pin = int(input("Enter your ATM PIN: "))

    if pin == correct_pin:
        print("PIN verified successfully. Welcome!")
        break
    else:
        attempts -= 1
        print("Incorrect PIN.")
        print("Attempts remaining:", attempts)

if attempts == 0:
    print("Access denied. Too many incorrect attempts.")
