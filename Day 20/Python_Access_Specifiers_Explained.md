# Access Specifiers in Python

Python does not have strict access specifiers like C++ or Java. Instead,
it follows **naming conventions** to indicate whether a variable or
method is intended to be public, protected, or private.

------------------------------------------------------------------------

# 1. Public Access Specifier

A **public** variable or method can be accessed from anywhere in the
program.

## Example

``` python
class Employee:
    def __init__(self):
        self.name = "Harry"

a = Employee()
print(a.name)
```

### Output

    Harry

### Explanation

-   `self.name` is a **public** instance variable.
-   It can be accessed both inside and outside the class.
-   This is the default behavior in Python.

------------------------------------------------------------------------

# 2. Private Access Specifier

A **private** variable starts with **double underscores (`__`)**.

## Example

``` python
class Student:
    def __init__(self):
        self.__name = "Vishal"

a = Student()
print(a.__name)
```

### Result

    AttributeError

### Why?

When Python sees `__name`, it performs **name mangling**, changing the
actual variable name internally.

Internally, Python stores it as:

``` python
_Student__name
```

This helps prevent accidental access or overriding from outside the
class.

------------------------------------------------------------------------

# 3. Accessing a Private Variable (Name Mangling)

Although private variables cannot be accessed directly, they can still
be accessed using Python's name mangling format.

## Example

``` python
class Employee:
    def __init__(self):
        self.__name = "bhuchal"

a = Employee()

print(a._Employee__name)
```

### Output

    bhuchal

### Explanation

-   Python changes `__name` into `_Employee__name`.
-   This process is called **Name Mangling**.
-   It is intended to avoid accidental access or conflicts, **not** to
    provide true security.

------------------------------------------------------------------------

# 4. Protected Access Specifier

A **protected** variable starts with a **single underscore (`_`)**.

## Example

``` python
class Employee:
    def __init__(self):
        self._salary = 50000

a = Employee()

print(a._salary)
```

### Output

    50000

### Explanation

-   A single underscore (`_`) is **only a naming convention**.
-   It tells other programmers: \> "This member is intended for internal
    use."
-   Python **does not restrict access** to protected members.

------------------------------------------------------------------------

# Public vs Protected vs Private

  ---------------------------------------------------------------------------
  Type        Syntax      Can Access Outside Class?              Purpose
  ----------- ----------- -------------------------------------- ------------
  Public      `name`      ✅ Yes                                 Normal
                                                                 variables
                                                                 and methods

  Protected   `_name`     ✅ Yes (allowed, but discouraged)      Internal use
                                                                 by
                                                                 convention

  Private     `__name`    ❌ Not directly                        Avoid
                                                                 accidental
                                                                 access using
                                                                 name
                                                                 mangling
  ---------------------------------------------------------------------------

------------------------------------------------------------------------

# Important Notes

-   Python follows the philosophy **"We are all consenting adults
    here."**
-   Access specifiers are based mostly on conventions.
-   **Public** → Accessible everywhere.
-   **Protected** → Meant for internal use, but still accessible.
-   **Private** → Uses name mangling (`_ClassName__variable`) to reduce
    accidental access.

------------------------------------------------------------------------

# Interview Tip

**Q: Does Python have true private variables?**

**Answer:**

No. Python does not have true private variables. Double underscores
(`__`) trigger **name mangling**, which discourages direct access but
does not make the variable completely inaccessible.
