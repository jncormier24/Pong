from turtle import Turtle

class Ball(Turtle):
    pass

    def build(self, dx, dy):
        self.speed(0) # speed of animation
        self.shape("square")
        self.color("black")
        self.penup()
        self.goto(0, 0)
        self.dx = dx
        self.dy = dy