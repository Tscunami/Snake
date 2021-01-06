from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.refresh_score()

    def add_point(self):
        self.score += 1
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def clear_scoreboard(self):
        self.clear()
