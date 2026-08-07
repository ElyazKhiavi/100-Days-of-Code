import random
from hangman_words import impossible_words, hard_words, intermediate_words, easy_words
from hangman_logo import logo, HANGMANPICS

print(logo)
print("Welcome to Hangman. Think you can survive?")


def play_game():
    while True:
        difficulty = input(
            "Set the stakes: Easy(e), Medium(m), Hard(h), or Impossible(i).\n====> "
        ).lower()  # easy , medium, hard , impossible
        if difficulty == "e":
            word = random.choice(easy_words)
            break
        elif difficulty == "m":
            word = random.choice(intermediate_words)
            break
        elif difficulty == "h":
            word = random.choice(hard_words)
            break
        elif difficulty == "i":
            word = random.choice(impossible_words)
            break
        else:
            print("There is no such level!")

    placeholder = ""
    for i in word:
        placeholder += "_"

    letter_list = []
    lives = 6
    game_over = False
    while not game_over:
        print(f"Word: {placeholder}")
        print(f"Lives: [{lives}]")
        print(HANGMANPICS[lives])

        guess = input("Guess a letter: ").lower()

        if guess in letter_list:
            print("You've already guessed that letter!")
        elif guess in word:
            print("Correct! One step closer to freedom.")
        else:
            print("Incorrect. One life lost.")
            lives -= 1

        display = ""
        for letter in word:
            if guess == letter:
                display += letter
                letter_list.append(guess)
            elif letter in letter_list:
                display += letter
            else:
                display += "_"
        placeholder = display

        if word == display:
            game_over = True
            print(HANGMANPICS[lives])
            print("You solved it!")
            print(f"The word was: [{word}]")
            print("The noose is cut. You survive another day.")
        elif lives == 0:
            game_over = True
            print(HANGMANPICS[lives])
            print(f"The word was: [{word}]")
            print("The trapdoor opens. You hang.")
            print("Game over.")


def main():
    play_game()
    while True:
        play_again = input("Play again? (y/n)").lower()
        if play_again == "y":
            print("Alright. One more round")
            play_game()
        elif play_again == "n":
            print("You walked away from the gallows.")
            print("Until next time...")
            break


main()
