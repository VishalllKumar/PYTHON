# Python Functions - Code Explanation

## 1. Function Syntax

``` python
def function_name(parameters):
    # logic / code
    return

function_name(arguments)
```

-   **def** is used to create a function.
-   **Function name** should describe what the function does.
-   **Parameters** are variables that receive values.
-   **Arguments** are the actual values passed while calling the
    function.
-   A function can have any number of parameters and arguments.

------------------------------------------------------------------------

## 2. `calGmean(a, b)`

``` python
def calGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

calGmean(7, 8)
```

### Explanation

-   Takes two numbers (`a` and `b`).
-   Calculates `(a*b)/(a+b)`.
-   Stores the result in `mean`.
-   Prints the result.

For `a = 7` and `b = 8`:

    mean = (7 × 8) / (7 + 8)
         = 56 / 15
         = 3.7333333333333334

**Output**

    3.7333333333333334

------------------------------------------------------------------------

## 3. `isgreater(a, b)`

``` python
def isgreater(a,b):
    if (a>b):
        print("first no. is greater.")
    else:
        print("secound no. is greater.")

isgreater(5,10)
```

### Explanation

-   Checks whether the first number is greater than the second.
-   If true, prints **"first no. is greater."**
-   Otherwise prints **"secound no. is greater."**

For `5` and `10`:

    5 > 10 → False

**Output**

    secound no. is greater.

------------------------------------------------------------------------

## 4. `islower(a, b)`

``` python
def islower(a,b):
    if (a<b):
        print("first no. is smaller.")
    else:
        print("secound no. is greater.")

islower(1,5)
```

### Explanation

-   Checks whether the first number is smaller than the second.
-   If true, prints **"first no. is smaller."**
-   Otherwise prints **"secound no. is greater."**

For `1` and `5`:

    1 < 5 → True

**Output**

    first no. is smaller.

------------------------------------------------------------------------

## 5. Default Arguments

``` python
def average(a,b=8):
    print((a+b)/2)

average(4)
```

### Explanation

-   `a` is a **required argument**.
-   `b=8` is a **default argument**.
-   If `b` is not provided, Python automatically uses `8`.

Function call:

``` python
average(4)
```

Python treats it as:

``` python
average(4, 8)
```

Calculation:

    (4 + 8) / 2 = 6.0

**Output**

    6.0

You can also override the default value:

``` python
average(4,10)
```

Output:

    7.0

------------------------------------------------------------------------

# Key Terms

  Term                Meaning
  ------------------- ----------------------------------------
  Function            A reusable block of code
  Parameter           Variable in function definition
  Argument            Actual value passed to a function
  Required Argument   Must be supplied during function call
  Default Argument    Has a predefined value if not provided

------------------------------------------------------------------------

# Final Outputs

``` text
3.7333333333333334
secound no. is greater.
first no. is smaller.
6.0
```
