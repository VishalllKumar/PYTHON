# Day 11 - Python Lists 📋

## What is a List?

A **List** is a collection of multiple items stored in a single variable.

- Lists are **ordered**
- Lists are **mutable** (can be changed)
- Lists can store **different data types**
- Lists allow **duplicate values**

### Example

```python
marks = [3, 5, 6, "Harry", True]
print(marks)
```

**Output**
```
[3, 5, 6, 'Harry', True]
```

---

# Accessing List Elements

Lists use **Indexing**.

```python
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
```

**Output**
```
3
5
6
Harry
True
```

---

## Index Error

```python
print(marks[5])
```

Since the list contains only **5 elements**, the last index is **4**.

So Python gives:

```
IndexError: list index out of range
```

---

# Negative Indexing

Negative indexing starts counting from the end.

```
Index      :  0    1    2      3       4
Value      : [3,   5,   6,   Harry,   True]

Negative   : -5   -4   -3     -2      -1
```

Example:

```python
print(marks[-3])
```

Python converts it like this:

```
len(marks) = 5
marks[-3] = marks[5-3] = marks[2]
```

Output

```
6
```

---

# Membership Operator (`in`)

```python
if "Harry" in marks:
    print("Yes")
else:
    print("No")
```

Output

```
Yes
```

---

# Membership in String

```python
if "rr" in "Harry":
    print("Yes")
else:
    print("No")
```

Output

```
Yes
```

---

# List Slicing

## Syntax

```python
list[start:stop]
```

- start → included
- stop → excluded

Example:

```python
print(marks[1:-1])
```

Output

```
[5, 6, 'Harry']
```

---

# Slicing with Step

Syntax:

```python
list[start:stop:step]
```

Example:

```python
print(marks[1:4:2])
```

Output

```
[5, 'Harry']
```

Example:

```python
print(marks[0:4:3])
```

Output

```
[3, 'Harry']
```

---

# List Comprehension

```python
lst = [i*i for i in range(10) if i % 2 == 0]
print(lst)
```

Output

```
[0, 4, 16, 36, 64]
```

---

# Filtering Names

```python
names = ["Milo","Sarah","Bruno","Anastasia","Rosa"]
filtre = [i for i in names if len(i)>4]
print(filtre)
```

Output

```
['Sarah', 'Bruno', 'Anastasia']
```

---

# Filtering Names Starting with B

```python
filtre = [names[i] for i in range(len(names)) if names[i][0] == 'B']
print(filtre)
```

Output

```
['Bruno']
```

---

# List Methods

## append()

Adds one element at the end.

## sort()

Sorts the list. Use `reverse=True` for descending order.

## reverse()

Reverses the current list.

## index(value)

Returns the first occurrence index.

## count(value)

Returns how many times the value occurs.

## copy()

Creates a separate copy of the list.

## insert(index, value)

Inserts an element at a specific index.

## extend()

Adds another list to the end of the current list.

---

# List Aliasing

```python
m = l
```

Both variables point to the same list.

Changing `m` also changes `l`.

---

# Copying a List

## Method 1: Slicing

```python
y = x[:]
```

Creates a new independent copy.

## Method 2: copy()

```python
m = l.copy()
```

Creates another independent copy.

---

# Concatenation

```python
k = l + m
```

Creates a new list by combining two lists.

Unlike `extend()`, it does not modify the original list.

---

# Summary

| Method | Purpose |
|--------|---------|
| append() | Add one item at end |
| sort() | Sort list |
| reverse() | Reverse list |
| index() | Find first index |
| count() | Count occurrences |
| copy() | Create separate copy |
| insert() | Insert at any position |
| extend() | Add another list |
| + | Concatenate two lists |

---

# Key Points ⭐

- Lists are mutable.
- Index starts from `0`.
- Negative indexing starts from `-1`.
- `in` checks membership.
- Slicing uses `start:stop:step`.
- List comprehension creates lists in one line.
- `append()` adds one item.
- `extend()` adds another list.
- `copy()` creates an independent copy.
- `m = l` creates an alias, not a copy.
- `+` concatenates two lists into a new list.
