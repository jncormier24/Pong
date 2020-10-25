# @TODO:
# can we have the ball project where it's going to go with physics?
# networking?

import turtle
from paddle import Paddle
from ball import Ball

# build the window
window = turtle.Screen()
window.title("Pong by Joe")
window.bgcolor("white")
window.setup(width=800, height=600)
window.tracer(0)  # stop the window from updating, helps with game speed

# Paddle A
paddleA = Paddle()
paddleA.build(xpos=-350, ypos=0, name='Player A')

# Paddle B
paddleB = Paddle()
paddleB.build(350, 0, 'Player B')

# Ball
ball = Ball()
ball.build(.15, .15)

# Scoring
playerAScore = 0
playerBScore = 0
score = turtle.Turtle()
score.speed(0)
score.color('black')
score.penup()
score.hideturtle()
score.goto(0, 260)


def writeScore(playerA, playerB):
    score.clear()
    score.write("Player A: {}  Player B: {}".format(playerAScore, playerBScore), align="center", font=("", 24, "normal"))

# Movements
def paddleAUp():
    paddleA.moveUp(20)

def paddleADown():
    paddleA.moveDown(20)

def paddleBUp():
    paddleB.moveUp(20)

def paddleBDown():
    paddleB.moveDown(20)

# Controls
window.listen()
window.onkeypress(paddleAUp, "w")
window.onkeypress(paddleADown, "s")
window.onkeypress(paddleBUp, "Up")
window.onkeypress(paddleBDown, "Down")

# game loop
writeScore(playerAScore, playerBScore)
playinggame = True

while playinggame:
    window.update()

    # Ball Movements
    # Player B Scored
    if ball.xcor() < -390:
        playerBScore += 1
        ball.goto(0, 0)
        ball.dx *= -1
        writeScore(playerAScore, playerBScore)

    # Player A Scored 
    elif ball.xcor() > 390:
        playerAScore += 1
        ball.goto(0, 0)
        ball.dx *= -1
        writeScore(playerAScore, playerBScore)

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
