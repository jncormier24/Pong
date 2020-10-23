import turtle

# build the window
window = turtle.Screen()
window.title("Pong by Joe")
window.bgcolor("white")
window.setup(width=800, height=600)
window.tracer(0)  # stop the window from updating, helps with game speed

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0) # speed of animation
paddleA.shape("square")
paddleA.color("black")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup() # draw a line
paddleA.goto(-350, 0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0) # speed of animation
paddleB.shape("square")
paddleB.color("black")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup() # draw a line
paddleB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) # speed of animation
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = .15
ball.dy = .15

# Movements
def paddleAUp():
    ycoord = paddleA.ycor()
    ycoord += 20
    paddleA.sety(ycoord)

def paddleADown():
    ycoord = paddleA.ycor()
    ycoord -= 20
    paddleA.sety(ycoord)

def paddleBUp():
    ycoord = paddleB.ycor()
    ycoord += 20
    paddleB.sety(ycoord)

def paddleBDown():
    ycoord = paddleB.ycor()
    ycoord -= 20
    paddleB.sety(ycoord)

# Controls
window.listen()
window.onkeypress(paddleAUp, "w")
window.onkeypress(paddleADown, "s")
window.onkeypress(paddleBUp, "Up")
window.onkeypress(paddleBDown, "Down")

# game loop
playinggame = True

while playinggame:
    window.update()

    # Ball Movements
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
    elif ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
    else:
        ball.setx(ball.xcor() + ball.dx)

    if ball.ycor() < -290:
        ball.dy *= -1
        ball.sety(-290)
    elif ball.ycor() > 290:
        ball.dy *= -1
        ball.sety(290)
    else:
        ball.sety(ball.ycor() + ball.dy)

    # Paddle Collision
    if (ball.xcor() < paddleA.xcor() + 10) and (ball.ycor() < paddleA.ycor() + 50) and (ball.ycor() > paddleA.ycor() - 50):
        # ball.setx(paddleA.xcor() + 10)
        # ball.sety(paddleA.ycor())
        ball.dx *= -1

    elif (ball.xcor() > paddleB.xcor() - 10) and (ball.ycor() < paddleB.ycor() + 50) and (ball.ycor() > paddleB.ycor() - 50):
        # ball.setx(paddleB.xcor() - 10)
        # ball.sety(paddleB.ycor())
        ball.dx *= -1

    # scoring
    # can we have the ball project where it's going to go with physics?
