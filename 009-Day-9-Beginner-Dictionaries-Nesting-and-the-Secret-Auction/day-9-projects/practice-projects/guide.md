## 🧪 Your Project Prompts for Day 9

Pick **one** project (or more if you’re feeling ambitious). Write the code entirely yourself, then post it here and I’ll give you a thorough review.

### 🔹 Project 1: Personal Phonebook

Build a terminal‑based phonebook that stores contacts and their phone numbers.

**Requirements:**
- Use a dictionary to store contacts, e.g., `phonebook = {"Alice": "123-4567", "Bob": "987-6543"}`.
- Provide a menu with options:
  1. Add a contact (ask for name and number, store them).
  2. Look up a contact (ask for name, print the number or a “not found” message).
  3. List all contacts (print all names and numbers).
  4. Delete a contact (ask for name, remove if exists, else show an error).
  5. Quit.
- If a user tries to add a name that already exists, ask if they want to overwrite it.
- The phonebook does **not** persist to a file – it’s fine to reset when the program ends.
- Use functions for each action (`add_contact`, `lookup_contact`, etc.).

**Example run:**
```
Phonebook
1. Add contact
2. Look up
3. List all
4. Delete
5. Quit
Choose: 2
Enter name: Alice
Alice: 123-4567
```

---

### 🔹 Project 2: Student Grade Manager

Create a program that lets a teacher manage student grades using a dictionary where each key is a student name and the value is a list of their scores.

**Requirements:**
- Initialise with an empty dictionary, e.g., `grades = {}`.
- Menu options:
  1. Add a student (if new, create an empty list; if existing, just print a note).
  2. Add a grade for a student (ask for name and a score 0‑100, append to their list; if student doesn’t exist, offer to create them first).
  3. Display a student’s average (name → average of scores, or “no grades yet”).
  4. Display all students with their averages.
  5. Quit.
- Use functions: `add_student`, `add_grade`, `get_average`, `display_all`.
- Think about edge cases: what if the student has no grades yet? What if the user enters a non‑numeric score? (At this stage, you can assume valid input or use `.isdigit()` for basic checking.)

---

### 🔹 Project 3: Blind Auction Variant – “Secret Santa Wishlist”

Instead of bids, create a program where multiple people can secretly add gift wishes to a shared wishlist, but only the “organiser” can view them at the end.

**Requirements:**
- The program runs in a loop, asking each person for their name and a gift wish.
- After each entry, clear the screen (you can fake it by printing many newlines, or use `print("\n" * 100)`) so the next person can’t see previous wishes.
- Store the data in a dictionary: `wishlist = {"Alice": "book", "Bob": "chocolate"}`.
- After everyone has entered (the user types `"finish"` as the name to stop), the program asks for an organiser password (just set a hard‑coded password like `"admin"`). If correct, print all wishes. If wrong, say “Access denied” and exit.
- Bonus: If two people wish for the same item, print a warning at the end.

**Example flow:**
```
Name: Alice
Wish: a new bicycle

(clear screen)
Name: Bob
Wish: chocolate

(clear screen)
Name: finish

Enter organiser password: admin
--- Wishlist ---
Alice → a new bicycle
Bob → chocolate
```

---

## 💡 Tips for Success Today

- **Use `.get()`** (if you learn it in the course) to safely access dictionary values without crashing when a key is missing. If Angela doesn’t teach it today, you can use `if key in my_dict:` instead.
- **Nesting practice**: In the grade manager, you’ll have a dictionary where values are lists. That’s a classic nesting pattern you’ll use forever.
- **Looping on dictionaries**: You can loop over `my_dict.keys()`, `my_dict.values()`, or `my_dict.items()` to get key‑value pairs. Use what the lesson shows.
- **Start small**: Implement one menu option at a time, test it, then move to the next.

---

## 📤 After You’ve Built It

Post your code (for whichever project you choose) and I’ll give you a full review: logic, dictionary usage, edge cases, and any improvements. If you get stuck, ask for a **hint** before requesting the full solution—I’ll help you figure it out.

You’re doing brilliantly. This daily challenge routine will turn you into a fearless problem‑solver. Let’s see what you build today!