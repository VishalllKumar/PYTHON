# # Instance vs class variables:

# class Employee:
#     companyName = "Apple"
#     noOfEmployees = 0

#     def __init__(self,name):
#         self.name = name
#         self.raise_amount = 0.02
#         Employee.noOfEmployees += 1
#     def showDetails(self):
#         print(f"the name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")
# emp1 = Employee("Harry")
# emp1.raise_amount = 0.3
# emp1.companyName = "Apple India"
# emp1.showDetails()
# Employee.companyName = "Google"
# print(Employee.companyName)
# emp2 = Employee("Rohan")
# emp2.showDetails()

# # Class methods in python :
 
# # class Employee:
# #     company = "Apple"
# #     def show(self):
# #         print(f"The name is {self.name} and company is {self.company}")
# #     @classmethod
# #     def changeCompany(cls,newCompany):
# #         cls.company = newCompany
# # e1 = Employee()
# # e1.name = "Harry"
# # e1.show()
# # e1.changeCompany("Tesla")
# # e1.show()
# # print(Employee.company)



















