import tkinter as tk

BACK_GROUND_COLOR = "lavender"

root = tk.Tk()
root.configure(background=BACK_GROUND_COLOR)
root.title("TKinter Intro")
root.minsize(1500, 1500)


# Label
my_label = tk.Label(text="Write here", font=("Helvetica", 40), bg=BACK_GROUND_COLOR)
my_label["text"] = "Like this as dict keys"
my_label.config(text="With config")
my_label.grid(row=1, column=1)


# Button
def write_sth():
    my_label.config(text=txt.get().title(), fg="red", font=("utopia", 48))


next = [4]


def submit():
    num = next[0]
    tk.Label(
        root, text=txt.get(), fg="red", bg=BACK_GROUND_COLOR, font=("utopia", 48)
    ).grid(row=num, column=2)
    next[0] += 1


button = tk.Button(text="Click Me!!!", font=("Helvetica", 32), command=write_sth)
button.grid(row=2, column=2)


# Entry

txt = tk.Entry(width=20, font=("helvetica", 34))
txt.grid(row=3, column=0)

sub = tk.Button(
    root, text="Submit", font=("Helvetica", 28), fg="purple", command=submit
)
sub.grid(row=3, column=1)


root.mainloop()
