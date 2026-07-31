---
title: "Python Errors Encountered"
tags: [python, errors, debugging, reference]
type: error-log
course: "100 Days of Code"
status: growing
last-updated: 2026-07-31
---

# 🐛 Python Errors Log

> [!tip] Philosophy
> You don't need to memorize every error type.  
> When one hits you → **Google it**, understand it, **log it here**.  
> This note is a the graveyard of bugs I've slain along the way.

---

## SyntaxError

**What:** Your code breaks Python's grammar rules.  
**Common causes:** Missing quotes, unmatched parentheses, wrong indentation, typos in keywords.

```python
# Missing closing quote
print('Hello World!)   # SyntaxError: unterminated string literal

# Mismatched brackets
print((1 + 2) * 3      # SyntaxError: unexpected EOF

# Keyword typo
fro range(5):           # SyntaxError: invalid syntax
```

**Fix:** Read the error message carefully — Python usually points to the exact line + character. Look for unclosed `()`, `[]`, `{}`, `''`, `""`.

---

## TypeError

**What:** An operation or function receives a value of the **wrong data type**.  
**Common cause:** Mixing types that don't play nice together.

```python
len(123)
# TypeError: object of type 'int' has no len()

print("Age: " + 25)
# TypeError: can only concatenate str (not "int") to str

"hello"[1.0]
# TypeError: string indices must be integers
```

**Fix:** Check what type your function expects. Use `type(var)` to inspect, or convert with `str()`, `int()`, `float()`.

> [!example] Day 2 context
>
> `input()` always returns a **string**. Doing math on it without `int()` first → TypeError.

---

## ValueError

**What:** The value is the **right type** but **wrong content** for the operation.  
**Common cause:** Trying to convert a non-numeric string to a number.

```python
# ✅ This works — string looks like a number
int("42")        # 42

# ❌ This explodes — string is NOT a number
int("Hello")
# ValueError: invalid literal for int() with base 10: 'Hello'

float("3.14abc") # ValueError
```

**Key distinction from TypeError:**
| Error | Meaning |
|-------|---------|
| `TypeError` | Wrong _kind_ of object (gave a banana, expected a wrench) |
| `ValueError` | Right kind, but broken inside (gave a wrench, but it's melted) |

**Fix:** Validate input before converting.

---

## NameError

**What:** You're referencing a variable or name that **doesn't exist** in the current scope.  
**Common causes:** Typo in variable name, using before assignment, forgot import.

```python
print(Hello)
# NameError: name 'Hello' is not defined
# (Python thinks Hello is a variable, not a string!)

message = "hi"
pritn(message)
# NameError: name 'pritn' is not defined  ← typo!

import math
print(mth.pi)
# NameError: name 'mth' is not defined    ← typo!
```

**Fix:** Check spelling. Make sure the variable is assigned _before_ you use it. Python reads top-to-bottom.

---

## (More errors will be added as we meet them...)

<!--
📋 ERROR TEMPLATE — copy & paste when a new one bites you:

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

- [[Day 13 - Debugging: How to Find and Fix Errors]] _(deep dive coming soon)_
- [[Data Types]]
- [[Type Conversion]]
- [[Python Debugging Techniques]]

---

_Last updated: Day 2 | Total errors logged: 4_
