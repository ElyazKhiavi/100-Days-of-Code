import random

words = [
    "baboon",
    "tooth",
    "balloon",
    "coffee",
    "cheese",
    "success",
    "letter",
    "kitten",
    "muffin",
    "summer",
    "banana",
    "potato",
    "tomato",
    "pepper",
    "radar",
    "level",
    "civic",
    "bookkeeper",
    "mississippi",
    "tennessee",
]

HANGMANPICS = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
]


def play_game():
    lives = 6
    chosen_word = random.choice(words)
    print(chosen_word)

    placeholder = ""
    for i in chosen_word:
        placeholder += "_"

    game_over = False
    correct_letters = []

    while not game_over:
        print(f"WORD: {placeholder}")
        print(f"LIVES: [{lives} ❤️ ]")
        guess_letter = input("Guess a Letter: ").lower()

        display = ""

        for letter in chosen_word:
            if letter == guess_letter:
                display += letter
                correct_letters.append(letter)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"
        placeholder=display

        if guess_letter in chosen_word:
            print("one step closer")
        elif guess_letter in correct_letters:
            print("You have already guessed that letter!")
        else:
            print("Wrong letter, you lost a life!")
            lives -= 1

        if display == chosen_word:
            game_over = True
            print("The noose is cut. You survive another day.")
        if lives == 0:
            game_over = True
            print("You lost")
        print(HANGMANPICS[lives])


play_game()
