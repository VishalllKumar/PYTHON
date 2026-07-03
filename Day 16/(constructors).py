class Person:

    def __init__(self,name,occupation):   #__init__ is a special method in a class that runs automatically when an object is created, used to initialize object variables.
        self.name = name
        self.occupation = occupation

    def info(self):
        print(f"{self.name} is a {self.occupation}")
name1 = input("enter name: ")
occupation1 = input("enter occupation: ")
name2 = input("enter name: ")
occupation2 = input("enter occupation: ")
name3 = input("enter name: ")
occupation3 = input("enter occupation: ")

a = Person(name1,occupation1)
b = Person(name2,occupation2)
c = Person(name3,occupation3)
a.info()
b.info()
c.info()

# Constructor in OOP :

# A constructor is a special function that initializes object data automatically when the object is created.

# In OOP, constructors are mainly of three types:
# Default Constructor – Automatically created, doesn’t take parameters, sets basic initial values.

# Parameterized Constructor – Takes parameters to set different values for each object.

# Copy Constructor – Creates a new object by copying data from another existing object.


