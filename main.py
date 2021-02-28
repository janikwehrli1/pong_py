from turtle import Turtle, Screen
from players import Player
from ball import Ball
import time
from scoreboard import Scoreboard

myscreen = Screen()
myscreen.bgcolor("black")
myscreen.setup(width=800, height=600)
myscreen.tracer(0)

myscoreboard = Scoreboard()

r_player = Player((350, 0))
l_player = Player((-350, 0))
ball = Ball()

myscreen.listen()
myscreen.onkeypress(r_player.go_up, "Up")
myscreen.onkeypress(r_player.go_down, "Down")

myscreen.onkeypress(l_player.go_up, "w")
myscreen.onkeypress(l_player.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    myscreen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_player) < 50 and ball.xcor() > 320 or ball.distance(l_player) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        myscoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        myscoreboard.r_point()

myscreen.exitonclick()
