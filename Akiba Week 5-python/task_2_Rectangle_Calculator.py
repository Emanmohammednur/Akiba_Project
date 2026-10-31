# Task 2: Rectangle Calculator
# Create a Rectangle class with the following requirements:
# Initialize length and width using __init__().
# Create an area() method to calculate the area.
# Create a perimeter() method to calculate the perimeter.
# Create two rectangle objects with different dimensions.
# Display the area and perimeter of each rectangle.


class Rectangle:
    def __init__(self,length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
rectangle1 = Rectangle(10,5)
print(rectangle1.area())
print(rectangle1.perimeter())