# Explanation of String Operations in Python

## Code Snippet

```python
names = "Harry,Vishal"
namelen = len(names)
print(namelen)
print(names[0:4])       # ()n-1
print(names[0:-3])      # it means print(names[0:len(names)-3])
print(names[-3:-1])     # it means print(names[len(names) - 3 : len(names) - 1])

# Quick Quiz:
nm = "Harry"
print(nm[-4:-2])        # it means print(nm[len(nm) - 4 : len(nm) - 2])
# output=3
```

---

## Explanation

### 1. Length of the String
```python
namelen = len(names)
```
- `len()` function is used to find the length of the string.
- Here, `names = "Harry,Vishal"` has **12 characters** (including the comma), so `namelen = 12`.

---

### 2. String Slicing

#### a. `names[0:4]`
- Slicing syntax: `string[start:end]`
- Returns characters from index `0` to `3` (end index is exclusive).
- Output: `"Harr"`

#### b. `names[0:-3]`
- Negative index `-3` means **`len(names) - 3`**.
- So, this slice is equivalent to: `names[0:9]` (0 to 8 index).
- Output: `"Harry,Vis"`

#### c. `names[-3:-1]`
- Negative indices count from the end: `-1` is last character.
- Equivalent to: `names[len(names)-3 : len(names)-1]` → `names[9:11]`
- Output: `"ha"`

---

### 3. Quick Quiz: `nm[-4:-2]`
- `nm = "Harry"` has 5 characters.
- Slice `nm[-4:-2]` → `nm[1:3]`
- Characters at index `1` and `2` → `"ar"`
- Output: `"ar"`

---

### Summary
- Negative indices in Python count from the end (`-1` is the last character).
- Slicing uses `[start:end]` format where `end` is **exclusive**.
- Using `len(string)` helps calculate slices relative to the string's length.

