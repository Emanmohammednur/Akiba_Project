# Python Assignment: Mutability, Object Identity, References, and `del`

## Question 1: Mutable and Immutable Objects

### 1.1 Difference Between Mutable and Immutable Objects

Mutable objects can be changed after they are created, while immutable objects cannot be changed after creation.

For example:
- Lists are mutable.
- Strings are immutable.

### 1.2 Python Program

marks = [75, 80, 90]
marks[0] = 85

print("Updated marks:", marks)

name = "Eman"
name[0] = "A"  # Raises TypeError

### Explanation

The list can be changed by updating its first element. However, strings are immutable, so trying to change an individual character using indexing raises a `TypeError`.

The string remains unchanged because the operation fails.


## Question 2: References and Object Identity

### 2.1 Python Program

a = [10, 20, 30]
b = a
c = [10, 20, 30]

print(a is b)
print(a is c)
print(a == c)

### 2.2 Output

True
False
True

### 2.3 Difference Between `is` and `==`

- `is` checks whether two variables refer to the same object.
- `==` checks whether two objects have equal values.

### 2.4 Why Do `a` and `c` Have the Same Values but Different Identities?

The variables `a` and `c` refer to two separate list objects. They contain the same values, but they are not the same object.

Therefore, `a is c` returns `False`, while `a == c` returns `True`.



## Question 3: Shared References and Side Effects

### 3.1 Python Program

numbers = [1, 2, 3]
values = numbers

values.append(4)

print(numbers)
print(values)

### 3.2 Output

[1, 2, 3, 4]
[1, 2, 3, 4]

### 3.3 Explanation

The variables `numbers` and `values` refer to the same list object. When I add `4` using `values.append(4)`, the change is also visible through `numbers`.

This happens because `values = numbers` creates another reference to the same list instead of creating a new list.

### 3.4 Rewrite the Code So That Modifying `values` Does Not Change `numbers`

numbers = [1, 2, 3]
values = numbers.copy()

values.append(4)

print(numbers)
print(values)

### Output


[1, 2, 3]
[1, 2, 3, 4]

The copy() method creates a separate, shallow copy of the list. Changes to the copied list's top-level elements do not affect the original list.


## Question 4: Function Arguments and Mutability

### 4.1 Python Program


def update_list(items):
    items.append(100)

scores = [50, 60, 70]
update_list(scores)

print(scores)

### 4.2 Output

[50, 60, 70, 100]

### 4.3 Explanation

When I pass `scores` to `update_list()`, the parameter `items` refers to the same list object as `scores`.

Since lists are mutable, `items.append(100)` changes the original list. That is why the updated list is displayed when I print `scores`.

### 4.4 Modify the Function to Return a New List

def update_list(items):
    new_list = items.copy()
    new_list.append(100)
    return new_list

scores = [50, 60, 70]

updated_scores = update_list(scores)

print(scores)
print(updated_scores)

### Output

[50, 60, 70]
[50, 60, 70, 100]

The function makes a copy of the original list, adds `100` to the copy, and returns it. This way, the original list stays unchanged.


## Question 5: References and the `del` Statement

### 5.1 Python Program

numbers = [5, 10, 15, 20]
num = numbers

print(numbers)
print(num)

del numbers

print(num)

### 5.2 Output

[5, 10, 15, 20]
[5, 10, 15, 20]
[5, 10, 15, 20]

### 5.3 What Happens When `del` Is Used?

The `del` statement removes the variable name `numbers`. It does not necessarily destroy the list object itself.

In this example, `num` still refers to the same list, so I can still access it using `num`.

### 5.4 Does Deleting One Variable Always Destroy the Object?

No. Deleting one variable does not always destroy the object.

If other references still point to the object, it can remain accessible through those references.

### 5.5 What Happens When an Object Is No Longer Referenced?

When an object is no longer reachable, it becomes eligible for garbage collection.

In CPython, objects are commonly cleaned up when their reference count reaches zero. However, objects involved in reference cycles may need garbage collection.

The memory used by an object is not necessarily returned to the operating system immediately.

---

#reflection
Through this assignment, I learned about:

1. Mutable and immutable objects.
2. Object identity and equality.
3. Shared references and side effects.
4. How mutable objects behave when passed to functions.
5. Creating independent list copies.
6. The `del` statement and garbage collection.

Understanding these concepts helps me write better Python programs and avoid unexpected changes when working with lists and other mutable objects.