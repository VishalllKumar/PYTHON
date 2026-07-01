# Python `for` / `while` Loop with `else`

## What is `else` with a loop?

In Python, the `else` block attached to a `for` or `while` loop runs
**only if the loop finishes normally**.

-   ✅ `else` runs if the loop completes without `break`.
-   ❌ `else` does **not** run if the loop is terminated using `break`.

------------------------------------------------------------------------

# `for` Loop with `else`

## Example 1

``` python
for i in range(5):
    print(i)
else:
    print("no i")
```

### Output

``` text
0
1
2
3
4
no i
```

### Explanation

-   `range(5)` generates numbers from **0 to 4**.
-   The loop finishes normally.
-   Since **no `break` statement** is executed, the `else` block runs.
-   Therefore, `"no i"` is printed.

------------------------------------------------------------------------

## Example 2

``` python
for i in range(6):
    print(i)

    if i == 4:
        break
else:
    print("no i")
```

### Output

``` text
0
1
2
3
4
```

### Explanation

-   `range(6)` generates **0 to 5**.
-   When `i` becomes **4**, the `break` statement executes.
-   `break` immediately terminates the loop.
-   Because the loop did **not** finish normally, the `else` block is
    skipped.

------------------------------------------------------------------------

# `while` Loop with `else`

## Example 1

``` python
i = 0

while i < 10:
    i += 1
    print(i)

    if i == 4:
        break
else:
    print("no i")
```

### Output

``` text
1
2
3
4
```

### Explanation

-   `i` starts from **0**.
-   `i` is increased before printing.
-   When `i` becomes **4**, `break` stops the loop.
-   Since the loop ended using `break`, the `else` block does **not**
    execute.

------------------------------------------------------------------------

## Example 2

``` python
i = 0

while i < 10:
    print(i)
    i += 1
else:
    print("no i")
```

### Output

``` text
0
1
2
3
4
5
6
7
8
9
no i
```

### Explanation

-   `i` starts from **0**.
-   The loop prints numbers from **0 to 9**.
-   When `i` becomes **10**, the condition `i < 10` becomes **False**.
-   The loop finishes normally.
-   Since there is **no `break`**, the `else` block executes.

------------------------------------------------------------------------

# Difference Between `break` and `else`

  Situation                             Will `else` Run?
  ------------------------------------- ------------------
  Loop finishes normally                ✅ Yes
  Loop ends with `break`                ❌ No
  Condition becomes False (`while`)     ✅ Yes
  `for` loop iterates over all values   ✅ Yes

------------------------------------------------------------------------

# Easy Trick to Remember

Think of the loop `else` like this:

> **"If the loop was NOT interrupted by `break`, then execute the `else`
> block."**

------------------------------------------------------------------------

# Interview Point

Many beginners think that the loop `else` runs when the loop condition
becomes false.

That is **partly true**, but the actual rule is:

> **The `else` block executes only when the loop finishes normally
> without encountering a `break` statement.**
