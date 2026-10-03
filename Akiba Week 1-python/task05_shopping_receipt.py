name = input("Enter Your Name: ")
product = input("Enter Your Product: ")
price = float(input("Enter Product Price: "))
quantity = int(input("Enter Quantity: "))
product2 = input("Enter Second Product: ")
price2 = float(input("Enter Second Product Price: "))
quantity2 = int(input("Enter Second Quantity: "))
print()

total = (price * quantity) + (price2 * quantity2)

print("===============================================")
print("                     RECEIPT                   ")
print("===============================================\n")

print(f"Customer: {name}\n")

print("Product        Price       Qty")
print("--------------------------------------")
print(f"{product:<15}{price:.2f} ETB{'':<7}{quantity}")
print(f"{product2:<15}{price2:.2f} ETB{'':<7}{quantity2}\n")

print(f"Total:         {total} ETB \n")
print("Thank you for shopping!")
print("===============================================")
