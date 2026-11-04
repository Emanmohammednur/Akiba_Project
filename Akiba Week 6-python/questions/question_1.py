class Student:
    def __init__(self,name, student_id, department):
        self.name = name
        self.student_id = student_id
        self.department = department


    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Department: {self.department}")
        print("-" * 30)


    def introduce(self):
        print(
            f"Hello, my name is {self.name}. "
            f"My student ID is {self.student_id}, "
            f"and I study {self.department}."
            )
        print("-" * 30)


student1 = Student("Sara","AK01","IT")
student2 = Student("Ali","AK02","Computer Science")
student3 = Student("Liza","AK03","Software Engineering")


student1.display_info()
student1.introduce()

student2.display_info()
student2.introduce()

student3.display_info()
student3.introduce()


# 1 What is a class in Python?

"""A class in Python is a blueprint or template used to create objects. It defines the attributes (data) and methods (behavior) that its objects can have.
"""

# 2 What is an object?

"""An object is a particular instance of a class. It has its own identity and can store its own data (attributes) and use the methods defined by its class.
"""

#3 What is the purpose of the __init__() method?

"""The __init__() method is a special method that Python automatically calls when a new object is created. It initializes the object's attributes with their starting values.
"""

# 4 What is the difference between an attribute and a method?
"""
An attribute is a variable associated with an object or class that stores data or information. 

A method is a function defined inside a class that describes the behavior or actions its objects can perform."""