## Question 1: Mutable and Immutable Objects

### Difference Between Mutable and Immutable Objects

Mutable objects can be changed after they are created, while immutable objects cannot be changed after they are created. For example, lists are mutable, but strings are immutable.

### Python Program

```python
# Mutable object: list
marks = [75, 80, 90]
marks[0] = 85
print("Updated marks:", marks)

# Immutable object: string
name = "Eman"
name[0] = "A"
print("Updated name:", name)
```

### Output

```text
Updated marks: [85, 80, 90]
TypeError: 'str' object does not support item assignment
```

### Explanation

The list is mutable, so I can change its first mark from 75 to 85. However, the string is immutable, so Python gives an error when I try to change its first character directly. This shows that lists can be modified, but strings cannot be changed in place.