import turtle   # Reference: https://docs.python.org/3/library/turtle.html
import random

# Setup
ELEMENT_COLOR = "white"
w, h = 600, 400                   # define the canvas dimensions
SCREEN = turtle.Screen()          # create the canvas
SCREEN.setup(width=w, height=h)   # this controls the canvas dimensions
SCREEN.bgcolor("black")
SCREEN.tracer(0)
framerate_ms = 10

class Posn:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Field:
    # borders
    color = "white"
    border_width = 50
    border_height = 100

    def __init__(self):
        # boundaries (coordinates relative to center)
        self.boundary_top    = SCREEN.window_height()  / 2 - self.border_height
        self.boundary_bottom = -SCREEN.window_height() / 2 + self.border_height
        self.boundary_left   = -SCREEN.window_width()  / 2 + self.border_width
        self.boundary_right  = SCREEN.window_width()   / 2 - self.border_width

        self.drawBoundaries()

    def drawBoundaries(self):
        boundary = turtle.Turtle()
        boundary.color(ELEMENT_COLOR)
        boundary.hideturtle()
        boundary.penup()
        boundary.goto(self.boundary_left,  self.boundary_top)
        boundary.pendown()
        boundary.goto(self.boundary_right, self.boundary_top)
        boundary.goto(self.boundary_right, self.boundary_bottom)
        boundary.goto(self.boundary_left,  self.boundary_bottom)
        boundary.goto(self.boundary_left,  self.boundary_top)

class Ball:
    stretch_factor = 0.5
    radius = 10 * stretch_factor
    color = "white"

    min_velocity = 2
    max_velocity = 2
    velocity_horiz = 0
    velocity_vert = 0

    def __init__(self):
        self._ball = turtle.Turtle()
        self._ball.color(ELEMENT_COLOR)
        self._ball.penup()
        self._ball.shape("circle")
        self._ball.shapesize(self.stretch_factor, self.stretch_factor)

    def getPos(self):
        return Posn(self._ball.xcor(), self._ball.ycor())

    # main movement method
    def update(self, field, paddle_left, paddle_right):
        wall_collision = self.check_wall_collision(field)
        paddle_collision = self.check_paddle_collision(paddle_left) \
            or self.check_paddle_collision(paddle_right)

        self.velocity_vert *= -1*wall_collision + 1*(not wall_collision)
        self.velocity_horiz *= -1*paddle_collision + 1*(not paddle_collision)
        self._ball.setx(self._ball.xcor() + self.velocity_horiz)
        self._ball.sety(self._ball.ycor() + self.velocity_vert)

    # collisions with top and bottom of field
    def check_wall_collision(self, field):
        top_collision = self.getPos().y + self.radius >= field.boundary_top
        bottom_collision = self.getPos().y - self.radius <= field.boundary_bottom
        return top_collision or bottom_collision

    # collisions with paddles
    def check_paddle_collision(self, paddle):
        distance_x = abs(paddle.getPos().x - self.getPos().x)
        distance_y = abs(paddle.getPos().y - self.getPos().y)
        horiz_collision = distance_x <= self.radius + (paddle.width/2)
        vert_collision  = distance_y <= self.radius + (paddle.height/2)
        return horiz_collision and vert_collision

    def reset(self, field):
        # place at center and randomize direction and speed
        self._ball.setpos(0,0)
        self.velocity_horiz  = random.randint(self.min_velocity, self.max_velocity)
        self.velocity_vert   = random.randint(self.min_velocity, self.max_velocity)
        self.velocity_horiz *= random.randint(0, 1) * 2 - 1
        self.velocity_vert  *= random.randint(0, 1) * 2 - 1

