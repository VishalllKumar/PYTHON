# Public Access Specifier In Python:
# Variables and methods that can be accessed freely from anywhere without restrictions in a program

#EXAMPLE OF PUBLIC ACCESS SPECIFIERS:
# class Employee:
#     def __init__(self):
#         self.name = "Harry"
# a = Employee()
# print(a.name)     #WE CAN ACCESS NAME FROM OUTSIDE OF FUNCTION.(IT'S CALLED PUBLIC ACCESS SPECIFIER IN PYTHON)


# #PRIVATE ACCESS SPECIFIERS IN PYTHON:
# double underscore in __name tells that the self.__name is private so that no one will able to access that.
# class Student:
#     def __init__(self):
#         self.__name = "Vishal"
# a = Student()
# print(a.__name)


#### IF WE WANT TO ACCESS THE PRIVATE ####
# class Employee:
#     def __init__(self):
#         self.__name = "bhuchal"
# a = Employee()
# # print(a.__name)   #it will not able to acces the private one "_ _" .
# print(a._Employee__name)   # this method called name mangling from this method we can access the private.


#PROTECTED ACCESS MODIFIER:
# to note that the single underscore is just a naming convention and dose not actualy provide any protection or restrict access to the member. the syntax we followed to make any variable protected is to write variable name followed by a single underscore(_) i.e _varName



