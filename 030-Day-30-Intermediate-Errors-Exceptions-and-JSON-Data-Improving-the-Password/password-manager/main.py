import tkinter as tk
import tkinter.messagebox as msg
import re
import secrets
import pyperclip
import json

ALPHABET = r"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
IMAGE_URL = "./logo.png"
DATA_FILE_URL = "./data.json"
IMAGE_WIDTH = 617
IMAGE_HEIGHT = 650


WEBSITE_ENTRY_EXPANSION = 28
SEARCH_BUTTON_EXPANSION = 10

PASSWORD_ENTRY_EXPANSION = 26
GENERATE_PASSWORD_EXPANSION = 18
EMAIL_ENTRY = 38
ADD_BUTTON = 38


FONT = ("Courier", 40)
DARK_COLOR = "#15161a"
GREY_COLOR = "#787d8a"
RED_COLOR = "#800a25"
WHITE_COLOR = "#bbbbbb"
DARKER_WHITE_COLOR = "#aaaaaa"

EMAIL_HOLDER = "dante@gmail.com"


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
    return len(username) > 5


def check_password(password: str) -> bool:
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    return True


def check_website(website: str) -> bool:
    pattern = r"""^[A-Za-z0-9-]+\.[A-Za-z0-9-]+$"""
    return re.match(pattern, website) is not None


# ---------------------------- SAVE PASSWORD ------------------------------- #


def show_warning_message(type: str, message: str) -> None:
    msg.showerror(type, message)


def add_to_data() -> bool:
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
        title="Confirm User-Pass",
        message=f"These are the information you entered:\nUsername: {username}\nPassword: {password}\nWebsite: {website}\nDo you want to proceed?",
        icon="question",
    )
    if not confirm:
        return False

    # _________________________ Add to Json File ______________________
    try:
        with open(DATA_FILE_URL, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    data[website] = {
        "username": username,
        "password": password,
    }

    with open(DATA_FILE_URL, "w") as f:
        json.dump(data, f, indent=4)
    # ------------------------------------------------------------------

    msg.showinfo(
        "Password Added", f"Your User-Pass for {website} were added successfully."
    )
    website_name_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    username_entry.insert(0, EMAIL_HOLDER)
    password_entry.delete(0, tk.END)
    return True


# ---------------------------- Search Passwords ------------------------------- #


def search_websites() -> None:
    """Search for the website name in the json file if the website is found show info and copy to clipboard with pyperclip, if it is not found show error message"""
    website_name = website_name_entry.get().strip()
    try:
        with open(DATA_FILE_URL, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return msg.showerror(f"File Note Found", f"{DATA_FILE_URL} was NOT Found!!!")

    if website_name in data:
        username = data[website_name]["username"]
        password = data[website_name]["password"]
        msg.showinfo(
            f"{website_name} Info",
            f"Username: {username}\nPassword: {password}",
        )
        pyperclip.copy(username)
        pyperclip.copy(password)

    else:
        msg.showerror(f"{website_name} Info", "Not Found!!!")


# ---------------------------- UI SETUP ------------------------------- #

root = tk.Tk()
root.config(background=GREY_COLOR, padx=100, pady=50)
root.title("Password Manager App")

canvas_body = tk.Canvas(
    root, height=IMAGE_HEIGHT, width=IMAGE_WIDTH, bg=GREY_COLOR, highlightthickness=0
)
lock_logo = tk.PhotoImage(file=IMAGE_URL)
canvas_body.create_image(IMAGE_WIDTH // 2, IMAGE_HEIGHT // 2, image=lock_logo)
canvas_body.grid(row=0, column=0, columnspan=3)


# ---- Form ---

# Website Name

website_label = tk.Label(
    root, text="Website: ", fg=RED_COLOR, bg=GREY_COLOR, font=FONT, pady=10
).grid(row=1, column=0, sticky="W")
website_name_entry = tk.Entry(
    root,
    font=FONT,
    width=WEBSITE_ENTRY_EXPANSION,
    bg=WHITE_COLOR,
    borderwidth=0,
    highlightthickness=0,
    insertwidth=15,
)
website_name_entry.grid(row=1, column=1, sticky="W")
website_name_entry.focus()


website_search_button = tk.Button(
    root,
    text="SEARCH",
    font=("Currier", 28),
    width=SEARCH_BUTTON_EXPANSION,
    bg=DARKER_WHITE_COLOR,
    fg=RED_COLOR,
    borderwidth=0,
    highlightthickness=0,
    command=search_websites,
)
website_search_button.grid(
    row=1,
    column=2,
    sticky="E",
)


# Email or Username
username_label = tk.Label(
    root, text="Email/Username: ", fg=RED_COLOR, bg=GREY_COLOR, font=FONT, pady=10
).grid(row=2, column=0, sticky="W")
username_entry = tk.Entry(
    root,
    font=FONT,
    width=EMAIL_ENTRY,
    bg=WHITE_COLOR,
    borderwidth=0,
    highlightthickness=0,
    insertwidth=15,
)
username_entry.insert(0, EMAIL_HOLDER)
username_entry.grid(row=2, column=1, columnspan=2, sticky="W")


# Password

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
    font=("Currier", 24),
    width=GENERATE_PASSWORD_EXPANSION,
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


# Add to file

tk.Label(root, text="", pady=35, bg=GREY_COLOR).grid(row=4, column=0)
add_button = tk.Button(
    root,
    text="Add",
    font=FONT,
    width=ADD_BUTTON,
    bg=DARKER_WHITE_COLOR,
    fg=RED_COLOR,
    borderwidth=0,
    highlightthickness=0,
    command=add_to_data,
)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")

root.mainloop()
