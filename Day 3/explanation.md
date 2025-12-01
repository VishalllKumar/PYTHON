# Typecasting in Python

Typecasting in Python is the conversion of one data type into another data type. There are two main types of typecasting:

1. **Explicit Typecasting** - manually converting one type to another using functions like `int()`, `float()`, `str()`, etc.
2. **Implicit Typecasting** - automatic conversion done by Python when different data types are used together.

---

```python
# Example 1: String concatenation vs integer addition
a = '1'
b = '2'
print(a + b)  # Output: '12'
```
**Explanation:** Here, `a` and `b` are strings. Using `+` with strings performs concatenation, not arithmetic addition. Hence the output is `'12'`.

```python
a = 1
b = 2
print(a + b)  # Output: 3
```
**Explanation:** Here, `a` and `b` are integers. Using `+` adds their values, so the output is `3`.

---

# Explicit Typecasting
```python
a = '1'
b = '2'
print(int(a) + int(b))  # Output: 3
```
**Explanation:** Here, `a` and `b` are strings. We explicitly convert them to integers using `int()`. Now `+` performs integer addition, giving `3`.

---

# Implicit Typecasting
```python
a = 1.9
b = 8
print(a + b)  # Output: 9.9
```
**Explanation:** `a` is a float and `b` is an integer. Python automatically converts the integer `b` to float, then adds them. The result is `9.9` (float).

---

**Summary:**
- Strings with `+` concatenate.
- Integers with `+` add numerically.
- Explicit typecasting changes type manually.
- Implicit typecasting happens automatically when combining different numeric types.

