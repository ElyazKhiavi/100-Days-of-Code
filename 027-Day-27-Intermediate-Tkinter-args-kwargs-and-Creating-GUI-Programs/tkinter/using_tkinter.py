import tkinter as tk

BACK_GROUND_COLOR = "lavender"
FONT = ("Helvetica", 40)
root = tk.Tk()
root.configure(background=BACK_GROUND_COLOR)
root.title("TKinter Intro")
root.minsize(1500, 1500)
root.config(padx=200, pady=50)


label = tk.Label(root, text="This Label", font=FONT, bg=BACK_GROUND_COLOR).grid(
    row=0, column=0
)


button = tk.Button(root, text="Button", font=FONT).grid(row=1, column=1)
button = tk.Button(root, text="New Button", font=FONT).grid(row=0, column=2)


entry = tk.Entry(width=20, font=FONT)
entry.grid(row=2, column=3)
root.mainloop()
