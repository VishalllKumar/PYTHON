# Explanation of Python if-else Examples

## Example 1: Age Checker

``` python
a = int(input("Enter Your Age: "))
print("Your Age is: ", a)
if (a >= 18):
    print("you can drive")
else:
    print("you cannot drive")
```

**Explanation:**\
- The program takes the user's age as input.\
- If the age is **18 or above**, it prints *"you can drive"*.\
- Otherwise, it prints *"you cannot drive"*.

------------------------------------------------------------------------

## Example 2: Apple Budget Checker

``` python
applePrice = 210
budget = int(input("Enter Budget:"))
if (applePrice <= budget):
    print("Alexa, add 1 kg apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")
```

**Explanation:**\
- Apple price is fixed at **210**.\
- The program asks the user for their budget.\
- If the budget is **greater than or equal to 210**, Alexa adds apples
to the cart.\
- Otherwise, Alexa does not add apples.

------------------------------------------------------------------------

## Example 3: Number Categorizer

``` python
num = int(input("Enter the value of num: "))
if (num < 0):
    print("Number is negative.")
elif (num == 0):
    print("Number is zero.")
else:
    print("Number is even.")
print("I am happy now :)")
```

**Explanation:**\
- The user enters a number.\
- If the number is **less than 0**, it prints *negative*.\
- If the number is **0**, it prints *zero*.\
- Otherwise, it assumes the number is **positive/even** and prints
*Number is even*.\
- Finally, it prints *"I am happy now :)"* regardless of the conditions.

------------------------------------------------------------------------