class Paddle:
    height = 40
    width = 10
    color = "white"
    boundaryoffset = 10

    velocity = 4
    direction = 0

    def __init__(self, side):
        self._paddle = turtle.Turtle()
        self._paddle.penup()
        self.side = side.upper() # 'L' or 'R'
        self.makeShape()
        self._paddle.shape("paddle")

    def getPos(self):
        return Posn(self._paddle.xcor(), self._paddle.ycor())

    def makeShape(self):
        shape = turtle.Shape("compound")
        points = (
            (-self.height/2, -self.width/2),
            (-self.height/2,  self.width/2),
            (self.height/2,   self.width/2),
            (self.height/2,  -self.width/2)
        )
        shape.addcomponent(points, ELEMENT_COLOR)
        SCREEN.register_shape("paddle", shape)

    def reset(self, field):
        if self.side=="L":
            self._paddle.setx(field.boundary_left  + self.boundaryoffset)
        elif self.side=="R":
            self._paddle.setx(field.boundary_right - self.boundaryoffset)

    # main movement method
    def update(self, field):
        new_y = self.getPos().y + (self.velocity * self.direction)
        if not self.check_wall_collision(field):
            self._paddle.sety(new_y)

    # stop paddle if hitting top or bottom
    def check_wall_collision(self, field):
        new_y = self.getPos().y + (self.velocity * self.direction)
        if (new_y - (self.height/2) < field.boundary_bottom):
            return True
        elif (new_y + (self.height/2) > field.boundary_top):
            return True
        else:
            return False

    # gets direction to move from player input
    def move(self, direction):
        self.direction = direction

class Scoreboard:
    color = "white"
    score = {
        "left"  : 0,
        "right" : 0
    }
    scoreboard_offset = 80
    scoreboard_pos = {
        "left" :  (-SCREEN.window_width()/4, SCREEN.window_height()/2 - scoreboard_offset),
        "right" : ( SCREEN.window_width()/4, SCREEN.window_height()/2 - scoreboard_offset)
    }
    scoreboard_font = ("Arial", 32, "bold")

    def __init__(self):
        self._score = turtle.Turtle()
        self._score.color(ELEMENT_COLOR)
        self._score.penup()
        self._score.hideturtle()
        self.update()  # write initial scores

    def update(self):
        self._score.clear()
        self._score.goto(*self.scoreboard_pos["left"])
        self._score.write(self.score["left"],  align="center", font=self.scoreboard_font)
        self._score.goto(*self.scoreboard_pos["right"])
        self._score.write(self.score["right"], align="center", font=self.scoreboard_font)

    def incrementScore(self, side):
        self.score[side] += 1

class Game:

    def __init__(self):
        self.field = Field()
        self.scoreboard = Scoreboard()
        self.ball = Ball()
        self.paddle_left  = Paddle("L")
        self.paddle_right = Paddle("R")

        self.ball.reset(self.field)
        self.paddle_left.reset(self.field)
        self.paddle_right.reset(self.field)

    # check if a player wins (ball hits edge)
    # this combined with check_paddle_collision is probably what's
    # responsible for the bugs we see with the ball getting "stuck"
    # on a paddle
    def check_score(self):
        if (self.ball.getPos().x + self.ball.radius >= self.field.boundary_right):
            self.scoreboard.incrementScore("left")
            self.ball.reset(self.field)
            self.scoreboard.update()
        elif (self.ball.getPos().x - self.ball.radius <= self.field.boundary_left):
            self.scoreboard.incrementScore("right")
            self.ball.reset(self.field)
            self.scoreboard.update()

    # direct paddle movement from player input
    def movePaddle(self, side, direction):
        if side=="L":
            self.paddle_left.move(direction)
        elif side=="R":
            self.paddle_right.move(direction)

    # main loop
    def frame(self):
        self.check_score()
        self.paddle_left.update(self.field)
        self.paddle_right.update(self.field)
        self.ball.update(self.field, self.paddle_left, self.paddle_right)

        SCREEN.update()
        SCREEN.ontimer(self.frame, framerate_ms) # repeat every ? milliseconds

game = Game()

# movement functions
leftup    = lambda: game.movePaddle("L", 1)
leftdown  = lambda: game.movePaddle("L", -1)
leftstop  = lambda: game.movePaddle("L", 0)
rightup   = lambda: game.movePaddle("R", 1)
rightdown = lambda: game.movePaddle("R", -1)
rightstop = lambda: game.movePaddle("R", 0)

game.frame()

# player input
SCREEN.onkeypress(leftup, key="w")
SCREEN.onkeypress(leftdown,  key="s")
SCREEN.onkeyrelease(leftstop, "w")
SCREEN.onkeyrelease(leftstop, "s")

SCREEN.onkeypress(rightup, key="Up")
SCREEN.onkeypress(rightdown, key="Down")
SCREEN.onkeyrelease(rightstop, "Up")
SCREEN.onkeyrelease(rightstop, "Down")

SCREEN.listen()

SCREEN.mainloop()
