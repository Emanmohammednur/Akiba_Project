# Create a Student class with the following requirements:
# Define attributes: name, age, and department.
# Use __init__() to initialize the attributes.
# Create a display_info() method to display the student's information.
# Create three student objects with different information.
# Display the information of all three students.
class Student:
    def __init__(self, name,age,department):
        self.name = name
        self.age = age
        self.department = department

    def display_info(self):
        print(self.name)
        print(self.age)
        print(self.department)

student1  = Student("Sara", 20, "IT")
student2  = Student("Hanah", 22, "Computer Science")
student3  = Student("Ali", 23, "Software Engineering")
student1.display_info()
student2.display_info()
student3.display_info()

