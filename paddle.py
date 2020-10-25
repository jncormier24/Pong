from turtle import Turtle

class Paddle(Turtle):
    pass

    def build(self, xpos, ypos, name='paddle'):
        self.name=name
        self.speed(0) # speed of animation
        self.shape("square")
        self.color("black")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(xpos, ypos)


    def moveUp(self, distance=20):
        ycoord = self.ycor()
        ycoord += distance
        self.sety(ycoord)

    def moveDown(self, distance=20):
        ycoord = self.ycor()
        ycoord -= distance
        self.sety(ycoord)
