from turtle import Turtle, Screen

SIDES = 4
OUTER_ITERS = 36
INNER_ITERS = 300
SPEED = 12
INNER_COLOR = "red"
OUTER_COLOR = "green"

def draw_square(some_turtle):

    for _ in range(SIDES):
        some_turtle.forward(200)
        some_turtle.right(360 / SIDES)

def draw_art():

    # Turtle Brad
    brad = Turtle(shape="turtle")
    brad.color(OUTER_COLOR)
    brad.pensize(2)
    brad.speed(SPEED)  # 6/normal is the default so don't need to do it

    for _ in range(OUTER_ITERS):
        draw_square(brad)
        brad.right(10)

    # Turtle Angie
    angie = Turtle(shape="turtle")
    angie.color(INNER_COLOR)
    angie.pensize(2)
    angie.speed(SPEED)  # slightly slower than brad

    size = 1

    for _ in range(INNER_ITERS):
        angie.forward(size)
        angie.right(91)
        size += 1

window = Screen()
window.bgcolor("black")

draw_art()

window.exitonclick()
