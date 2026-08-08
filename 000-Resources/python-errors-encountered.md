---
title: "Python Errors Encountered"
tags: [python, errors, debugging, reference]
type: error-log
course: "100 Days of Code"
status: growing
last-updated: 2026-08-06
---

# 🐛 Python Errors Log

> [!tip] Philosophy
> Don't memorize every error type. Google it, understand it, log it here.  
> This note is a graveyard of bugs I've slain along the way.

---

## SyntaxError

**What:** Code breaks Python's grammar rules.  
**Common causes:** Missing quotes, unmatched parentheses, wrong indentation, typos in keywords.

```python
print('Hello World!)   # unterminated string literal
fro range(5):           # invalid syntax
```

**Fix:** Read the error message. Look for unclosed `()`, `[]`, `{}`, `''`, `""`.

---

## TypeError

**What:** Operation receives a value of the **wrong data type**.  
**Common cause:** Mixing types (e.g., str + int).

```python
len(123)             # object of type 'int' has no len()
print("Age: " + 25)  # can only concatenate str (not "int") to str
```

**Fix:** Use `type(var)` to inspect. Convert with `str()`, `int()`, `float()`.

> [!note] Day 2 context
> `input()` always returns a **string**. Doing math on it without `int()` first → TypeError.

---

## ValueError

**What:** Value is the **right type** but **wrong content**.  
**Common cause:** Converting a non-numeric string to a number.

```python
int("Hello")   # invalid literal for int() with base 10: 'Hello'
float("3.14abc") # ValueError
```

**Fix:** Validate input before converting, or use `try/except`.

---

## NameError

**What:** Referencing a variable or name that **doesn't exist** in the current scope.  
**Common causes:** Typo in variable name, using before assignment, forgot import.

```python
pritn(message)  # name 'pritn' is not defined
```

**Fix:** Check spelling. Ensure variable is assigned _before_ use.

---

## IndexError

**What:** Accessing an index that doesn't exist in a sequence.  
**Common cause:** Asking for item #5 in a list that only has items 0–4.

```python
ls = [0, 1, 2, 3, 4]
print(ls[5])  # list index out of range
```

**Fix:** Remember indexing starts at **0**. Check length with `len()` first.

---

## KeyError

**What:** Accessing a dictionary key that doesn't exist.  
**Common cause:** User input didn't match any expected dictionary key.

```python
art = {"r": "rock"}
print(art["o"])  # KeyError: 'o'
```

**Fix:** Use `.get()` with a default value, or check `if key in dict:`.

---

## IndentationError

**What:** Indentation is wrong—Python uses whitespace to define code blocks.  
**Common cause:** Mixed tabs/spaces, or missing indent inside `for`/`if`/`def`.

```python
for i in range(5):
print(i)  # expected an indented block
```

**Fix:** Use **Tab** or **4 spaces** consistently. Code inside blocks must be indented.

---

## UnboundLocalError

**What:** Trying to access a **local variable** that doesn't exist in the current scope.  
**Common cause:** Referenced a variable inside a function before assigning it a value.

```python
def check(word):
    for i in word:
        score += 1  # cannot access local variable 'score'
```

**Fix:** Always initialize accumulators (`score = 0`) **before** loops.

---

## ZeroDivisionError

**What:** Trying to divide a number by zero, which is mathematically undefined.  
**Common cause:** Using a variable that ends up being `0` as a divisor, often in a loop or user input without validation.

```python
total = 0
average = 100 / total  # division by zero
```

**Fix:** Always check the divisor is not zero before dividing. You can use an `if` guard:

```python
if total != 0:
    average = 100 / total
else:
    average = 0  # or handle gracefully
```

<!--
📋 ERROR TEMPLATE:

## ErrorName
**What:** One-line description.
**When/Why it happened:** Context from your code.

```python
# Your failing code here
```
**Fix:** How you solved it.
-->

---

## 🔗 See Also

- [[Day 13 - Debugging: How to Find and Fix Errors]]
- [[Lists]] | [[Dictionaries]] | [[Type Conversion]]

---

_Last updated: Day 10 | Total errors logged: 9_
