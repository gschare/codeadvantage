import turtle
from helpers import check_border_collision

class Bullet:
    size = 1.0
    radius = 10
    color = "white"
    move_speed = 40
    dead = False

    def __init__(self, x, y, angle):
        self._bullet = turtle.Turtle()
        self._bullet.shapesize(self.size, self.size)
        self._bullet.color(self.color)
        self._bullet.penup()
        self._bullet.goto(x, y)
        self._bullet.setheading(angle)
        self._bullet.pendown()

    def update(self, gamestate):
        if not check_border_collision(self._bullet.pos(), self.radius, gamestate):
            self._bullet.forward(self.move_speed)
        else:
            self.dead = True
            self._bullet.hideturtle()
            self._bullet.penup()
            self._bullet.clear()
