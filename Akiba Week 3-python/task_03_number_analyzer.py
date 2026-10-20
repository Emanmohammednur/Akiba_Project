
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def get_divisors(number):
    divisors = []

    if number == 0:
        return divisors

    number = abs(number)

    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)

    return divisors


def sum_of_digits(number):
    number = abs(number)
    total = 0

    while number > 0:
        digit = number % 10
        total += digit
        number //= 10

    return total


def reverse_number(number):
    sign = -1 if number < 0 else 1
    number = abs(number)
    reversed_num = 0

    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number //= 10

    return reversed_num * sign


def analyze_number(number):
    if number == 0:
        even_or_odd = "Even"
    elif number % 2 == 0:
        even_or_odd = "Even"
    else:
        even_or_odd = "Odd"

    return {
        "number": number,
        "even_or_odd": even_or_odd,
        "is_prime": is_prime(number),
        "sum_of_digits": sum_of_digits(number),
        "reversed_number": reverse_number(number),
        "divisors": get_divisors(number)
    }


# Test the program
number = 123
report = analyze_number(number)

print("Number Analysis")
print("----------------")
print("Number:", report["number"])
print("Even or Odd:", report["even_or_odd"])
print("Is Prime:", report["is_prime"])
print("Sum of Digits:", report["sum_of_digits"])
print("Reversed Number:", report["reversed_number"])
print("Divisors:", report["divisors"])
