from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.ini(x, y)

    def ini(self, x, y):
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)


    def up(self):
        x = self.xcor()
        y = self.ycor()+20
        self.goto(x, y)

    def down(self):
        x = self.xcor()
        y = self.ycor() - 20
        self.goto(x, y)

