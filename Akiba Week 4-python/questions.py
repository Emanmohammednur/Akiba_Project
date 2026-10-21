## Question 1: Mutable and Immutable Objects

### Difference Between Mutable and Immutable Objects

Mutable objects can be changed after they are created, while immutable objects cannot be changed after they are created.

For example, **lists are mutable**, but **strings are immutable** in Python.

### Python Program



# Mutable object: list
marks = [75, 80, 90]
marks[0] = 85
print("Updated marks:", marks)

# Immutable object: string
name = "Eman"
name[0] = "A"
print("Updated name:", name)


### Output


Updated marks: [85, 80, 90]
TypeError: 'str' object does not support item assignment


### Explanation

The list is mutable, so I can change its first mark from `75` to `85`.

However, a string is immutable, so Python raises a `TypeError` when I try to change the first character of `name` using `name[0] = "A"`.

To create a modified string, I can assign a new string instead:


name = "A" + name[1:]
print("Updated name:", name)



Output:


Updated name: Aman

