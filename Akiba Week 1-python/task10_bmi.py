name = input("Enter Name: ")

weight = float(input("Enter Weight in Kilogram (kg): "))
height = float(input("Enter Height in meter (m): "))

# Calculate BMI (weight in kg divided by height in meters squared)
BMI = weight / (height * height)

print("================================================")
print("                   BMI REPORT                   ")
print("================================================\n")

print(f"Name: {name}")
print(f"Weight: {weight} kg")
print(f"Height: {height:.2f} m\n")
print(f"BMI: {BMI:.2f}")

print("================================================")