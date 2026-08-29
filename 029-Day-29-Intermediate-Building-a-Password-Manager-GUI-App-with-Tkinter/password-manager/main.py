import tkinter as tk
import re
import secrets
import pyperclip
import tkinter.messagebox as msg

ALPHABET = r"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
IMAGE_URL = "./assets/big_logo.png"
DATA_FILE_URL = "./data.txt"
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

EMAIL_HOLDER = "email@email.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    return "".join(secrets.choice(ALPHABET) for i in range(26))


def add_password_to_entry():
    password = generate_password()
    pyperclip.copy(password)
    print(password)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


# ---------------------------- CHECK ENTRY ------------------------------- #


def check_username(username: str) -> bool:
    """Return True if username length > 5."""
    return len(username) > 5


def check_password(password: str) -> bool:
    """Return True if password length > 8, contains at least one uppercase and one digit."""
    if len(password) <= 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    return True


def check_website(website: str) -> bool:
    """
    Return True if website matches <site>.<domain> where both parts consist of
    letters, digits, or hyphens. Any domain extension is allowed.
    """
    # Regex: one or more alnum/hyphen, a dot, then one or more alnum/hyphen
    pattern = r"^[A-Za-z0-9-]+\.[A-Za-z0-9-]+$"
    return re.match(pattern, website) is not None


# ---------------------------- SAVE PASSWORD ------------------------------- #


def check_file():
    try:
        with open(DATA_FILE_URL, "r") as f:
            print("file exists")
            return True
    except FileNotFoundError:
        print("file does not exist")
        return False


def show_warning_message(type: str, message: str) -> None:
    msg.showerror(type, message)


def add_to_data() -> None:
    website = website_name_entry.get().strip()
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not check_password(password):
        show_warning_message(
            "Invalid Password",
            "Password must exceed 8 characters, include at least one uppercase letter and one digit",
        )
        return False

    if not check_username(username):
        show_warning_message(
            "Invalid Username", "Username must be longer than 5 characters"
        )
        return False

    if not check_website(website):
        show_warning_message(
            "Invalid Website URL",
            "Website must follow the format 'site.domain' (any domain).",
        )
        return False

    confirm = msg.askokcancel(
        title="Confirm User/Pass",
        message=f"These are the information you entered:\nUsername: {username}\Password: {password}\nWebsite: {website}\nDo you want to proceed?",
        icon="question",
    )
    if not confirm:
        return False

    if not check_file():
        with open(DATA_FILE_URL, "w") as f:
            f.write("WEBSITE | EMAIL/USERNAME | PASSWORD")
            print("file created \nWEBSITE | EMAIL/USERNAME | PASSWORD")

    with open(DATA_FILE_URL, "a") as f:
        f.write(f"\n{website} | {username} | {password}")
        print("password added", f"{website} | {username} | {password}")

    msg.showinfo(
        "Password Added", f"Your User/Pass for {website} were added successfully."
    )
    website_name_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    return True


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
    insertwidth=15,
)
website_name_entry.grid(row=1, column=1, columnspan=2, sticky="W")
website_name_entry.focus()

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
    insertwidth=15,
)
username_entry.insert(0, EMAIL_HOLDER)
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
    insertwidth=15,
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
    command=add_password_to_entry,
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
    command=add_to_data,
)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")

root.mainloop()