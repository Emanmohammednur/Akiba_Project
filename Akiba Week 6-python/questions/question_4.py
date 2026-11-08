class Dog:
    def make_sound(self):
        print("Dog Barks")

class Cat:
    def make_sound(self):
        print("Cat Meows")

class Cow:
    def make_sound(self):
        print("Cow Moos")

dog1 = Dog()
cat1 = Cat()
cow1 = Cow()


dog1.make_sound()
cat1.make_sound()
cow1.make_sound()


# abstract task 
import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width 
        return area


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    
    def calculate_area(self):
        return  math.pi* (self.radius * self.radius)


rectangle1= Rectangle(10,5)

circle1 = Circle(5)

print(rectangle1.calculate_area())
print(circle1.calculate_area())



#Theory Answer

#1. What is polymorphism?

"""Polymorphism means many forms. It allows different objects to use the same method name but perform different actions."""

# 2. What is abstraction?
"""
Abstraction is an OOP principle that hides unnecessary implementation details and shows only essential features to the user.
"""

# 3. What is an abstract class?

"""An abstract class is a parent class that cannot be instantiated directly and can define methods that child classes must implement.
"""

# 4. What does @abstractmethod do?

"""It marks a method that child classes must implement before their objects can be created.
"""
# 5. What happens if a child class does not implement an abstract method?

"""Python raises a TypeError when we try to create an object of that child class.
"""
# 6. What is the difference between abstraction and encapsulation?
"""
- Abstraction: Hides implementation details.
- Encapsulation: Protects data and controls how it is accessed or modified.
"""
# 7. Why do we use ABC?

"""We import ABC from Python's abc module to create abstract classes.
"""
