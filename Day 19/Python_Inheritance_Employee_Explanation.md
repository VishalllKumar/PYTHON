# Python Inheritance Example Explained

## Code

``` python
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"the name of employee: {self.id} is {self.name}")

class programmer(Employee):
    def showLanguage(self):
        print("the default language is python")

e1 = Employee("Rohan Das", 400)
e1.showDetails()

e2 = programmer("Harry", 4100)
e2.showDetails()
e2.showLanguage()
```

------------------------------------------------------------------------

# Explanation

## 1. Parent Class (`Employee`)

``` python
class Employee:
```

This creates a class named **Employee**.

It represents a general employee and contains: - Data (name and id) - A
method to display employee details

------------------------------------------------------------------------

## 2. Constructor (`__init__`)

``` python
def __init__(self, name, id):
```

The constructor runs automatically whenever an object is created.

``` python
self.name = name
self.id = id
```

These lines store the values inside the object.

Example:

``` python
e1 = Employee("Rohan Das", 400)
```

After this:

-   `self.name = "Rohan Das"`
-   `self.id = 400`

------------------------------------------------------------------------

## 3. Method

``` python
def showDetails(self):
```

This method prints the employee information.

``` python
print(f"the name of employee: {self.id} is {self.name}")
```

Output:

    the name of employee: 400 is Rohan Das

------------------------------------------------------------------------

# Child Class (Inheritance)

``` python
class programmer(Employee):
```

`programmer` inherits from `Employee`.

This means it automatically gets: - `__init__()` - `showDetails()`

without writing them again.

------------------------------------------------------------------------

## 5. Child Class Method

``` python
def showLanguage(self):
```

This method exists only in the child class.

``` python
print("the default language is python")
```

------------------------------------------------------------------------

# Creating Objects

## Employee Object

``` python
e1 = Employee("Rohan Das", 400)
```

Memory:

    name = "Rohan Das"
    id = 400

Calling:

``` python
e1.showDetails()
```

Output:

    the name of employee: 400 is Rohan Das

------------------------------------------------------------------------

## Programmer Object

``` python
e2 = programmer("Harry", 4100)
```

Since `programmer` inherits `Employee`, it uses the parent's
constructor.

Memory:

    name = "Harry"
    id = 4100

Calling:

``` python
e2.showDetails()
```

Output:

    the name of employee: 4100 is Harry

Calling:

``` python
e2.showLanguage()
```

Output:

    the default language is python

------------------------------------------------------------------------

# Final Output

``` text
the name of employee: 400 is Rohan Das
the name of employee: 4100 is Harry
the default language is python
```

------------------------------------------------------------------------

# Key Concepts Learned

-   **Class** -- Blueprint for creating objects.
-   **Object** -- Instance of a class.
-   **Constructor (`__init__`)** -- Initializes object data
    automatically.
-   **`self`** -- Refers to the current object.
-   **Inheritance** -- Child class reuses code from the parent class.
-   **Method** -- Function inside a class.
-   **Code Reusability** -- The child class uses the parent's
    constructor and methods without rewriting them.
