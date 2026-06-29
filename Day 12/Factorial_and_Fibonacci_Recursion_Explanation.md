# Python Recursion Examples: Factorial and Fibonacci

## 1. Factorial Program

``` python
def factorial(n):
    if (n == 0) or (n == 1):
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("enter no. : "))
print(factorial(n))
```

### Explanation

-   `def factorial(n):`
    -   Defines a function named `factorial` with one parameter `n`.
-   `if (n == 0) or (n == 1):`
    -   This is the **base case** of recursion.
    -   `0! = 1` and `1! = 1`.
-   `return 1`
    -   Stops the recursive calls and returns `1`.
-   `else:`
    -   Runs when `n` is greater than `1`.
-   `return n * factorial(n - 1)`
    -   Calls the same function with `n-1`.
    -   Multiplies `n` by the factorial of the previous number.

### Example (n = 5)

    factorial(5)
    = 5 × factorial(4)
    = 5 × 4 × factorial(3)
    = 5 × 4 × 3 × factorial(2)
    = 5 × 4 × 3 × 2 × factorial(1)
    = 5 × 4 × 3 × 2 × 1
    = 120

**Output**

    enter no. : 5
    120

------------------------------------------------------------------------

# 2. Fibonacci Program

``` python
def fib(n):
    if (n == 0):
        return 0
    elif (n == 1 or n == 2):
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input("Enter any number"))
for i in range(n):
    print(fib(i), end=" ")
```

## Explanation

-   `def fib(n):`
    -   Creates a recursive function to find the nth Fibonacci number.
-   `if (n == 0):`
    -   Base case: returns `0`.
-   `elif (n == 1 or n == 2):`
    -   Base cases: returns `1`.
-   `return fib(n-1) + fib(n-2)`
    -   Adds the previous two Fibonacci numbers.
-   `for i in range(n):`
    -   Prints Fibonacci numbers from `0` to `n-1`.

### Example (n = 7)

    fib(0) = 0
    fib(1) = 1
    fib(2) = 1
    fib(3) = 2
    fib(4) = 3
    fib(5) = 5
    fib(6) = 8

**Output**

    Enter any number: 7
    0 1 1 2 3 5 8

------------------------------------------------------------------------

# Recursion

Recursion is a technique where a function calls itself until it reaches
a **base case**.

### Steps:

1.  Function is called.
2.  Base case is checked.
3.  If base case is not reached, function calls itself.
4.  When the base case is reached, values are returned back one by one.

## Time Complexity

### Factorial

-   Time: **O(n)**
-   Space: **O(n)** (recursive call stack)

### Fibonacci (Recursive)

-   Time: **O(2\^n)** (slow because of repeated calculations)
-   Space: **O(n)**

> **Note:** The recursive Fibonacci method is easy to understand but
> inefficient for large values of `n`.
