# Understanding the Python OOP Code (Constructors)

## Code

``` python
class Person:

    def __init__(self, name, occupation):
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

a = Person(name1, occupation1)
b = Person(name2, occupation2)
c = Person(name3, occupation3)

a.info()
b.info()
c.info()
```

------------------------------------------------------------------------

# Step-by-Step Explanation

## 1. Creating a Class

``` python
class Person:
```

-   `class` is used to create a blueprint for objects.
-   `Person` is the name of the class.
-   Every object created from this class will have the same structure.

------------------------------------------------------------------------

## 2. The Constructor (`__init__`)

``` python
def __init__(self, name, occupation):
```

-   `__init__()` is a **special method** called a **constructor**.
-   It runs **automatically** whenever an object is created.
-   Its job is to initialize (assign) values to the object.

### Parameters

-   `self` → refers to the current object.
-   `name` → receives the person's name.
-   `occupation` → receives the person's occupation.

------------------------------------------------------------------------

## 3. Creating Instance Variables

``` python
self.name = name
self.occupation = occupation
```

These lines store the received values inside the object.

Example:

``` python
a = Person("Vishal", "Student")
```

becomes

``` text
a.name = "Vishal"
a.occupation = "Student"
```

Each object stores its own values independently.

------------------------------------------------------------------------

## 4. Creating a Method

``` python
def info(self):
```

This is a normal method of the class.

``` python
print(f"{self.name} is a {self.occupation}")
```

It prints the information stored in the object.

Example output:

``` text
Vishal is a Student
```

------------------------------------------------------------------------

## 5. Taking User Input

``` python
name1 = input("enter name: ")
occupation1 = input("enter occupation: ")
```

The program asks the user for data.

This is repeated three times so that information for three different
people can be entered.

------------------------------------------------------------------------

## 6. Creating Objects

``` python
a = Person(name1, occupation1)
```

Here an object is created.

Python automatically calls:

``` python
Person.__init__(a, name1, occupation1)
```

The same happens for objects `b` and `c`.

------------------------------------------------------------------------

## 7. Calling Methods

``` python
a.info()
b.info()
c.info()
```

Each object calls the `info()` method and prints its own stored data.

------------------------------------------------------------------------

# Example Run

### Input

``` text
enter name: Vishal
enter occupation: Student
enter name: Rahul
enter occupation: Engineer
enter name: Priya
enter occupation: Doctor
```

### Output

``` text
Vishal is a Student
Rahul is a Engineer
Priya is a Doctor
```

------------------------------------------------------------------------

# Memory Representation

``` text
Person Class
│
├── Object a
│     ├── name = Vishal
│     └── occupation = Student
│
├── Object b
│     ├── name = Rahul
│     └── occupation = Engineer
│
└── Object c
      ├── name = Priya
      └── occupation = Doctor
```

Every object has its own separate data.

------------------------------------------------------------------------

# Constructor in OOP

A constructor is a special method that executes automatically when an
object is created. Its main purpose is to initialize the object's data.

## Types of Constructors

### 1. Default Constructor

-   Takes no extra parameters.
-   Assigns default values.

Example:

``` python
class Person:
    def __init__(self):
        self.name = "Unknown"
```

------------------------------------------------------------------------

### 2. Parameterized Constructor

-   Accepts parameters.
-   Initializes each object with different values.

Example:

``` python
class Person:
    def __init__(self, name):
        self.name = name
```

------------------------------------------------------------------------

### 3. Copy Constructor

-   Creates a new object by copying another object's data.
-   Python has no built-in copy constructor, but it can be implemented
    manually.

Example:

``` python
class Person:
    def __init__(self, other):
        self.name = other.name
```

------------------------------------------------------------------------

# Key Points

-   `class` creates a blueprint.
-   `__init__()` is called automatically when an object is created.
-   `self` refers to the current object.
-   `self.name` and `self.occupation` are **instance variables**.
-   `info()` is an instance method.
-   Every object stores its own independent data.
-   `Person(name, occupation)` automatically invokes the constructor.

This is an example of a **Parameterized Constructor** because values are
passed while creating each object.
