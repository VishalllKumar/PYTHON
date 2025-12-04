# String Methods in Python --- Explanation

## String Immutability

Strings in Python are immutable, meaning any method applied returns a
new string without modifying the original.

## Variables Used

``` python
a = "!!!Harry!!!!!! !!!Vishal!!!!!!"
b = 'jay shree ram'
c = 'Welcome to VS code'
```

## Method Explanations

### 1. `len(a)`

Returns the total length of the string `a`.

### 2. `a`

Prints the string as it is.

### 3. `a.upper()`

Converts all letters in `a` to uppercase.

### 4. `a.lower()`

Converts all letters in `a` to lowercase.

### 5. `a.rstrip("!")`

Removes trailing `!` characters from the right end.

### 6. `a.lstrip("!")`

Removes leading `!` characters from the left end.

### 7. `a.replace("Harry", "John")`

Replaces `"Harry"` with `"John"`.

### 8. `a.split(" ")`

Splits `a` into a list using spaces as separators.

### 9. `b.capitalize()`

Capitalizes the first letter and makes the rest lowercase.

### 10. `b.title()`

Capitalizes the first letter of every word in `b`.

### 11. `c.center(50, '.')`

Centers string `c` in a width of 50, filling with `.`.

### 12. `a.count("!")`

Counts occurrences of `!` in `a`.

### 13. `a.endswith("!!!")`

Checks if `a` ends with `"!!!"`.

### 14. `a.find("h")`

Returns the index of the first occurrence of `'h'`, or -1 if not found.

### 15. `a.index("h")`

Same as `.find()` but raises an error if `'h'` is not found.

### 16. `str1.isalnum()`

Checks if all characters are alphanumeric.

### 17. `str1.isalpha()`

Returns `True` if all characters are alphabets.

### 18. `str1.isupper()`

Checks if the string is fully uppercase.

### 19. `str1.islower()`

Checks if the string is fully lowercase.

### 20. `str2.isprintable()`

Returns `False` because `\n` is not printable.

### 21. `str3.isspace()`

Returns `True` if the string contains only whitespace.

### 22. `str2.istitle()`

Checks if every word starts with a capital letter.

### 23. `a.startswith("!!!")`

Checks if `a` begins with `"!!!"`.

### 24. `str4.swapcase()`

Swaps uppercase letters to lowercase and vice versa.

## Summary

This script demonstrates important string methods used for
case-changing, formatting, searching, validating, and transforming
strings in Python.
