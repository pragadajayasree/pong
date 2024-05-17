from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_c = 10
        self.y_c = 10
        self.speed = 0.1
        self.create()

    def create(self):
        self.shape("circle")
        self.penup()
        self.color("white")
        self.home()

    def move(self):
        x = self.xcor()+self.x_c
        y = self.ycor()+self.y_c
        self.goto(x, y)

    def bounce_y(self):
        self.y_c *= -1

    def bounce_x(self):
        self.x_c *= -1
        self.speed *= 0.9

    def reposition(self):
        self.home()
        self.speed = 0.1
        self.bounce_x()
