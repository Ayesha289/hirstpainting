import turtle as t
import random

t.colormode(255)
timmy = t.Turtle()

color_fill = ((255, 204, 255), (153, 255, 204), (102, 153, 255), (153, 0, 153), (255, 255, 153), (51, 102, 153), (255, 102, 0), (153, 204, 0), (255, 0, 0), (51, 153, 255))

timmy.speed("fastest")
timmy.penup()
timmy.goto(-250, -250)
timmy.pendown()

def timmy_paint():
    for _ in range(10):
        color = random.choice(color_fill)
        timmy.dot(20, color)
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()

def timmy_direction():
    timmy.penup()
    timmy.speed("fastest")
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(500)
    timmy.right(180)
    timmy.pendown()

for _ in range(10):
    timmy_paint()
    timmy_direction()

screen = t.Screen()
screen.exitonclick()