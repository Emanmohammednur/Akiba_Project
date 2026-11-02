class Student:
    school_name = "Akiba Academy"
    def __init__(self, name,score,department):
        self.name = name
        self.score = score
        self.department = department
    def display(self):
        print("Name: ",self.name)
        print("Score: ",self.score)
        print("Department: ",self.department)
        print("School Name: ",self.school_name)
        print("-" * 30)


student1 = Student("Sara", 86, "Computer Science")
student2 = Student("Ali",78,"IT" )
student3 = Student("Liza",91,"Software Engineering")

student2.score = 86

student1.display()
student2.display()
student3.display()


print(student1.name,":",student1.score)
print("-" * 10)
print(student2.name,":",student2.score)
print("-" * 10)
print(student3.name,":",student3.score)


# Class Attribute:
# A variable defined inside a class and shared by all instances.

# Instance Attribute:
# A variable belonging to a specific object.
# Each object maintains its own independent values.

# Why are scores independent?
# Because score is an instance attribute.
# Every Student object stores its own score.
# Updating one object's score does not affect other objects.