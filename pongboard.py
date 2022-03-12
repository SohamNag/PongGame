from turtle import Turtle


class PongBoard:
    def __init__(self):
        self.divide_screen()

    def divide_screen(self):
        divider = Turtle()
        divider.hideturtle()
        divider.speed("fastest")
        divider.color("white")
        divider.pensize(6)
        divider.penup()
        divider.goto(0, -270)
        divider.setheading(90)
        for i in range(19):
            divider.pendown()
            divider.forward(15)
            divider.penup()
            divider.forward(15)
