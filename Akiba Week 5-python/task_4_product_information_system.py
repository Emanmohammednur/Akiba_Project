class Product:
    def __init__(self,name,price,quantity):
        self.name  = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Name:{self.name} | Price:{self.price} | Quantity:{self.quantity}"

    def total_value(self):
        return self.price * self.quantity
    
product1 = Product("Notebook",30,2) 
product2 = Product("Pen",10,4)
product3 = Product("Bag",100,2)


print(product1)
print("Total:",product1.total_value())
print("-" * 35)

print(product2)
print("Total:",product2.total_value())
print("-" * 35)

print(product3)
print("Total:",product3.total_value())


# Question: What is the purpose of the __str__() method?

# __str__() is a special method that returns a human-readable string representation of an object.It determines what is displayed when we use print(object).