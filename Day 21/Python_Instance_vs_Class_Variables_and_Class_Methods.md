# Python: Instance Variables vs Class Variables & Class Methods

## 1. Instance Variables vs Class Variables

### Class Variables

A **class variable** is shared by **all objects** of a class.

``` python
class Employee:
    companyName = "Apple"
    noOfEmployees = 0
```

-   `companyName` belongs to the class.
-   `noOfEmployees` also belongs to the class.
-   Every object can access them unless it creates its own variable with
    the same name.

------------------------------------------------------------------------

### Instance Variables

Instance variables belong to **each individual object**.

``` python
def __init__(self, name):
    self.name = name
    self.raise_amount = 0.02
```

Here:

-   `self.name` → Different for every employee.
-   `self.raise_amount` → Different for every employee.

Example:

``` python
emp1 = Employee("Harry")
emp2 = Employee("Rohan")
```

-   `emp1.name` = Harry
-   `emp2.name` = Rohan

Both objects have their own copy.

------------------------------------------------------------------------

## Understanding the Constructor

``` python
Employee.noOfEmployees += 1
```

Whenever a new object is created, the class variable increases by 1.

After:

``` python
emp1 = Employee("Harry")
```

`noOfEmployees = 1`

After:

``` python
emp2 = Employee("Rohan")
```

`noOfEmployees = 2`

------------------------------------------------------------------------

## Changing an Instance Variable

``` python
emp1.raise_amount = 0.3
```

Only `emp1` changes.

-   emp1.raise_amount = 0.3
-   emp2.raise_amount = 0.02

------------------------------------------------------------------------

## Creating an Instance Variable with the Same Name

``` python
emp1.companyName = "Apple India"
```

This **does not change the class variable**.

Now:

-   `emp1.companyName` → Apple India (instance variable)
-   `Employee.companyName` → Apple
-   `emp2.companyName` → Apple

Python first checks the object. If the variable is not found there, it
checks the class.

------------------------------------------------------------------------

## Changing the Class Variable

``` python
Employee.companyName = "Google"
```

Now:

-   `Employee.companyName` → Google
-   `emp2.companyName` → Google
-   `emp1.companyName` → Apple India (its own instance variable still
    hides the class variable)

------------------------------------------------------------------------

## showDetails()

``` python
def showDetails(self):
    print(
        f"the name of the Employee is {self.name} "
        f"and the raise amount in {self.noOfEmployees} sized "
        f"{self.companyName} is {self.raise_amount}"
    )
```

Example outputs:

For `emp1`:

    the name of the Employee is Harry and the raise amount in 1 sized Apple India is 0.3

For `emp2`:

    the name of the Employee is Rohan and the raise amount in 2 sized Google is 0.02

------------------------------------------------------------------------

# Class Methods

A **class method** works with the **class itself**, not a particular
object.

Syntax:

``` python
@classmethod
def method_name(cls):
    ...
```

`cls` represents the class, similar to how `self` represents the object.

Example:

``` python
class Employee:
    company = "Apple"

    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany
```

------------------------------------------------------------------------

## Creating an Object

``` python
e1 = Employee()
e1.name = "Harry"
```

Output:

    The name is Harry and company is Apple

------------------------------------------------------------------------

## Calling the Class Method

``` python
e1.changeCompany("Tesla")
```

Internally, Python treats it like:

``` python
Employee.changeCompany("Tesla")
```

Inside the method:

``` python
cls.company = newCompany
```

becomes

``` python
Employee.company = "Tesla"
```

Now every object sees the updated company unless it has its own
`company` instance variable.

Output:

    The name is Harry and company is Tesla
    Tesla

------------------------------------------------------------------------

# Difference Between `self` and `cls`

  self                           cls
  ------------------------------ --------------------------
  Refers to the current object   Refers to the class
  Used in instance methods       Used in class methods
  Accesses instance variables    Accesses class variables

------------------------------------------------------------------------

# Summary

-   **Class variables** are shared by all objects.
-   **Instance variables** belong to individual objects.
-   Changing an instance variable affects only that object.
-   Changing a class variable affects all objects that don't override
    it.
-   `@classmethod` receives `cls` instead of `self` and is used to
    modify or work with class-level data.
