class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: {self.salary}")


class Manager(Employee):
        def __init__(self, name, salary,department):
            super().__init__(name,salary)
            self.department = department

        def display_info(self):
            print("Manager Name:",self.name)
            print("Manager Salary:",self.salary)
            print("Manager Department:",self.department)
    


class Developer(Employee):
        def __init__(self, name, salary,programming_language):
            super().__init__(name,salary)
            self.programming_language = programming_language

        def display_info(self):
            print("Developer Name:",self.name)
            print("Developer Salary:",self.salary)
            print("Developer Programming Language:",self.programming_language)


employee1 = Employee("Sara",20000)

manager1 = Manager("Ali", 50000,"IT")

developer1 = Developer("Liza",40000,"Python")



employee1.display_info()
print("-----------------------------------")

manager1.display_info()
print("-----------------------------------")

developer1.display_info()
print("-----------------------------------")



#Theory Answers

#1. What is inheritance?

"""Inheritance is an OOP concept that allows a child class to acquire attributes and methods from a parent class.
"""
#2. What is the difference between a parent class and a child class?

"""
A parent class provides attributes and methods to other classes, while a child class inherits and can extend or modify them.
"""

#3. What is method overriding?
"""
Method overriding occurs when a child class defines its own implementation of a method that already exists in its parent class.
"""
#4. What is the purpose of super()?

"""super() allows a child class to call methods from its parent class, commonly the parent constructor to initialize inherited attributes.
"""
#5. What is the difference between single and multiple inheritance?

"""
Single inheritance means a child class inherits from one parent class, while multiple inheritance means a child class inherits from two or more parent classes."""
