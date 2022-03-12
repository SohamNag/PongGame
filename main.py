import time
from turtle import Screen
from pongboard import PongBoard
from scoreboard import ScoreBoard
from paddle import Paddle
from ball import Ball


def game_bye():
    global game_on
    game_on = False


screen = Screen()
game_on = True
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)
screen.listen()
pong = PongBoard()
player_score = ScoreBoard()
player_paddle1 = Paddle()
player_paddle1.player_paddle.goto(-380, 0)
player_paddle2 = Paddle()
player_paddle2.player_paddle.goto(372, 0)
player_ball = Ball()
screen.update()
while game_on:
    time.sleep(0.1)
    screen.onkeypress(player_paddle1.move_paddle_up, 'w')
    screen.onkeypress(player_paddle1.move_paddle_down, 's')
    screen.onkeypress(player_paddle2.move_paddle_up, 'Up')
    screen.onkeypress(player_paddle2.move_paddle_down, 'Down')
    player_ball.move_ball()
    if player_ball.outbound() == 1:
        player_score.increase_score1()
        player_ball.reset_ball()
    if player_ball.outbound() == 2:
        player_score.increase_score2()
        player_ball.reset_ball()
    if player_ball.game_ball.distance(player_paddle1.player_paddle) <= 30 or \
            player_ball.game_ball.distance(player_paddle2.player_paddle) <= 30:
        player_ball.invert_x()
    player_ball.wall_collision()
    screen.update()
    screen.onkeypress(game_bye, 'y')
