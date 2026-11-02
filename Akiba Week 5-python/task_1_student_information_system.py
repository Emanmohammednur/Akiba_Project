class Student:
    def __init__(self, name,age,department):
        self.name = name
        self.age = age
        self.department = department

    def display_info(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Department: ",self.department)
        print("-" * 30)

student1  = Student("Sara", 20, "IT")
student2  = Student("Hanah", 22, "Computer Science")
student3  = Student("Ali", 23, "Software Engineering")
student1.display_info()
student2.display_info()
student3.display_info()

