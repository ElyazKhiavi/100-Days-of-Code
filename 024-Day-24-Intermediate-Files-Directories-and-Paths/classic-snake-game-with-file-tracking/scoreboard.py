# ScoreBoard
import turtle

ALIGNMENT = "center"
NORMAL_FONT = ("Courier", 38, "italic")
GAME_OVER_FONT = ("Courier", 60, "italic")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.set_high_score()
        self.set_screen()
        self.update_screen()

    def set_screen(self):
        self.speed("fastest")
        self.goto(x=-50, y=820)
        self.color("white")
        self.penup()
        self.hideturtle()

    def update_screen(self):
        self.clear()
        self.write(
            f"Score: {self.score} - High Score: {self.high_score}",
            False,
            ALIGNMENT,
            NORMAL_FONT,
        )

    def update_score(self):
        self.score += 1
        self.update_screen()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.save_high_score()
        self.score = 0
        self.update_screen()

    def set_high_score(self):
        with open("high_score.txt", "r") as f:
            high_score = f.read() 
        if high_score: # if it's not empty 
            try:
                high_score =  int(high_score) # if it's not a number we don't get get error for trying to convert it 
            except ValueError:
                print("Invalid data in the file!")
                high_score = 0
            return high_score
        return 0 # if it was empty then we just set it to zero the save high score we handle it from here 

    def save_high_score(self):
        with open("high_score.txt", "w") as f:
            f.write(str(self.high_score))

    # def game_over(self):
    #     self.color('red')
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", False, ALIGNMENT, GAME_OVER_FONT)
