# Python Operators and Simple Calculator

This project demonstrates the use of various Python operators and implements a simple calculator using arithmetic operators.

---

## 1. Python Operators Covered

### (i) Arithmetic Operators
These operators perform basic mathematical operations:

| Operator | Description                        | Example       | Output |
|----------|------------------------------------|---------------|--------|
| `+`      | Addition                            | `5 + 6`       | `11`   |
| `-`      | Subtraction                         | `15 - 6`      | `9`    |
| `*`      | Multiplication                      | `15 * 6`      | `90`   |
| `/`      | Division (returns exact float)      | `15 / 6`      | `2.5`  |
| `//`     | Floor division (quotient only)      | `15 // 6`     | `2`    |
| `%`      | Modulus (remainder)                 | `15 % 6`      | `3`    |
| `**`     | Exponentiation                      | `5 ** 3`      | `125`  |

---

## 2. Simple Calculator Code

The calculator takes **two numbers** and an **operator** from the user, and performs the corresponding operation.

```python
# Input two numbers
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))

# Input operator
c = input("Choose Operator(+,-,*,**,/,//,%) : ")

# Perform operation based on input
if c == '+':
    print(n1 + n2)
elif c == '-':
    print(n1 - n2)
elif c == '*':
    print(n1 * n2)
elif c == '**':
    print(n1 ** n2)
elif c == '//':
    print(n1 // n2)
elif c == '/':
    print(n1 / n2)
elif c == '%':
    print(n1 % n2)
else:
    print("!Invalid Operator!")
```

---

### 3. How the Calculator Works

1. **Input Numbers**:  
   The program asks the user to enter two numbers (`n1` and `n2`) using `input()` and converts them into integers using `int()`.

2. **Input Operator**:  
   The program asks the user to choose an arithmetic operator as a string (`c`).

3. **Perform Operation**:  
   - The `if-elif-else` structure checks which operator the user entered.  
   - It performs the corresponding operation and prints the result.  
   - If the operator is invalid, it prints `!Invalid Operator!`.

---

### 4. Sample Run

**Input:**  
```
Enter first number : 10
Enter second number : 5
Choose Operator(+,-,*,**,/,//,%) : *
```

**Output:**  
```
50
```

---

### 5. Notes

- Operators like `//` and `%` are especially useful for integer operations.
- This program can be expanded to include more complex calculations or handle exceptions like division by zero.

---

### Author

- Your Name  
- GitHub Repository: [Link to repo]
