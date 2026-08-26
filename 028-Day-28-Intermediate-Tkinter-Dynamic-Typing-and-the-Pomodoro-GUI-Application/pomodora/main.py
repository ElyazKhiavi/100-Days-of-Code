import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
IMAGE_ADDRESS = "./big_tomato.png"
IMAGE_WIDTH = 600
IMAGE_HEIGHT = 669
reps = 0
p_timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps, p_timer
    root.after_cancel(p_timer)
    reps = 0

    check_mark.config(text="")
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    count = None

    if reps % 8 == 0:
        count = long_break
        label.config(text="Break", fg=RED)
        check_mark.config(text="✓" * (int(reps // 8)))
    elif reps % 2 == 0:
        count = short_break
        label.config(text="Break", fg=PINK)
    else:
        count = work_secs
        label.config(text="Work", fg=GREEN)
    count_down(count)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# Recursion is bad though!!
def count_down(count):

    mins_left = int(count // 60)
    secs_left = int(count % 60)

    canvas.itemconfig(
        timer_text,
        text=f'{mins_left if mins_left > 9 else f"0{mins_left}"}:{secs_left if secs_left > 9 else f"0{secs_left}"}',
    )
    if count > 0:
        global p_timer
        p_timer = root.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

root = tk.Tk()
root.title("Pomodora Project")
root.config(background=YELLOW)
root.config(padx=100, pady=100)

# The Title Text
label = tk.Label(
    root, text="Timer", font=(FONT_NAME, 100, "bold"), fg=GREEN, bg=YELLOW, pady=15
)
label.grid(row=0, column=1)

# Canvas Tomato
canvas = tk.Canvas(
    root, width=IMAGE_WIDTH, height=IMAGE_HEIGHT, bg=YELLOW, highlightthickness=0
)
tomato_img = tk.PhotoImage(file=IMAGE_ADDRESS)
canvas.create_image(IMAGE_WIDTH // 2, IMAGE_HEIGHT // 2, image=tomato_img)
timer_text = canvas.create_text(
    IMAGE_WIDTH // 2,
    (IMAGE_HEIGHT // 2) + 50,
    text="00:00",
    font=(FONT_NAME, 84, "bold"),
    fill=GREEN,
)
canvas.grid(row=1, column=1)


# Check mark label

check_mark = tk.Label(root, text="", font=(FONT_NAME, 60), fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)

# Buttons
start_btn = tk.Button(
    root, text="Start", command=start_timer, font=(FONT_NAME, 40), highlightthickness=0
)
start_btn.grid(row=2, column=0)

reset_btn = tk.Button(
    root, text="Reset", command=reset_timer, font=(FONT_NAME, 40), highlightthickness=0
)
reset_btn.grid(row=2, column=2)


root.mainloop()
