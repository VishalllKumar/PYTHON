# Python OOP Notes -- Class, Object and `self`

## Code

``` python
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

a.info1(name, occupation, networth)
b.info2(name1, occupation1, networth1)
```

------------------------------------------------------------------------

# Explanation

## 1. Class

A **class** is a blueprint used to create objects.

Here, `Person` is the class.

------------------------------------------------------------------------

## 2. Methods

The class contains two methods:

### `info1()`

Stores and prints details of the first person.

### `info2()`

Stores and prints details of the second person.

Both methods work in the same way; only the variable names are
different.

------------------------------------------------------------------------

## 3. `self`

`self` refers to the **current object**.

Example:

``` python
self.name = name
```

The value entered by the user is stored inside that particular object.

For object `a`:

``` python
a.name
```

For object `b`:

``` python
b.name1
```

Each object stores its own data.

------------------------------------------------------------------------

## 4. User Input

The program asks for:

-   Name
-   Occupation
-   Net Worth

for two different people.

------------------------------------------------------------------------

## 5. Creating Objects

``` python
a = Person()
b = Person()
```

Two different objects are created.

-   `a` → First Person
-   `b` → Second Person

------------------------------------------------------------------------

## 6. Calling Methods

``` python
a.info1(name, occupation, networth)
```

Stores data inside object `a`.

``` python
b.info2(name1, occupation1, networth1)
```

Stores data inside object `b`.

------------------------------------------------------------------------

## Example Output

**Input**

    Enter name: Elon Musk
    Enter occupation: Businessman
    Enter networth: 420

    Enter name1: Virat Kohli
    Enter occupation1: Cricketer
    Enter networth1: 105

**Output**

    Elon Musk is a Businessman with 420 CR networth
    Virat Kohli is a Cricketer with 105 CR networth

------------------------------------------------------------------------

# Important Concepts

### Class

A blueprint for creating objects.

### Object

An instance of a class that stores data and performs actions.

### Method

A function written inside a class.

### `self`

Refers to the current object and is used to access its variables and
methods.

------------------------------------------------------------------------

# Better Version of the Program

Instead of creating two separate methods (`info1` and `info2`), one
method is enough:

``` python
class Person:
    def info(self, name, occupation, networth):
        self.name = name
        self.occupation = occupation
        self.networth = networth
        print(f"{self.name} is a {self.occupation} with {self.networth} CR networth")

a = Person()
b = Person()

a.info("Elon Musk", "Businessman", 420)
b.info("Virat Kohli", "Cricketer", 105)
```

This approach is cleaner and follows good Object-Oriented Programming
(OOP) practices.
