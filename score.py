from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Console", 12, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def score_plus(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
