from turtle import Turtle


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(y=new_y, x=self.xcor())

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(y=new_y, x=self.xcor())
