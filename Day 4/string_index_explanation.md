# Python Strings Example

This Python code demonstrates how to work with **strings**, access their characters using indices, and iterate over the characters using a loop.

---

## Code Explanation

### 1. Creating a String

```python
name = 'Harry'
print('hello ' + name)
```

- We define a string variable `name` and assign it the value `'Harry'`.
- Using the `print` function, we concatenate `'hello '` with the value of `name` using the `+` operator.
- **Output:**  
  ```
  hello Harry
  ```

---

### 2. Accessing Characters by Index

```python
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) # IndexError
```

- Strings in Python are **indexed**, starting from `0`.
- `name[0]` accesses the first character `'H'`, `name[1]` accesses the second character `'a'`, and so on.
- Trying to access `name[5]` will give an **IndexError** because the string `'Harry'` has only 5 characters (indices `0` to `4`).

**Output:**
```
H
a
r
r
y
```

---

### 3. Accessing Characters Using a `for` Loop

```python
for character in name:
    print(character)
```

- We use a **for loop** to iterate over each character in the string `name`.
- Each iteration assigns the current character to the variable `character` and prints it.

**Output:**
```
H
a
r
r
y
```

---

### Summary

- Strings are sequences of characters that can be accessed using **indices**.
- Indexing starts from `0` in Python.
- You can use a **for loop** to iterate through each character in a string.
- Be careful not to access an index that is out of the string's range to avoid **IndexError**.