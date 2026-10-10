number = int(input("Enter a number: "))

if number < 2:
    print("Not Prime")
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

    # We only check up to the square root because
    # factors come in pairs, so checking further is unnecessary.