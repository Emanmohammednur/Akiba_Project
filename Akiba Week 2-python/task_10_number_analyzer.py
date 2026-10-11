total = 0
even_count = 0
odd_count = 0

for i in range(10):
    number = int(input("Enter a number: "))

    if i == 0:
        largest = number
        smallest = number
    else:
        largest = max(largest, number)
        smallest = min(smallest, number)
    
    total += number

    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

average = total / 10

print("Largest number:", largest)
print("Smallest number:", smallest)
print("Total sum:", total)
print("Average:", average)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)