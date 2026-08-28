import tkinter as tk
import secrets

IMAGE_URL = "./big_logo.png"
IMAGE_WIDTH = 617
IMAGE_HEIGHT = 650

ENTRY_EXPANSION = 40
GENERATE_EXPANSION = 18
PASSWORD_ENTRY_EXPANSION = 27
ADD_BUTTON_EXPANSION = 40

FONT = ("Courier", 40)
DARK_COLOR = "#15161a"
GREY_COLOR = "#787d8a"
RED_COLOR = "#800a25"
WHITE_COLOR = "#bbbbbb"
DARKER_WHITE_COLOR = "#aaaaaa"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

alphabet = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
password = ''.join(secrets.choice(alphabet) for i in range(32))


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


# Canvas
root = tk.Tk()
root.config(background=GREY_COLOR, padx=150, pady=150)
root.title("Password Manager App")

canvas_body = tk.Canvas(
    root, height=IMAGE_HEIGHT, width=IMAGE_WIDTH, bg=GREY_COLOR, highlightthickness=0
)
lock_logo = tk.PhotoImage(file=IMAGE_URL)
canvas_body.create_image(IMAGE_WIDTH // 2, IMAGE_HEIGHT // 2, image=lock_logo)
canvas_body.grid(row=0, column=0, columnspan=3)


# Form

website_label = tk.Label(
    root, text="Website: ", fg=RED_COLOR, bg=GREY_COLOR, font=FONT, pady=10
).grid(row=1, column=0, sticky="W")
website_name_entry = tk.Entry(
    root,
    font=FONT,
    width=ENTRY_EXPANSION,
    bg=WHITE_COLOR,
    borderwidth=0,
    highlightthickness=0,
)
website_name_entry.grid(row=1, column=1, columnspan=2, sticky="W")


username_label = tk.Label(
    root, text="Email/Username: ", fg=RED_COLOR, bg=GREY_COLOR, font=FONT, pady=10
).grid(row=2, column=0, sticky="W")
username_entry = tk.Entry(
    root,
    font=FONT,
    width=ENTRY_EXPANSION,
    bg=WHITE_COLOR,
    borderwidth=0,
    highlightthickness=0,
)
username_entry.grid(row=2, column=1, columnspan=2, sticky="W")


password_label = tk.Label(
    root, text="Password: ", fg=RED_COLOR, bg=GREY_COLOR, font=FONT, pady=10
).grid(row=3, column=0, sticky="W")
password_entry = tk.Entry(
    root,
    font=FONT,
    width=PASSWORD_ENTRY_EXPANSION,
    bg=WHITE_COLOR,
    borderwidth=0,
    highlightthickness=0,
)
password_entry.grid(row=3, column=1, sticky="W")

generate_password_button = tk.Button(
    root,
    text="Generate Password",
    font=("Currier", 32),
    width=GENERATE_EXPANSION,
    bg=DARKER_WHITE_COLOR,
    fg=RED_COLOR,
    borderwidth=0,
    highlightthickness=0,
)
generate_password_button.grid(
    row=3,
    column=2,
    sticky="E",
)


tk.Label(root, text="", pady=35, bg=GREY_COLOR).grid(row=4, column=0)
add_button = tk.Button(
    root,
    text="Add",
    font=FONT,
    width=ADD_BUTTON_EXPANSION,
    bg=DARKER_WHITE_COLOR,
    fg=RED_COLOR,
    borderwidth=0,
    highlightthickness=0,
)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")


root.mainloop()
