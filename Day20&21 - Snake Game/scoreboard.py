from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.currentScore = 0
        self.hideturtle()
        self.updateScoreBoard()


    def updateScoreBoard(self):
        self.write(f"Score : {self.currentScore}", align= ALIGNMENT, font= FONT)


    def addScore(self):
        self.currentScore += 1
        self.clear()
        self.updateScoreBoard()

    def gameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER !!", align= ALIGNMENT, font= FONT)