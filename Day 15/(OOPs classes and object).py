class Person:
    def info1(self,name,occupation,networth):
        self.name = name
        self.occupation = occupation
        self.networth = networth
        print(f"{self.name} is a {self.occupation} with {self.networth} CR networth")
    def info2(self,name1,occupation1,networth1):
        self.name1 = name1
        self.occupation1 = occupation1
        self.networth1 = networth1
        print(f"{self.name1} is a {self.occupation1} with {self.networth1} CR networth")

name = input("Enter name: ")
occupation = input("Enter occupation: ")
networth = int(input("Enter networth: "))
name1 = input("Enter name1: ")
occupation1 = input("Enter occupation1: ")
networth1 = int(input("Enter networth1: "))
a = Person()
b = Person()
a.info1(name,occupation,networth)
b.info2(name1,occupation1,networth1)

# Self parameter:
# self refers to the object itself, used to access its data and functions inside class.

# Class :
# A class is a simple design or blueprint used to create similar type objects.

# Object :
# An object is something created from a class that holds data and performs actions.











