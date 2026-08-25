import tkinter as tk

BACK_GROUND_COLOR = "lavender"

root = tk.Tk()
root.title("Miles To KM Convertor")
root.minsize(1000, 700)
root.config(padx=200, pady=50, bg=BACK_GROUND_COLOR)


def km_to_ml():
    num = int(entry.get())
    value = round(num * 1.609, 2)
    answer.config(text=value)


entry = tk.Entry(width=10, font=("helvetica", 32))
entry.grid(row=1, column=2)

tk.Label(root, text="Miles", font=("helvetica", 32), bg=BACK_GROUND_COLOR).grid(
    row=1, column=3
)

tk.Label(root, text="is equal to", font=("helvetica", 32), bg=BACK_GROUND_COLOR).grid(
    row=2, column=1
)

answer = tk.Label(
    root, text=0, font=("helvetica", 32), bg=BACK_GROUND_COLOR
)
answer.grid(row=2, column=2) 

tk.Label(root, text="Km", font=("helvetica", 32), bg=BACK_GROUND_COLOR).grid(
    row=2, column=3
)

calculate = tk.Button(root, text="Calculate", command=km_to_ml, font=("helvetica", 32))
calculate.grid(row=3, column=2)


root.mainloop()
