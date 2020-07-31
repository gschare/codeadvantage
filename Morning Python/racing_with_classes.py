import turtle, random

w, h = 1000, 400
screen = turtle.Screen()
screen.setup(width=w, height=h)
screen.tracer(0)
framerate = 20

class Field:
    offset = 20
    top    =   screen.window_height()/2 - offset
    bottom = -(screen.window_height()/2 - offset)
    left   = -(screen.window_width()/2  - offset)
    right  =   screen.window_width()/2  - offset
    
    def __init__(self):
        self.borders = turtle.Turtle()
        self.drawBorders()

    def drawBorders(self):
        self.borders.hideturtle()
        self.borders.penup()
        self.borders.goto(self.left, self.top)
        self.borders.pendown()
        self.borders.goto(self.right, self.top)
        self.borders.goto(self.right, self.bottom)
        self.borders.goto(self.left, self.bottom)
        self.borders.goto(self.left, self.top)

class RacingTurtle:
    time = 0.1
    isPlayer = False
    turn_limit = 15
    min_speed = 0
    max_speed = 10
    size = 10
    starting_x_offset = 20
    
    def __init__(self, name, color, starting_y, field):
        self.field = field
        self.name = name
        self.color = color
        self.turtle = turtle.Turtle(shape="turtle")
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(self.field.left + self.starting_x_offset, starting_y)
        self.prevx = self.turtle.xcor()
        self.prevy = self.turtle.ycor()

    def check_collision(self):
        if self.turtle.xcor() - self.size <= self.field.left:
            return True
        elif self.turtle.ycor() - self.size <= self.field.bottom:
            return True
        elif self.turtle.ycor() + self.size >= self.field.top:
            return True
        else:
            return False

    def move(self):

        # if the turtle is a player, don't turn randomly
        turn_angle = random.randint(-self.turn_limit, self.turn_limit) * (not self.isPlayer)
        speed = random.randint(self.min_speed, self.max_speed)
        self.turtle.forward(speed)
        self.turtle.right(turn_angle)

        if self.check_collision():
            print(f'Collision: {self.name} ({self.color})')
            dx = self.turtle.xcor() - self.prevx
            dy = self.turtle.ycor() - self.prevy
            if dx * dy >= 0:
                direction = 1
            else:
                direction = -1
            self.turtle.right(180)  # direction is -1 or 1
            self.turtle.forward(20)

        self.prevx = self.turtle.xcor()
        self.prevy = self.turtle.ycor()
        
        self.time += 1 # currently unused

    def checkWin(self):
        # if the turtle has passed the finish line
        # it may be prudent to make the finish line a separate variable
        if self.turtle.xcor() + self.size >= self.field.right:
            return True
        else:
            return False

def calculateStartingY(num_turtles, field):
    first_pos = (field.top - field.bottom) / (num_turtles+1)
    positions = []
    for i in range(num_turtles):
        positions.append(first_pos * (i+1) - ((field.top - field.bottom)/2))
    return positions    

field = Field()

positions = calculateStartingY(5, field)

competitors = [
    RacingTurtle("Jeff", "pink", positions[0], field),
    RacingTurtle("Bob", "blue", positions[1], field),
    RacingTurtle("Harold", "lime", positions[3], field),
    RacingTurtle("Marilyn", "red", positions[4], field)
    ]

player = RacingTurtle("Gregory", "green", positions[2], field)
player.isPlayer = True

def goLeft():
    player.turtle.left(10)

def goRight():
    player.turtle.right(10)

screen.onkey(goLeft, key="Left")
screen.onkey(goRight, key="Right")
screen.listen()

# soon we will convert this while loop to a framerate loop to keep it consistent
def frame():
    for t in competitors:
        if t.checkWin():
            print(t.name + " wins!")
            return
        t.move()
        
    if player.checkWin():
        print(player.name + " wins!")
        return
    
    player.move()  # we reuse the NPC move method, except we don't turn randomly

    screen.update()
    screen.ontimer(frame, framerate)

frame()

screen.mainloop()
