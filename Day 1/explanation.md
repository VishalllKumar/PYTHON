# Explanation of Python Code

## 1. Variables
Variables act like containers that store data.
```python
a = 1234567890
print(a)
b = "vishal"
print(b)
```
- `a` stores a number.
- `b` stores a string.
- `print()` displays the values.

---

## 2. Data Types
Python assigns data types automatically based on values.
```python
a = 1          # integer
b = True       # boolean
c = "Harry"    # string
d = None       # no value
e = 1.1        # float
f = complex(8,2)  # complex number
a1 = 9
```
### Printing values and performing operations
```python
print(a)
print(b)
print(a + a1)   # adds two integers
```
### Checking their data types
```python
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
```

---

## 3. Sequenced Data Types: List & Tuple
### List
A list is ordered and mutable.
```python
list1 = [8, 2.3, [-4, 5], ["apple", "bannana"]]
print(list1)
```
- Can store different types of data.
- Can be modified.

### Tuple
A tuple is ordered but immutable.
```python
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)
```
- Values cannot be changed.

---

## 4. Mapped Data Type: Dictionary
A dictionary stores data in key–value pairs.
```python
dict1 = {
    'name': 'Vishal',
    'class': 12,
    'roll no.': 40,
    'can_vote': True
}
print(dict1)
```
- Keys: `'name'`, `'class'`, `'roll no.'`, `'can_vote'`
- Values: `'Vishal'`, `12`, `40`, `True`
- Dictionaries are unordered and mutable.
