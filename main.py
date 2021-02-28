from turtle import Turtle, Screen
from players import Player

myscreen = Screen()
myscreen.bgcolor("black")
myscreen.setup(width=800, height=600)
myscreen.tracer(0)


newplayer = Player()

myscreen.listen()
myscreen.onkeypress(newplayer.go_up, "Up")
myscreen.onkeypress(newplayer.go_down, "Down")

game_is_on = True
while game_is_on:
    myscreen.update()


myscreen.exitonclick()