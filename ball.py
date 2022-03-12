from turtle import Turtle
import random


class Ball:
    def __init__(self):
        self.game_ball = Turtle()
        self.game_ball.shape("circle")
        self.game_ball.color("white")
        self.game_ball.penup()
        self.game_ball.goto(0, 0)
        self.x_move = 0
        self.y_move = 0
        self.assign_xy_movement()

    def assign_xy_movement(self):
        self.x_move = random.choice([10, -10])
        self.y_move = random.choice([10, -10])

    def reset_ball(self):
        self.game_ball.goto(0, 0)
        self.assign_xy_movement()

    def invert_x(self):
        self.x_move *= -1

    def invert_y(self):
        self.y_move *= -1

    def move_ball(self):
        self.game_ball.setx(self.game_ball.xcor() + self.x_move)
        self.game_ball.sety(self.game_ball.ycor() + self.y_move)

    def outbound(self):
        if self.game_ball.xcor() >= 390:
            return 1
        if self.game_ball.xcor() <= -395:
            return 2

    def wall_collision(self):
        if self.game_ball.ycor() >= 280 or self.game_ball.ycor() <= -280:
            self.invert_y()
