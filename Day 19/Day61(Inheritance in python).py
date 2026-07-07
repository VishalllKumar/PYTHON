class Employee:
    def __init__(self,name,id):
        self.name = name 
        self.id = id
                                       
    def showDetails(self):
        print(f"the name of employee: {self.id} is {self.name}")

class programmer(Employee):
    def showLanguage(self):
        print("the default language is python")

e1 = Employee("Rohan Das" , 400)
e1.showDetails()
e2 = programmer("Harry",4100)
e2.showDetails()
e2.showLanguage()
















