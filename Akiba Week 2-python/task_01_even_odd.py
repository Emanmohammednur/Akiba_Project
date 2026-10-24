number = int(input("Enter number: "))

if number == 0 :
    print(f"The number is {number} (even).")

elif number > 0:
    if number % 2 == 0:
        print(f"{number} is positive and even.")
    else:
        print(f"{number} is positive and odd.")
else:
    if number % 2 == 0 :
        print(f"{number} is negative and even.")
    else:
        print(f"{number} is negative and odd.")
    