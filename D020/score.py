from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.high_score = 0
        with open("high_score.txt") as high_score_file:
            self.high_score = int(high_score_file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as high_score_file:
                high_score_file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
