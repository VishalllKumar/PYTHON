# Python Sets -- Complete Notes

## What is a Set?

A **set** is an unordered collection of unique elements.

``` python
s = {2, 4, 2, 6}
print(s)
```

**Output**

``` text
{2, 4, 6}
```

-   Duplicate values are removed automatically.
-   Sets are **unordered**, so the order may change.
-   Sets are **mutable** (you can add/remove elements), but their
    elements must be immutable.

------------------------------------------------------------------------

## Creating a Set

``` python
info = {"Carla", 19, False, 5.9, 19}
print(info)
```

-   Duplicate `19` is removed.
-   Indexing is **not allowed** because sets are unordered.

### Empty Set

``` python
harry = set()
print(type(harry))
```

Use `set()` for an empty set. `{}` creates an empty dictionary.

------------------------------------------------------------------------

## Traversing a Set

``` python
for i in info:
    print(i)
```

Prints every element in an unpredictable order.

------------------------------------------------------------------------

# Set Operations

## 1. `union()`

Returns a new set containing all unique elements.

``` python
s1 = {1,2,5,6}
s2 = {3,6,7}

print(s1.union(s2))
```

Output:

``` text
{1,2,3,5,6,7}
```

Original set remains unchanged.

------------------------------------------------------------------------

## 2. `update()`

Adds all elements of another set into the current set.

``` python
s1.update(s2)
print(s1)
```

Output:

``` text
{1,2,3,5,6,7}
```

------------------------------------------------------------------------

## 3. `intersection_update()`

Keeps only common elements and updates the original set.

``` python
cities.intersection_update(cities2)
```

Example:

Set1:

    Tokyo Madrid Berlin Delhi

Set2:

    Tokyo Seoul Kabul Madrid

Result:

    Tokyo Madrid

------------------------------------------------------------------------

## 4. `symmetric_difference()`

Returns elements that are present in only one of the sets.

``` python
cities.symmetric_difference(cities2)
```

Result:

    Berlin Delhi Seoul Kabul

------------------------------------------------------------------------

## 5. `difference()`

Returns elements present in the first set but not in the second.

``` python
cities.difference(cities2)
```

Result:

    Berlin Delhi

------------------------------------------------------------------------

## 6. `issuperset()`

Checks whether all elements of another set exist in the current set.

``` python
cities.issuperset(cities2)
```

Returns `True` if every element of `cities2` is present in `cities`.

------------------------------------------------------------------------

## 7. `issubset()`

Opposite of `issuperset()`.

``` python
cities2.issubset(cities)
```

Returns `True` if every element of `cities2` exists in `cities`.

------------------------------------------------------------------------

## 8. `add()`

Adds one element.

``` python
cities.add("Meow")
```

------------------------------------------------------------------------

## 9. `remove()`

Removes an element.

``` python
cities.remove("Tokyo")
```

If the element doesn't exist, Python raises a **KeyError**.

------------------------------------------------------------------------

## 10. `discard()`

Removes an element if present.

``` python
cities.discard("Tokyo2")
```

No error if the element is absent.

------------------------------------------------------------------------

## 11. `pop()`

Removes and returns a random element because sets are unordered.

``` python
item = cities.pop()
print(item)
```

------------------------------------------------------------------------

## 12. `clear()`

Removes all elements.

``` python
cities.clear()
print(cities)
```

Output:

``` text
set()
```

------------------------------------------------------------------------

## 13. `del`

Deletes the entire set.

``` python
del cities
```

Accessing it afterwards gives:

``` text
NameError
```

------------------------------------------------------------------------

# Membership Operator

``` python
info = {"Carla",19,False,5.9}

if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
```

Checks whether an element exists in a set.

------------------------------------------------------------------------

# Quick Revision Table

  Method                     Purpose
  -------------------------- -----------------------------------------
  `union()`                  Combines two sets
  `update()`                 Adds elements into current set
  `intersection_update()`    Keeps common elements
  `symmetric_difference()`   Keeps uncommon elements
  `difference()`             Elements only in first set
  `issuperset()`             Checks if current set contains another
  `issubset()`               Checks if current set is inside another
  `add()`                    Adds one element
  `remove()`                 Removes element (error if absent)
  `discard()`                Removes element (no error)
  `pop()`                    Removes a random element
  `clear()`                  Empties the set
  `del`                      Deletes the set completely
  `in`                       Membership check

------------------------------------------------------------------------

## Important Points for Exams

-   Sets are unordered.
-   Duplicate values are not allowed.
-   Sets do not support indexing.
-   Empty set is created using `set()`.
-   `remove()` throws an error if the element doesn't exist.
-   `discard()` never throws an error.
-   `pop()` removes a random element.
