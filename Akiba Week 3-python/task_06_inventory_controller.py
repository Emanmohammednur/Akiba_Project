inventory = {}

def add_product(name, price, stock):

    if not name.strip():
        print("Product name cannot be empty.")
        return

    if name in inventory:
        print("Product already exists.")
        return

    if price < 0:
        print("Price cannot be negative.")
        return

    if stock < 0:
        print("Stock cannot be negative.")
        return

    inventory[name] = {
        "price": price,
        "stock": stock
    }

    print(f"{name} added successfully.")


def search_product(name):

    if name in inventory:
        print("Product found:")
        print("Name:", name)
        print("Price:", inventory[name]["price"])
        print("Stock:", inventory[name]["stock"])
    else:
        print("Product not found.")


def update_price(name, new_price):

    if name not in inventory:
        print("Product not found.")
        return

    if new_price < 0:
        print("Price cannot be negative.")
        return

    inventory[name]["price"] = new_price

    print("Price updated successfully.")


def increase_stock(name, quantity):

    if name not in inventory:
        print("Product not found.")
        return

    if quantity < 0:
        print("Quantity cannot be negative.")
        return

    inventory[name]["stock"] += quantity

    print("Stock increased successfully.")


def sell_product(name, quantity):

    if name not in inventory:
        print("Product not found.")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    if quantity > inventory[name]["stock"]:
        print("Not enough stock available.")
        return

    inventory[name]["stock"] -= quantity

    print("Sale completed successfully.")


def total_inventory_value():

    total = 0

    for product in inventory:
        price = inventory[product]["price"]
        stock = inventory[product]["stock"]

        total += price * stock

    print("Total inventory value:", total)


def low_stock_report(threshold=5):

    print("Low Stock Products:")

    for product in inventory:

        if inventory[product]["stock"] < threshold:
            print(
                product,
                "Stock:",
                inventory[product]["stock"]
            )


add_product("Laptop", 50000, 10)
add_product("Mouse", 500, 3)
add_product("Keyboard", 1500, 8)

search_product("Laptop")

update_price("Mouse", 600)

increase_stock("Mouse", 5)

sell_product("Laptop", 2)

total_inventory_value()

low_stock_report()
