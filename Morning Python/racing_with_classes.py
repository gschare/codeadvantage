import turtle, random

w, h = 1000, 200
screen = turtle.Screen()
screen.setup(width=w, height=h)

class RacingTurtle:
    time = 0.1
    isPlayer = False
    
    def __init__(self, name, color, starting_y):
        self.name = name
        self.color = color
        self.turtle = turtle.Turtle(shape="turtle")
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(-screen.window_width()/2 + 10, starting_y)
        self.prevx = self.turtle.xcor()
        self.prevy = self.turtle.ycor()

    def check_collision(self):
        if self.turtle.xcor() <= -screen.window_width()/2 + 10:
            return True
        elif self.turtle.ycor() <= -screen.window_height()/2 + 10:
            return True
        elif self.turtle.ycor() >= screen.window_height()/2 - 10:
            return True
        else:
            return False

    def move(self):

        # if the turtle is a player, don't turn randomly
        turn_angle = random.randint(-15, 15) * (not self.isPlayer)
        speed = random.randint(0, 10)
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
            self.turtle.right(60*direction)  # direction is -1 or 1
            self.turtle.forward(10)

        self.prevx = self.turtle.xcor()
        self.prevy = self.turtle.ycor()
        
        self.time += 1 # currently unused

    def checkWin(self):
        # if the turtle has passed the finish line
        # it may be prudent to make the finish line a separate variable
        if self.turtle.xcor() >= screen.window_width()/2 - 10:
            return True
        else:
            return False

def calculateStartingY(num_turtles):
    first_pos = screen.window_height() / (num_turtles+1)
    positions = []
    for i in range(num_turtles):
        positions.append(first_pos * (i+1) - (screen.window_height()/2))
    return positions    

positions = calculateStartingY(5)

competitors = [
    RacingTurtle("Jeff", "pink", positions[0]),
    RacingTurtle("Bob", "blue", positions[1]),
    RacingTurtle("Harold", "lime", positions[3]),
    RacingTurtle("Marilyn", "red", positions[4])
    ]

player = RacingTurtle("Gregory", "green", positions[2])
player.isPlayer = True

def goLeft():
    player.turtle.left(10)

def goRight():
    player.turtle.right(10)

# soon we will convert this while loop to a framerate loop to keep it consistent
won = False
while not won:
    for t in competitors:
        if t.checkWin():
            print(t.name + " wins!")
            won = True
        t.move()
        
    if player.checkWin():
        print(player.name + " wins!")
        won = True
    screen.onkey(goLeft, key="Left")
    screen.onkey(goRight, key="Right")
    screen.listen()
    player.move()  # we reuse the NPC move method, except we don't turn randomly

screen.mainloop()
