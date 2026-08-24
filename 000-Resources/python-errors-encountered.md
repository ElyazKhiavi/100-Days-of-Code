---
title: "Python Errors Encountered"
tags: [python, errors, debugging, reference, documentation]
type: error-log
course: "100 Days of Code"
status: growing
last-updated: 2026-08-22
---

# 🐛 Python Errors Log

> [!TIP]
> Don't memorize every error type. When one hits you → **Google it**, understand it, **log it here**.
> This note is a cheat sheet of bugs I've slain along the way.

---

## SyntaxError

**What:** Code breaks Python's grammar rules.
**Common causes:** Missing colons (`:`), unclosed quotes, unmatched parentheses, typos in keywords.

```python
print('Hello World!)   # unterminated string literal
fro range(5):         # invalid syntax
```

**Fix:** Read the error message. Look for unclosed `()`, `[]`, `{}`, `''`, `""`, or missing `:`.

---

## IndentationError

**What:** Indentation (spacing) is wrong—Python uses whitespace to define code blocks.
**Common causes:** Mixed tabs and spaces, or missing indent inside `for`/`if`/`def`.

```python
for i in range(5):
print(i)  # expected an indented block
```

**Fix:** Use **Tab** or **4 spaces** consistently. Code inside blocks must be indented.

---

## NameError

**What:** Referencing a variable or name that **doesn't exist** in the current scope.
**Common causes:** Typo in variable name, using before assignment, forgot `import`.

```python
pritn(message)  # name 'pritn' is not defined
```

**Fix:** Check spelling. Ensure the variable is assigned _before_ use. Check your imports.

---

## AttributeError

**What:** Trying to access an attribute or method that doesn't exist for that object type.
**Common causes:**

- Typo in method name (e.g., `.forwardd()` instead of `.forward()`).
- Variable is actually `None` (e.g., a function returned `None` instead of an object).
- Forgetting `super().__init__()` in a child class (so it doesn't inherit the parent's methods).

```python
my_list = 5
my_list.append(10)  # 'int' object has no attribute 'append'

trt = None
trt.fd(100)         # 'NoneType' object has no attribute 'fd'
```

**Fix:** Print the type of the variable (`print(type(var))`). If it says `NoneType`, find where your function returned `None` instead of the object. If in a child class, ensure `super().__init__()` is called.

---

## TypeError

**What:** An operation or function receives a value of the **wrong data type**.
**Common cause:** Mixing types that don't play nice together (e.g., str + int).

```python
len(123)             # object of type 'int' has no len()
print("Age: " + 25)  # can only concatenate str (not "int") to str
```

**Fix:** Use `type(var)` to inspect. Convert types using `str()`, `int()`, `float()`.

> [!NOTE] 
> #### Day 2 Context
> `input()` always returns a **string**. Doing math on it without `int()` first → TypeError.

---

## ValueError

**What:** The value is the **right type** but **wrong content** for the operation.
**Common cause:** Trying to convert a non-numeric string to a number.

```python
int("Hello")      # invalid literal for int() with base 10: 'Hello'
float("3.14abc")  # ValueError
```

**Fix:** Validate input before converting, or use `try/except ValueError:`.

---

## IndexError

**What:** You try to access an index that doesn't exist in a sequence (list, string, etc.).
**Common cause:** Asking for item #5 in a list that only has items 0–4.

```python
ls = [0, 1, 2, 3, 4]
print(ls[5])  # list index out of range
```

**Fix:** Remember indexing starts at **0**. Check the length with `len(ls)` first.

---

## KeyError

**What:** Trying to access a dictionary key that doesn't exist.
**Common cause:** User input didn't match any expected dictionary key.

```python
art = {"r": "rock"}
print(art["o"])  # KeyError: 'o'
```

**Fix:** Always validate dictionary access! Use `.get()` with a default value, or check `if key in dict:`.

---

## UnboundLocalError

**What:** Trying to access a **local variable** that hasn't been initialized in the current scope.
**Common cause:** Forgetting to initialize an accumulator (`score = 0`) before a loop, or modifying a global variable inside a function without the `global` keyword.

```python
def check(word):
    for i in word:
        score += 1  # cannot access local variable 'score'
```

**Fix:** Always initialize accumulators **before** loops (`score = 0`). Use the `global` keyword if modifying an outer variable.

---

## ZeroDivisionError

**What:** Trying to divide a number by zero, which is mathematically undefined.
**Common cause:** Using a variable that ends up being `0` as a divisor, often from user input without validation.

```python
total = 0
average = 100 / total  # division by zero
```

**Fix:** Always check the divisor is not zero before dividing.

```python
if total != 0:
    average = 100 / total
else:
    average = 0  # handle gracefully
```

---

## FileNotFoundError

**What:** Trying to open a file that doesn't exist in the specified path.
**Common causes:** Using read mode (`'r'`) on a missing file, or running the script from the wrong Current Working Directory (CWD).

```python
with open("missing_file.txt", "r") as f:
    contents = f.read()
# FileNotFoundError: [Errno 2] No such file or directory: 'missing_file.txt'
```

**Fix:** Check your CWD (`import os; print(os.getcwd())`). Use absolute paths if unsure, or ensure the file exists before reading. If you want Python to create it, use write (`'w'`) or append (`'a'`) mode.

---

## io.UnsupportedOperation

**What:** Performing a file operation that the current file mode does not allow.
**Common cause:** Trying to `.write()` to a file opened in default read (`'r'`) mode.

```python
with open("my_file.txt") as f:  # Default mode is 'r' (read)
    f.write("New text")
# io.UnsupportedOperation: not writable
```

**Fix:** Explicitly specify the mode as `'w'` (write) or `'a'` (append) when opening the file if you intend to modify it.

---

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

- [[Day 13 - Beginner - Debugging How to Find and Fix Errors in your Code]]
- [[Day 16 - Intermediate - Object Oriented Programming (OOP)]] (AttributeError common here)
- [[Day 24 - Intermediate - Files, Directories and Paths]] (FileNotFound & io.UnsupportedOperation common here)
- [[Lists]] | [[Dictionaries]] | [[Type Conversion]] | [[OOP]] | [[File Handling]]

---

_Last updated: Day 24 | Total errors logged: 12_
