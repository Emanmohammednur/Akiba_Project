# Theory Questions

## Question 1: Function Design

A function containing 100 lines of code that manages products, processes sales, and generates reports can become difficult to maintain because it performs too many different tasks in one place.

If something goes wrong, it may take a long time to find the problem. Changing one part of the function could also affect other parts of the program.

### 1. Single-purpose functions

A function should ideally perform one specific task. This makes the code easier to understand, read, and maintain.

For example, instead of using one function to manage everything, I would create separate functions for adding products, processing sales, and generating reports.

### 2. Parameters and return values

Parameters allow functions to receive the information they need to perform a task. Return values allow them to send results back to the part of the program that called them.

This makes functions more flexible because they can work with different data instead of depending on fixed values.

### 3. Code reuse

When a program is divided into smaller functions, the same function can be called whenever its task is needed.

This avoids writing the same code repeatedly and makes future changes easier.

### 4. Testing and debugging

Smaller functions are easier to test individually. If a problem occurs, I can identify which function is responsible instead of checking a large block of code.

This makes debugging faster and reduces the chance of introducing new errors.

### 5. How I would divide the program

I would divide the program into the following functions:

- `add_product()`: Adds a new product.
- `get_product()`: Finds a product.
- `process_sale()`: Processes a product sale and updates its quantity.
- `calculate_total_sales()`: Calculates total sales.
- `generate_report()`: Displays the sales report.

### Example of a poorly organized function

```python
def manage_store(products, product, quantity, price):
    products.append(product)

    total = quantity * price

    print("Product:", product)
    print("Total sales:", total)

    return products
```

This function adds a product, calculates sales, and displays a report. It performs several different tasks.

### Improved version

```python
def add_product(products, product):
    products.append(product)
    return products


def calculate_sales(quantity, price):
    return quantity * price


def generate_report(product, total):
    print("Product:", product)
    print("Total sales:", total)


products = []

add_product(products, "Laptop")

total = calculate_sales(2, 500)

generate_report("Laptop", total)
```

Now each function has one main responsibility. This makes the program easier to understand, reuse, test, and maintain.

---

## Question 2: Mutable Data and Function Side Effects

Consider the following code:

```python
def add_item(items, item):
    items.append(item)
    return items


products = ["Pen", "Book"]

result = add_item(products, "Bag")

print(products)
print(result)
```

**Output:**

```text
['Pen', 'Book', 'Bag']
['Pen', 'Book', 'Bag']
```

### 1. Why do both printed results contain the added item?

Both results contain `"Bag"` because lists are mutable objects in Python.

When the `products` list is passed to `add_item()`, the function receives a reference to the same list object.

The `append()` method modifies that existing list by adding `"Bag"` to it.

Therefore, both `products` and `result` refer to the same modified list.

### 2. How do lists behave when passed to functions?

When a list is passed as an argument to a function, the function can access and modify the original list.

For example:

```python
def add_item(items):
    items.append("Bag")


products = ["Pen", "Book"]

add_item(products)

print(products)
```

Output:

```text
['Pen', 'Book', 'Bag']
```

Even though the function does not return anything, the original list has changed.

### 3. Difference between modifying an existing list and returning a new list

Modifying an existing list means changing the original object directly. Methods such as `append()`, `remove()`, and `sort()` can modify a list.

Returning a new list means creating another list without changing the original one.

### 4. When is modifying the original data useful or problematic?

Modifying the original list is useful when we intentionally want to update shared data, such as adding a new product to a shopping cart.

However, it can cause unexpected problems when other parts of the program depend on the original data remaining unchanged.

For example, one function might change a list that another function is still using.

### Example that avoids modifying the original list

We can use the `+` operator to create a new list containing the original items and the new item.

```python
def add_item(items, item):
    new_items = items + [item]
    return new_items


products = ["Pen", "Book"]

result = add_item(products, "Bag")

print(products)
print(result)
```

**Output:**

```text
['Pen', 'Book']
['Pen', 'Book', 'Bag']
```

In this example, the original `products` list remains unchanged, while `result` contains a new list with the added item.

This approach is useful when we want to preserve the original data and avoid unexpected side effects.