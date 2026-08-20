## 🛠️ Project 1: Password Strength Checker

Build a program that evaluates how strong a given password is, based on a set of rules. The user enters a password, and the program gives it a score out of 5 and provides feedback on how to improve it.

### Requirements

1. Create a function `check_password_strength(password)` that returns a score (0–5) and a list of messages (e.g., “Add uppercase letters”).
2. The function should check for:
   - Length >= 8 characters
   - Contains at least one uppercase letter (A–Z)
   - Contains at least one lowercase letter (a–z)
   - Contains at least one digit (0–9)
   - Contains at least one special character from `!@#$%^&*()_+-=[]{}|;:'\",.<>?/~` (you can define your own set)
3. If the password meets a criterion, add 1 to the score. If not, add a specific suggestion to a feedback list.
4. In the `main()` function:
   - Ask the user to enter a password.
   - Call the checker, then print the score and any improvement tips.
   - Keep asking for a password until the user types `quit`.
5. **Tip:** Use string methods like `.isupper()`, `.islower()`, `.isdigit()`, but for special characters you’ll need to loop and check if each character is in your special list.

### Example Run

```
Password Strength Checker
Enter a password (or 'quit' to exit): hello
Score: 1/5
Suggestions:
- Add at least 8 characters
- Add uppercase letters
- Add digits
- Add special characters

Enter a password (or 'quit' to exit): Hello123!
Score: 5/5
Your password is strong!

Enter a password (or 'quit' to exit): quit
Goodbye!
```

---

## 🎮 Project 2: Rock‑Paper‑Scissors Championship

Extend the classic rock‑paper‑scissors into a best‑of‑N tournament. The player chooses how many rounds to win (e.g., first to 3). The computer picks randomly, and after each round the scores are shown.

### Requirements

1. Write a function `get_computer_choice()` that returns a random choice from `["rock", "paper", "scissors"]`.
2. Write a function `determine_winner(player, computer)` that returns `"player"`, `"computer"`, or `"tie"`. The rules are standard (rock beats scissors, scissors beats paper, paper beats rock).
3. Write a function `play_round()` that:
   - Asks the user for their choice (validate input: must be rock, paper, or scissors – keep asking if invalid).
   - Gets the computer’s choice.
   - Prints both choices and the round result.
   - Returns the result (`"player"`, `"computer"`, `"tie"`).
4. In `main()`:
   - Ask how many wins are needed to become champion (e.g., 3).
   - Loop until either the player or computer reaches that number of wins.
   - Display the running score after each round.
   - After the match, announce the champion and ask if they want to play again.
5. **Extra challenge:** Add "lizard" and "spock" (from Big Bang Theory) to make it Rock‑Paper‑Scissors‑Lizard‑Spock. The rules: scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, rock crushes scissors. (You’ll need to update the winner logic accordingly.)

### Example Run

```
Welcome to the Rock‑Paper‑Scissors Championship!
How many wins to become champion? 3

Round 1: Player 0 – Computer 0
Choose rock, paper, or scissors: rock
Computer chose scissors. You win this round!

Round 2: Player 1 – Computer 0
Choose rock, paper, or scissors: paper
Computer chose paper. It's a tie!

...

Player wins the championship 3‑1!
Play again? (yes/no): no
Thanks for playing!
```

---

## 💡 Hints for Both Projects (Without Spoilers)

- **Use functions liberally** – each small job gets its own function, just like in the Caesar cipher.
- **Input validation without try/except:** For Rock‑Paper‑Scissors, you can use `while choice not in ["rock", "paper", "scissors"]`. For the password checker, you don’t need to reject input – just evaluate whatever the user types.
- **Keep score with variables** in `main()`, passing them to functions or updating them based on return values.
- **Loop until exit condition** is a classic `while True` with a `break` when `"quit"` is entered or the game ends.
- **For the special character check** in the password project, make a string like `special_chars = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/~"` and use a loop with `if char in special_chars`.



# final touches




🧠 Time Management Tips (from this experience)

    Pick one project and finish it completely before moving on. A 90‑minute block for one project would have given you a fully polished piece.

    Pseudocode on paper first – it prevents mid‑code direction changes that break logic (like your scoring reversal).

    Test often – after each small addition, run the code. If you’d tested the uppercase/lowercase detection with "hello", you’d have seen the bug instantly.

    Return values immediately – when a function is meant to provide a result, always put the return statement before you forget.

    Don’t be afraid to rewrite small chunks – the moment you feel tangled, save a copy and restart the problematic function with fresh logic.