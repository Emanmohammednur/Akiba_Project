number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))



if number1 == number2 == number3 :
    print("All three numbers are equal.")

elif number1 >= number2 and number1 >= number3:
    print(f"The largest number is {number1}.")

elif number2 >= number1 and number2 >= number3:
    print(f"The largest number is {number2}.")
    
else:
    print(f"The largest number is {number3}.")