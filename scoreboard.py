from turtle import Turtle


class ScoreBoard:
    def __init__(self):
        self.score1 = 0
        self.score2 = 0
        self.draw1 = Turtle()
        self.draw2 = Turtle()
        self.score_board()

    def score_board(self):
        self.draw1.hideturtle()
        self.draw1.penup()
        self.draw1.color("white")
        self.draw1.goto(-60, 270)
        self.draw1.pendown()
        self.draw1.write(arg="Player 1", font=("Ariel", 10, "normal"))
        self.draw1.penup()
        self.draw1.goto(-40, 240)
        self.draw1.pendown()
        self.draw1.write(arg=f"{self.score1}", font=('Ariel', 12, 'normal'))
        self.draw2.hideturtle()
        self.draw2.penup()
        self.draw2.color("white")
        self.draw2.goto(13, 270)
        self.draw2.pendown()
        self.draw2.write(arg="Player 2", font=("Ariel", 10, "normal"))
        self.draw2.penup()
        self.draw2.goto(35, 240)
        self.draw2.pendown()
        self.draw2.write(arg=f"{self.score2}", font=('Ariel', 12, 'normal'))

    def increase_score1(self):
        self.score1 += 1
        self.draw1.clear()
        self.score_board()

    def increase_score2(self):
        self.score2 += 1
        self.draw2.clear()
        self.score_board()
