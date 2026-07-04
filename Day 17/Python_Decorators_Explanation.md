# Python Decorators Explained

## What is a Decorator?

A **decorator** is a function that **adds extra functionality to another
function** without changing the original function's code.

Syntax:

``` python
@decorator_name
def function_name():
    pass
```

This is the same as:

``` python
function_name = decorator_name(function_name)
```

------------------------------------------------------------------------

## Your Code

``` python
def greet(fx):
    def mfx(*args, **kwargs):
        print("good morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello world")

@greet
def add(a, b):
    print(a + b)

hello()
add(1, 2)
```

------------------------------------------------------------------------

# Step-by-Step Explanation

## 1. `greet(fx)`

``` python
def greet(fx):
```

-   `greet` is the **decorator function**.
-   `fx` stores the function being decorated.
-   For `hello()`, `fx` becomes `hello`.
-   For `add()`, `fx` becomes `add`.

------------------------------------------------------------------------

## 2. Inner Function

``` python
def mfx(*args, **kwargs):
```

This function wraps the original function.

It performs three steps:

1.  Prints **"good morning"**
2.  Calls the original function
3.  Prints **"Thanks for using this function"**

------------------------------------------------------------------------

## 3. Before the Original Function

``` python
print("good morning")
```

Runs before the original function.

------------------------------------------------------------------------

## 4. Calling the Original Function

``` python
fx(*args, **kwargs)
```

This executes whichever function was decorated.

Examples:

``` python
hello()
```

becomes

``` python
fx()
```

and

``` python
add(1, 2)
```

becomes

``` python
fx(1, 2)
```

------------------------------------------------------------------------

## 5. After the Original Function

``` python
print("Thanks for using this function")
```

Runs after the original function finishes.

------------------------------------------------------------------------

# Why `*args`?

``` python
*args
```

-   Accepts any number of **positional arguments**.
-   Stored as a **tuple**.

Example:

``` python
def demo(*args):
    print(args)

demo(10, 20, 30)
```

Output:

``` python
(10, 20, 30)
```

Without `*args`, your decorator would fail for functions with
parameters.

------------------------------------------------------------------------

# Why `**kwargs`?

``` python
**kwargs
```

-   Accepts any number of **keyword arguments**.
-   Stored as a **dictionary**.

Example:

``` python
def demo(**kwargs):
    print(kwargs)

demo(name="Vishal", age=19)
```

Output:

``` python
{'name': 'Vishal', 'age': 19}
```

------------------------------------------------------------------------

# Why Use Both?

Using

``` python
def mfx(*args, **kwargs):
```

allows the decorator to work with **any function**, whether it has:

-   No arguments
-   One argument
-   Many positional arguments
-   Keyword arguments

Examples:

``` python
hello()
add(1, 2)
student("Vishal", age=19)
```

All work correctly.

------------------------------------------------------------------------

# What Does `@greet` Do?

``` python
@greet
def hello():
    print("Hello world")
```

Python automatically converts it to:

``` python
def hello():
    print("Hello world")

hello = greet(hello)
```

So calling:

``` python
hello()
```

actually calls `mfx()`.

------------------------------------------------------------------------

# Execution Flow

### `hello()`

    hello()
       ↓
    mfx()
       ↓
    good morning
       ↓
    Hello world
       ↓
    Thanks for using this function

### `add(1, 2)`

    add(1,2)
        ↓
    mfx(1,2)
        ↓
    good morning
        ↓
    fx(1,2)
        ↓
    3
        ↓
    Thanks for using this function

------------------------------------------------------------------------

# Output

``` text
good morning
Hello world
Thanks for using this function

good morning
3
Thanks for using this function
```

------------------------------------------------------------------------

# Summary

-   A decorator modifies or extends another function without changing
    its code.
-   `@greet` replaces the original function with the wrapped version
    (`mfx`).
-   `*args` accepts unlimited positional arguments (tuple).
-   `**kwargs` accepts unlimited keyword arguments (dictionary).
-   `fx(*args, **kwargs)` ensures the decorator works with almost any
    function signature.
