def check_minimum_length(password, min_length=8):
    return len(password) >= min_length


def check_uppercase(password):
    return any(char.isupper() for char in password)


def check_lowercase(password):
    return any(char.islower() for char in password)


def check_digits(password):
    return any(char.isdigit() for char in password)


def check_special_characters(password):
    return any(not char.isalnum() for char in password)


def analyze_password(password, min_length=8):
    results = {
        "Minimum length": check_minimum_length(password, min_length),
        "Uppercase letters": check_uppercase(password),
        "Lowercase letters": check_lowercase(password),
        "Digits": check_digits(password),
        "Special characters": check_special_characters(password)
    }

    passed = sum(results.values())
    total = len(results)

    return {
        "requirements": results,
        "passed": passed,
        "total": total,
        "percentage": (passed / total) * 100
    }


def display_report(password, min_length=8):
    report = analyze_password(password, min_length)

    print("\n===== PASSWORD ANALYSIS =====")

    for requirement, status in report["requirements"].items():
        if status:
            print(f"{requirement}: Passed")
        else:
            print(f"{requirement}: Failed")

    print(f"\nRequirements passed: {report['passed']}/{report['total']}")
    print(f"Password score: {report['percentage']:.0f}%")

    if report["passed"] == report["total"]:
        print("Password meets all requirements.")
    else:
        print("Password does not meet all requirements.")


def main():
    test_passwords = [
        "Hello123!",
        "python123",
        "HELLO@123",
        "Ab1!",
        "MySecurePass2026@"
    ]

    for password in test_passwords:
        print(f"\nTesting password: {password}")
        display_report(password)


main()