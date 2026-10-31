## Project Reflection

### 1. Why does modifying a shared reference affect the original list?

Modifying a shared reference affects the original list because both variables refer to the same list object. Therefore, when I modify the list using one variable, the changes are visible through the other variable as well.

### 2. Why does modifying the copied list not affect the original list?

Modifying the copied list does not affect the original list because `copy()` creates a separate, shallow copy of the list. Therefore, changes to the copied list's top-level elements do not affect the original list.

### 3. What is the difference between equality and identity in Python?

**Equality (`==`)** checks whether two objects have equal values, while **identity (`is`)** checks whether two references point to the same object.

In short:
- `==` means equal values.
- `is` means the same object.
