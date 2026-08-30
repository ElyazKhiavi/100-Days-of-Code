import tkinter as tk
import pandas as pd
import random

### --------------------------------------- Constants --------------------------------------- ###
BACKGROUND_COLOR = "#B1DDC6"

CARD_WIDTH = 1600
CARD_HEIGHT = 1200


CARD_TITLE_TEXT_WIDTH = 800
CARD_TITLE_TEXT_HEIGHT = 380

CARD_WORD_TEXT_WIDTH = 800
CARD_WORD_TEXT_HEIGHT = 600


CARD_BACK_IMG = "./images/card_back.png"
CARD_FRONT_IMG = "./images/card_front.png"

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 200

RIGHT_IMG = "./images/right.png"
WRONG_IMG = "./images/wrong.png"


DATA_FR = "./data/french_words.csv"
DATA_GR = "./data/german_words.csv"

TO_LEARN = "./data/to_learn.csv"


LANGUAGE_1 = "English"
LANGUAGE_2 = "French"


TITLE_FONT = ("Helvetica", 72, "italic")
WORD_FONT = ("Helvetica", 100, "bold")

TIMER_TIME = 2000

### --------------------------------------- LOGIC --------------------------------------- ###


try:
    data = pd.read_csv(TO_LEARN)
except FileNotFoundError:
    data = pd.read_csv(DATA_FR)

words_list = data.to_dict(orient="records")

timer_id = None
current_word = None


def next_word():
    global timer_id, current_word
    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None

    if words_list:
        current_word = random.choice(words_list)
        german_word = current_word[LANGUAGE_2]  # Change to the csv language

        card_canvas.itemconfig(card_title_text, text=LANGUAGE_2, fill="black")
        card_canvas.itemconfig(card_word_text, text=german_word, fill="black")
        card_canvas.itemconfig(card_image, image=front_pic)

        timer_id = root.after(TIMER_TIME, func=flip_card)
    else:
        card_canvas.itemconfig(card_title_text, text="Completed", fill="white")
        card_canvas.itemconfig(card_word_text, text="Way to Go!!", fill="white")
        card_canvas.itemconfig(card_image, image=back_pic)
        right_button.grid_remove()
        wrong_button.grid_remove()


def flip_card():
    global timer_id, current_word

    english_word = current_word[LANGUAGE_1]

    card_canvas.itemconfig(card_title_text, text=LANGUAGE_1, fill="white")
    card_canvas.itemconfig(card_word_text, text=english_word, fill="white")
    card_canvas.itemconfig(card_image, image=back_pic)

    timer_id = None


def known_word():
    """Save the words that are left to a CSV and then resume to the next work"""

    if words_list:
        print(len(words_list))
        words_list.remove(current_word)

        df = pd.DataFrame(words_list)
        df.to_csv(TO_LEARN, index=False)  # this index false is very important

        next_word()


### --------------------------------------- UI --------------------------------------- ###


root = tk.Tk()
root.title("Flash Card Game")
root.config(padx=200, pady=100, background=BACKGROUND_COLOR)


# Card
card_canvas = tk.Canvas(
    root,
    height=CARD_HEIGHT,
    width=CARD_WIDTH,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    borderwidth=0,
)
front_pic = tk.PhotoImage(file=CARD_FRONT_IMG)
back_pic = tk.PhotoImage(file=CARD_BACK_IMG)

card_image = card_canvas.create_image(
    CARD_WIDTH // 2, CARD_HEIGHT // 2, image=front_pic
)

card_title_text = card_canvas.create_text(
    CARD_TITLE_TEXT_WIDTH, CARD_TITLE_TEXT_HEIGHT, text="", font=TITLE_FONT
)
card_word_text = card_canvas.create_text(
    CARD_WORD_TEXT_WIDTH, CARD_WORD_TEXT_HEIGHT, text="", font=WORD_FONT
)
card_canvas.grid(row=0, column=0, columnspan=2)


# Right Button
right_pic = tk.PhotoImage(file=RIGHT_IMG)
right_button = tk.Button(
    root, image=right_pic, borderwidth=0, highlightthickness=0, command=known_word
)
right_button.grid(row=1, column=1)


# Wrong Button
wrong_pic = tk.PhotoImage(file=WRONG_IMG)
wrong_button = tk.Button(
    root, image=wrong_pic, borderwidth=0, highlightthickness=0, command=next_word
)
wrong_button.grid(row=1, column=0)


next_word()

root.mainloop()
