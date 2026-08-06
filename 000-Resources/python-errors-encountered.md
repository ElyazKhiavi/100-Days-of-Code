---
title: "Python Errors Encountered"
tags: [python, errors, debugging, reference]
type: error-log
course: "100 Days of Code"
status: growing
last-updated: 2026-08-03
---

# 🐛 Python Errors Log

> [!tip] Philosophy
> You don't need to memorize every error type.  
> When one hits you → **Google it**, understand it, **log it here**.  
> This note is a graveyard of bugs I've slain along the way.

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

> [!note] Day 2 context
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

| Error        | Meaning                                                        |
| ------------ | -------------------------------------------------------------- |
| `TypeError`  | Wrong _kind_ of object (gave a banana, expected a wrench)      |
| `ValueError` | Right kind, but broken inside (gave a wrench, but it's melted) |

**Fix:** Validate input before converting, or wrap in `try/except` (you'll learn this soon).

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

## IndexError

**What:** You try to access an index that doesn't exist in a sequence (list, string, etc.).  
**When/Why it happened:** Index is out of range — you asked for item #5 in a list that only has items 0–4.

```python
ls = [0, 1, 2, 3, 4]
print(ls[5])
# IndexError: list index out of range

# Also happens with strings
name = "Alice"
print(name[10])
# IndexError: string index out of range
```

**Fix:** Remember indexing starts at **0**. Check the length with `len()` first, or use negative indices carefully (`[-1]` = last item, always safe if list isn't empty).

> [!note] Day 4 context
> Lists are zero-indexed. A list of 5 items has valid indices 0, 1, 2, 3, 4. Anything else → IndexError.

---

## KeyError

**What:** Similar to IndexError, but for **dictionaries**. Happens when you try to access a key that doesn't exist in the dict.  
**When/Why it happened:** User input didn't match any expected dictionary key.

```python
art = {"r": rock, "p": paper, "s": scissors}
user_choice = "o"  # user typed something invalid
print(art[user_choice])
# KeyError: 'o'
```

**Real-world traceback from my Rock Paper Scissors game:**

```bash
✊ Make your move: (r)ock, (p)aper, or (s)cissors? o
Traceback (most recent call last):
  File ".../Rock-Paper-Scissors-Game.py", line 125, in <module>
    print(f"🎯 Your choose {art[user]}")
                            ~~~^^^^^^
KeyError: 'o'
```

**Fix:** Always validate dictionary access! Use `.get()` with a default value, or check `if key in dict` before accessing:

```python
# Safe approach — check first
if user in art:
    print(art[user])
else:
    print("Invalid choice!")

# Or use .get() with fallback
print(art.get(user, "Invalid choice!"))
```

---

## IndentationError

**What:** Your indentation (spacing) is wrong — Python uses whitespace to define code blocks.  
**When/Why it happened:** Added extra spaces at the start of a line where Python didn't expect them, or mixed tabs with spaces.

```python
# Wrong — unexpected indent at start of line
 ls = ['a', 'b', 'c']
# IndentationError: unexpected indent

# Correct — no leading spaces at top level
ls = ['a', 'b', 'c']
```

Also happens inside loops/conditionals when you inconsistent indentation:

```python
for i in range(5):
print(i)  # IndentationError: expected an indented block

# Correct
for i in range(5):
    print(i)  # 4 spaces (or 1 tab) — must be consistent!
```

**Fix:**

- Use **Tab** or **4 spaces** consistently — never mix them
- Code inside `for`, `if`, `def`, `with`, etc. must be indented
- Most editors can show invisible characters (`Alt+Z` in VS Code)
- Python convention: **4 spaces per indent level**

> [!note] Day 5 context
> Loops introduce new indentation blocks.
>
> Forgetting to indent the loop body → IndentationError.
>
> Indenting something that shouldn't be → also IndentationError.

---

## UnboundLocalError

**What:** You're trying to access a **local variable** that doesn't exist in the current scope.  
**When/Why it happened:** Inside a function, you referenced a variable that was defined in a **different function or scope**, or you tried to use a variable before assigning it a value.

**Real-world traceback from my Love Calculator:**

```bash
File ".../Love-Calculator.py", line 53, in <module>
    calculate_love_score(input("Name 1:"), input("Name 2: "))
  File ".../Love-Calculator.py", line 49, in check
    digit += score  # ← THIS is where it broke!
    ^^^^^
UnboundLocalError: cannot access local variable 'digit'
where it is not associated with a value
```

**The Problem:** In my `check()` nested inside `calculate_love_score()`, I used `digit` as an accumulator variable but **forgot to initialize it before the loop** (`digit = 0` before the `for` loop). Python sees `digit += score` → looks for `digit` → can't find it in current/local scope → explodes.

**Fix:** Always initialize your accumulators BEFORE the loop/function:

```python
def check(word):
    score = 0  # ← ADD THIS
    for i in name1 + name2:
        if i.lower() in word:
            score += 1
    return score
```

> [!tip] Common Pattern
> This error almost always means one of two things:
>
> 1. **Forgot to initialize** a variable before using it (most common cause!)
> 2. **Typo in variable name** — Python says "not associated" = you misspelled it somewhere

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
- [[Lists]]
- [[Dictionaries]]
- [[Type Conversion]]
- [[Python Debugging Techniques]]

---

_Last updated: Day 8 | Total errors logged: 8_
