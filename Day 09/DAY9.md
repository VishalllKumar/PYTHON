# 🐍 Python Loops

Loops are used to execute a block of code repeatedly until a condition becomes false.

There are **two types of loops** in Python:

1. **For Loop**
2. **While Loop**

---

# 1️⃣ For Loop

A **for loop** is used when you know **how many times** you want to repeat something.

## Syntax

```python
for variable in sequence:
    # code
```

---

## Example 1

```python
for i in range(5):
    print(i)
```

### Output

```
0
1
2
3
4
```

### Explanation

```python
range(5)
```

creates the numbers:

```
0, 1, 2, 3, 4
```

The loop works like this:

| Iteration | Value of i | Output |
|-----------|------------|--------|
| 1 | 0 | 0 |
| 2 | 1 | 1 |
| 3 | 2 | 2 |
| 4 | 3 | 3 |
| 5 | 4 | 4 |

After `i = 4`, the loop ends automatically.

---

# 2️⃣ While Loop

A **while loop** runs **until a condition becomes False**.

## Syntax

```python
while condition:
    # code
```

If the condition is True, the loop continues.

If the condition is False, the loop stops.

---

## Example 1

```python
i = 0

while i < 3:
    print(i)
    i = i + 1
```

### Output

```
0
1
2
```

### Step-by-Step

Initial value

```
i = 0
```

Iteration 1

```
0 < 3 ✅
print(0)
i = 1
```

Iteration 2

```
1 < 3 ✅
print(1)
i = 2
```

Iteration 3

```
2 < 3 ✅
print(2)
i = 3
```

Now

```
3 < 3 ❌
```

Loop stops.

---

## Example 2

```python
i = 0

while i <= 34:
    i = int(input("Enter number: "))
    print(i)
```

### Explanation

Initially

```
i = 0
```

Condition

```
0 <= 34
```

is True.

The program keeps asking the user to enter a number.

Example

```
Enter number: 5
5

Enter number: 20
20

Enter number: 34
34

Enter number: 40
40
```

Now

```
40 <= 34
```

is False.

The loop ends.

---

## Example 3 (Countdown)

```python
count = 10

while count > 0:
    print(count)
    count -= 1
else:
    print("meow")
```

### Output

```
10
9
8
7
6
5
4
3
2
1
meow
```

### Explanation

The loop prints numbers from **10 to 1**.

Each time,

```python
count -= 1
```

means

```python
count = count - 1
```

After reaching

```
count = 0
```

Condition becomes False.

The `else` block executes.

---

# While Loop with Else

The `else` block runs **only when the while loop ends normally**.

## Syntax

```python
while condition:
    # code
else:
    # executes after loop finishes normally
```

### Example

```python
count = 3

while count > 0:
    print(count)
    count -= 1
else:
    print("Loop Finished")
```

Output

```
3
2
1
Loop Finished
```

---

# 3️⃣ Break Statement

`break` immediately **terminates** the loop.

## Syntax

```python
break
```

---

## Example

```python
for i in range(1, 12):

    if i == 11:
        break

    print("5 x", i, "=", 5 * i)
```

### Output

```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```

When

```python
i == 11
```

Python executes

```python
break
```

and exits the loop immediately.

---

# Break Flow

```
Start

↓

i = 1

↓

Print

↓

i = 2

↓

Print

↓

...

↓

i = 11

↓

break

↓

Loop Ends
```

---

# 4️⃣ Continue Statement

`continue` skips the **current iteration** and moves to the next one.

## Syntax

```python
continue
```

---

## Example

```python
for i in range(1, 12):

    if i == 10:
        continue

    print("5 x", i, "=", 5 * i)
```

### Output

```
5 x 1 = 5
5 x 2 = 10
...
5 x 9 = 45

5 x 11 = 55
```

Notice

```
5 x 10 = 50
```

is skipped.

The loop does **not stop**.

It simply skips that iteration.

---

# Continue Flow

```
i = 1

↓

Print

↓

...

↓

i = 10

↓

continue

↓

Skip Printing

↓

i = 11

↓

Print
```

---

# 5️⃣ Pass Statement

`pass` means

> **"Do nothing."**

Python expects some code inside blocks.

If you haven't written the code yet, use `pass`.

---

## Example

```python
for i in range(1, 12):

    if i == 10:
        pass

    print("5 x", i, "=", 5 * i)
```

### Output

```
5 x 1 = 5
...
5 x 9 = 45
5 x 10 = 50
5 x 11 = 55
```

Since `pass` does nothing, every iteration is printed.

---

# Difference Between break, continue and pass

| Statement | What it Does |
|------------|-------------|
| `break` | Stops the loop immediately |
| `continue` | Skips only the current iteration |
| `pass` | Does nothing |

---

# Visual Comparison

## break

```
1
2
3
4
STOP ❌
```

---

## continue

```
1
2
3
(skip 4)
5
6
```

---

## pass

```
1
2
3
4
5
```

Nothing changes.

---

# When to Use Which?

### Use **for loop**

- When you know the number of iterations.
- Working with `range()`, lists, tuples, strings, etc.

Example

```python
for i in range(10):
    print(i)
```

---

### Use **while loop**

- When you don't know how many times the loop should run.
- Depends on a condition.

Example

```python
while password != "python":
    password = input("Enter Password: ")
```

---

# Summary

| Topic | Purpose |
|--------|---------|
| `for` | Repeat over a sequence |
| `while` | Repeat until condition becomes False |
| `break` | Exit the loop |
| `continue` | Skip current iteration |
| `pass` | Placeholder that does nothing |
| `else` with while | Executes when loop finishes normally |

---

# Quick Revision

```python
# FOR LOOP
for i in range(5):
    print(i)

# WHILE LOOP
i = 0
while i < 5:
    print(i)
    i += 1

# BREAK
for i in range(10):
    if i == 5:
        break
    print(i)

# CONTINUE
for i in range(10):
    if i == 5:
        continue
    print(i)

# PASS
for i in range(5):
    if i == 2:
        pass
    print(i)
```

---

# 💡 Tip

Remember this simple trick:

- 🔁 **for** → Fixed number of repetitions.
- ♾️ **while** → Runs until a condition changes.
- 🛑 **break** → Exit the loop.
- ⏭️ **continue** → Skip one iteration.
- 😴 **pass** → Do nothing.