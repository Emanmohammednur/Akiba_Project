def validate_units():
    while True:
        try:
            units = float(input("Enter electricity units consumed: "))

            if units < 0:
                print("Units cannot be negative. Try again.")
            else:
                return units

        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_tier_charges(units):
    first_tier = min(units, 50) * 0.50
    second_tier = min(max(units - 50, 0), 100) * 0.75
    third_tier = max(units - 150, 0) * 1.20

    return first_tier, second_tier, third_tier


def calculate_total_bill(units, service_fee=10):
    first, second, third = calculate_tier_charges(units)

    total = first + second + third + service_fee

    return total


def generate_summary(units, service_fee=10):
    first, second, third = calculate_tier_charges(units)
    total = calculate_total_bill(units, service_fee)

    print("\n===== ELECTRICITY BILL =====")
    print(f"Units consumed: {units:.2f}")
    print(f"First 50 units: {first:.2f} Birr")
    print(f"Next 100 units: {second:.2f} Birr")
    print(f"Above 150 units: {third:.2f} Birr")
    print(f"Service fee: {service_fee:.2f} Birr")
    print("----------------------------")
    print(f"Total bill: {total:.2f} Birr")


def main():
    units = validate_units()
    generate_summary(units)


main()