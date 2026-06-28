# 🐍 Python `match-case` Statement Explained

---

## 📌 Code

```python
x = int(input("Enter the value of x: "))

match x:
    case 0:
        print("x is zero")

    case 4:
        print("x is 4")

    case _ if x != 90:
        print(x, "is not 90")

    case _ if x != 80:
        print(x, "is not 80")

    case _:
        print(x)
```

---

# 🎯 What is `match-case`?

`match-case` was introduced in **Python 3.10** and works similarly to a switch-case statement.

## 🧠 Key Takeaways

✔ Cases are checked from top to bottom.  
✔ The first matching case executes.  
✔ `_` acts as the default case.  
✔ `if` inside a case is called a guard condition.  
✔ In this program, `case _ if x != 90` makes the next condition almost unreachable.

---

# 🧪 Sample Outputs

| Input | Output |
|---------|---------|
| 0 | x is zero |
| 4 | x is 4 |
| 50 | 50 is not 90 |
| 80 | 80 is not 90 |
| 90 | 90 is not 80 |

---

# 🚀 Exam Definition

**Match-case is a control statement introduced in Python 3.10 that allows a variable's value to be matched against multiple cases, executing the code block of the first matching case.**
