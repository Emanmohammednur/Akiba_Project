name = input("Enter Employee Name: ")
basic_salary = int(input("Enter Basic Salary: "))
transport_allowance = int(input("Enter Transport Allowance: "))
food_allowance = int(input("Enter Food Allowance: "))

gross_salary = basic_salary + transport_allowance + food_allowance

print("===================================================")
print("                   EMPLOYEE PAYSLIP                ")
print("===================================================\n")

print(f"Employee: {name}\n")
print(f"Basic Salary:          {basic_salary:,} ETB")
print(f"Transport Allowance:    {transport_allowance:,} ETB")
print(f"Food Allowance:         {food_allowance:,} ETB")
print("--------------------------------------------")
print(f"Gross Salary:           {gross_salary:,} ETB")
print("===================================================")
