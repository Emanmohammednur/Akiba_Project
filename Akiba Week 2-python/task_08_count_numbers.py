n = int(input("Enter a positive number: "))

even_count = 0
odd_count = 0
total = 0

for number in range(1, n + 1):

    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    total += number

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
print("Sum:", total)