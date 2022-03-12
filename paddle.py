from turtle import Turtle


class Paddle:
    def __init__(self):
        self.player_paddle = self.make_paddle()

    def make_paddle(self):
        paddle = Turtle()
        paddle.shape("square")
        paddle.shapesize(1, 3, 1)
        paddle.setheading(90)
        paddle.color('white')
        paddle.penup()
        return paddle

    def move_paddle_up(self):
        if self.player_paddle.ycor() <= 250:
            self.player_paddle.forward(20)

    def move_paddle_down(self):
        if self.player_paddle.ycor() >= -240:
            self.player_paddle.back(20)
