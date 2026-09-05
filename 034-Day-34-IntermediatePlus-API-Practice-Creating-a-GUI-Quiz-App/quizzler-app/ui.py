import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
GREEN = "#008744"
RED = "#d62d20"
BLUE = "#0057e7"
WHITE = "white"

WINDOW_PADDING = 75

SCORE_FONT = ("Helvetica", 40, "italic")
FONT = ("Helvetica", 48, "italic")

RIGHT_IMG = "./images/true.png"
WRONG_IMG = "./images/false.png"


class UI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain

        self.root = tk.Tk()
        self.root.title("Quizzler")
        self.root.config(padx=WINDOW_PADDING, pady=WINDOW_PADDING, bg=THEME_COLOR)

        self.score_label = tk.Label(
            self.root,
            font=SCORE_FONT,
            bg=THEME_COLOR,
            fg="white",
        )
        self.score_label.grid(row=0, column=1, sticky="e", pady=20)

        self.question_text = tk.Label(
            fg=THEME_COLOR,
            width=27,
            height=10,
            padx=20,
            pady=50,
            justify="center",
            wraplength=850,
            bg="white",
            font=FONT,
        )
        self.question_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        right_img = tk.PhotoImage(file=RIGHT_IMG)
        wrong_img = tk.PhotoImage(file=WRONG_IMG)

        self.right_button = tk.Button(
            self.root,
            image=right_img,
            highlightthickness=0,
            borderwidth=0,
            bg=THEME_COLOR,
            command=self.click_button,
        )
        self.right_button.grid(row=2, column=1, padx=50, pady=50)

        self.wrong_button = tk.Button(
            self.root,
            image=wrong_img,
            highlightthickness=0,
            borderwidth=0,
            bg=THEME_COLOR,
            command=lambda: self.click_button(False),
        )
        self.wrong_button.grid(row=2, column=0, padx=50, pady=50)

        self.change_text()  # call it once so that the placeholder get's replaced from the get go
        self.root.mainloop()

    def change_text(self):
        self.question_text.config(
            text=self.quiz_brain.show_question(),
            bg=WHITE,
        )
        self.score_label.config(
            text=f"Score: {self.quiz_brain.score}/{self.quiz_brain.current_question_number}",
        )

    def click_button(self, answer=True):

        if answer:
            is_true = self.quiz_brain.check_answer("true")
        else:
            is_true = self.quiz_brain.check_answer("false")

        if is_true:
            self.question_text.config(
                bg=GREEN,
            )
        else:
            self.question_text.config(bg=RED)

        if self.quiz_brain.quiz_finished():
            self.score_label.config(
                text=f"Score: {self.quiz_brain.score}/{self.quiz_brain.current_question_number}"
            )
            self.question_text.config(
                text=f"Completed!\nFinal Score:\n{self.quiz_brain.score}/{self.quiz_brain.current_question_number}",
                bg=BLUE,
            )
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
            return

        self.root.after(700, self.change_text)

    def __str__(self):
        return "TKinter UI for 'Quizller' app"
