# Python Getter and Setter Explained

## What is `@property` (Getter)?

A **getter** lets you access a method like an attribute (without
parentheses).

Instead of writing:

``` python
obj.ten_value()
```

you can write:

``` python
obj.ten_value
```

The `@property` decorator makes this possible.

------------------------------------------------------------------------

## Getter Example

``` python
class Myclass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def ten_value(self):
        return 10 * self._value

obj = Myclass(10)
print(obj.ten_value)
obj.show()
```

### Step-by-step

### 1. Object Creation

``` python
obj = Myclass(10)
```

The constructor (`__init__`) runs automatically.

    self._value = 10

Current value:

    _value = 10

------------------------------------------------------------------------

### 2. Accessing the Property

``` python
print(obj.ten_value)
```

Python automatically calls:

``` python
ten_value(self)
```

which returns:

``` python
10 * self._value
```

Calculation:

    10 × 10 = 100

Output:

    100

Notice there are **no parentheses** because it is a property.

------------------------------------------------------------------------

### 3. Calling `show()`

``` python
obj.show()
```

prints

    Value is 10

The original `_value` is unchanged.

Output:

    100
    Value is 10

------------------------------------------------------------------------

# What is a Setter?

A **setter** allows you to change a value using attribute assignment.

Instead of writing a method like:

``` python
obj.set_value(50)
```

you can simply write:

``` python
obj.ten_value = 50
```

Python automatically calls the setter function.

------------------------------------------------------------------------

## Setter Example

``` python
class Myclass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def ten_value(self):
        return 10 * self._value

    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value / 10

obj = Myclass(10)
obj.ten_value = 76
print(obj.ten_value)
obj.show()
```

------------------------------------------------------------------------

## What Happens Here?

### Initial object

    _value = 10

------------------------------------------------------------------------

### Assignment

``` python
obj.ten_value = 76
```

Python actually executes:

``` python
ten_value(self, 76)
```

Inside the setter:

``` python
self._value = new_value / 10
```

Calculation:

    76 / 10 = 7.6

Now:

    _value = 7.6

------------------------------------------------------------------------

### Printing

``` python
print(obj.ten_value)
```

Getter runs automatically:

``` python
10 * 7.6
```

Result:

    76.0

------------------------------------------------------------------------

### Calling `show()`

``` python
obj.show()
```

prints

    Value is 7.6

Final output:

    76.0
    Value is 7.6

------------------------------------------------------------------------

# Why divide by 10 in the Setter?

The getter returns:

``` python
10 * _value
```

So the setter stores the reverse:

``` python
_value = new_value / 10
```

This keeps the getter and setter consistent.

Example:

    obj.ten_value = 200

    Setter:
    _value = 200 / 10 = 20

    Getter:
    10 × 20 = 200

------------------------------------------------------------------------

# Flow Diagram

    Object Created
          │
          ▼
    _value = 10
          │
          ▼
    Getter
    obj.ten_value
          │
          ▼
    10 × 10 = 100

    -------------------------

    obj.ten_value = 76
          │
          ▼
    Setter
    _value = 76 / 10
          │
          ▼
    _value = 7.6
          │
          ▼
    Getter
    10 × 7.6 = 76

------------------------------------------------------------------------

# Key Points

-   `@property` creates a **getter**.
-   A getter lets you access a method like an attribute.
-   `@property_name.setter` creates a **setter**.
-   A setter runs automatically when you assign a value.
-   In this example, the getter multiplies by 10 and the setter divides
    by 10 so both operations remain consistent.
