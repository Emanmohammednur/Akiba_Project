# Python Assignment: Mutability, Object Identity, References, and `del`

## Question 1: Mutable and Immutable Objects

### 1.1 Difference Between Mutable and Immutable Objects

**Mutable objects** can be modified after they are created, while **immutable objects** cannot be modified after creation.

For example:
- **Lists** are mutable.
- **Strings** are immutable.

### 1.2 Python Program

```python
# Mutable object: List
marks = [75, 80, 90]
marks[0] = 85

print("Updated marks:", marks)
# Output: Updated marks: [85, 80, 90]


# Immutable object: String
name = "Eman"
name[0] = "A"  # Raises TypeError
```

### Explanation

The list can be modified by changing its first element. However, strings are immutable, so attempting to change an individual character using indexing raises a `TypeError`.

The string variable `name` is not updated because the assignment fails.

---

## Question 2: References and Object Identity

### 2.1 Python Program

```python
a = [10, 20, 30]
b = a
c = [10, 20, 30]

print(a is b)
print(a is c)
print(a == c)
```

### 2.2 Output

```text
True
False
True
```

### 2.3 Difference Between `is` and `==`

- **`is`** checks whether two references point to the same object.
- **`==`** checks whether two objects are equal in value, according to their equality comparison.

### 2.4 Why Do `a` and `c` Have the Same Values but Different Identities?

The variables `a` and `c` refer to two separate list objects created independently. Although their elements are equal, they do not refer to the same object.

Therefore, `a is c` returns `False`, while `a == c` returns `True`.

---

## Question 3: Shared References and Side Effects

### 3.1 Python Program

```python
numbers = [1, 2, 3]
values = numbers

values.append(4)

print(numbers)
print(values)
```

### 3.2 Output

```text
[1, 2, 3, 4]
[1, 2, 3, 4]
```

### 3.3 Explanation

The variables `numbers` and `values` refer to the same list object. When `values.append(4)` modifies the list, the change is visible through both variables.

This happens because assigning `values = numbers` creates another reference to the existing list rather than creating a new list.

### 3.4 Rewrite the Code to Avoid Changing the Original List

```python
numbers = [1, 2, 3]
values = numbers.copy()

values.append(4)

print(numbers)
print(values)
```

**Output:**

```text
[1, 2, 3]
[1, 2, 3, 4]
```

The `copy()` method creates a new, shallow copy of the list. Therefore, modifying its top-level elements does not change the original list.

---

## Question 4: Function Arguments and Mutability

### 4.1 Python Program

```python
def update_list(items):
    items.append(100)

scores = [50, 60, 70]
update_list(scores)

print(scores)
```

### 4.2 Output

```text
[50, 60, 70, 100]
```

### 4.3 Explanation

When `scores` is passed to `update_list()`, the parameter `items` refers to the same list object as `scores`.

Since lists are mutable, `items.append(100)` modifies the original list. As a result, the change is visible through `scores`.

### 4.4 Modify the Function to Return a New List

```python
def update_list(items):
    new_list = items.copy()
    new_list.append(100)
    return new_list

scores = [50, 60, 70]

updated_scores = update_list(scores)

print(scores)
print(updated_scores)
```

**Output:**

```text
[50, 60, 70]
[50, 60, 70, 100]
```

The function creates a shallow copy of the original list, modifies the copy, and returns it. Therefore, the original list remains unchanged.

---

## Question 5: References and the `del` Statement

### 5.1 Python Program

```python
numbers = [5, 10, 15, 20]
num = numbers

print(numbers)
print(num)

del numbers

print(num)
```

### 5.2 Output

```text
[5, 10, 15, 20]
[5, 10, 15, 20]
[5, 10, 15, 20]
```

### 5.3 What Happens When `del` Is Used?

The `del` statement removes the reference name `numbers` from the current namespace. It does not necessarily destroy the list object itself.

In this example, `num` still refers to the same list, so the object remains accessible.

### 5.4 Does Deleting One Variable Always Destroy the Object?

No. Deleting one variable does not necessarily destroy the object.

If other references still point to the object, it can remain accessible through those references.

### 5.5 What Happens When an Object Is No Longer Referenced?

When an object becomes unreachable, it becomes eligible for garbage collection.

In CPython, objects are commonly reclaimed promptly when their reference count reaches zero. However, garbage collection and memory reclamation can depend on the Python implementation and whether reference cycles exist.

An object becoming eligible for collection does not guarantee that its memory is immediately returned to the operating system.

---

## Conclusion

This assignment demonstrates the following Python concepts:

1. Mutable and immutable objects.
2. Object identity and equality.
3. Shared references and side effects.
4. Mutability when passing arguments to functions.
5. Creating independent list copies.
6. Deleting references and understanding garbage collection.

Understanding these concepts is important for writing reliable Python programs and avoiding unexpected changes to mutable objects.