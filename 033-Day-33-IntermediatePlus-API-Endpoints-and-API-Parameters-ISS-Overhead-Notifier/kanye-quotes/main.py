from tkinter import *
import requests


def get_quote():
    connection = requests.get("https://api.kanye.rest/")
    connection.raise_for_status()

    quote = connection.json()["quote"]
    canvas.itemconfig(quote_text, text=quote)
    return True, quote


window = Tk()
window.title("Kanye Says...")
window.config(padx=100, pady=100)

canvas = Canvas(width=600, height=828)
background_img = PhotoImage(file="background.png")
canvas.create_image(300, 414, image=background_img)
quote_text = canvas.create_text(
    300,
    414,
    text="Kanye Quote Goes HERE",
    width=414,

    font=("Arial", 30, "bold"),
    fill="white",
    
)
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
