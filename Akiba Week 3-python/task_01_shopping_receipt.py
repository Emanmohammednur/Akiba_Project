def calculate_subtotal(items):
    subtotal = 0

    for item in items:
        price = item["price"]
        quantity = item["quantity"]

        if not isinstance(price, (int, float)) or isinstance(price, bool):
            return "Invalid price: price must be a number"

        if not isinstance(quantity, (int, float)) or isinstance(quantity, bool):
            return "Invalid quantity: quantity must be a number"

        if price < 0:
            return "Invalid price: price cannot be negative"

        if quantity < 0:
            return "Invalid quantity: quantity cannot be negative"

        subtotal += price * quantity

    return subtotal


def calculate_discount(subtotal):
    if subtotal < 0:
        return "Invalid subtotal"

    if subtotal < 1000:
        return 0
    elif subtotal < 3000:
        return subtotal * 0.05
    else:
        return subtotal * 0.10


def calculate_tax(amount, tax_rate):
    if not isinstance(amount, (int, float)) or isinstance(amount, bool):
        return "Invalid amount"

    if not isinstance(tax_rate, (int, float)) or isinstance(tax_rate, bool):
        return "Invalid tax rate: tax rate must be a number"

    if amount < 0:
        return "Invalid amount"

    if tax_rate < 0 or tax_rate > 1:
        return "Invalid tax rate: use a rate between 0 and 1"

    return amount * tax_rate


def generate_receipt(items, tax_rate):
    subtotal = calculate_subtotal(items)

    if isinstance(subtotal, str):
        return subtotal

    discount = calculate_discount(subtotal)

    if isinstance(discount, str):
        return discount

    discounted_amount = subtotal - discount

    tax = calculate_tax(discounted_amount, tax_rate)

    if isinstance(tax, str):
        return tax

    final_amount = discounted_amount + tax

    return {
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "final_amount": final_amount
    }

items = [
    {"name": "Notebook", "price": 80, "quantity": 3},
    {"name": "Pen", "price": 15, "quantity": 5}
]
tax_rate = 0.15 
receipt = generate_receipt(items, tax_rate)

if isinstance(receipt, str):
    print("Receipt error:", receipt)

else:
    print("\n===== SHOPPING RECEIPT =====")
    print(f"Subtotal:      {receipt['subtotal']:.2f} Birr")
    print(f"Discount:     -{receipt['discount']:.2f} Birr")
    print(f"Tax:           {receipt['tax']:.2f} Birr")
    print("----------------------------")
    print(f"Final amount:  {receipt['final_amount']:.2f} Birr")
    print("============================")
