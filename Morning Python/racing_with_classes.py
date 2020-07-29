import turtle, random

w, h = 1000, 200
screen = turtle.Screen()
screen.setup(width=w, height=h)

class RacingTurtle:
    time = 0.1
    
    def __init__(self, name, color, starting_y):
        self.name = name
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
        turn_angle = random.randint(-15, 15)
        speed = random.randint(0, 10)
        self.turtle.forward(speed)
        self.turtle.right(turn_angle)

        if self.check_collision():
            print("collision")
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
        
        self.time += 1

    
    '''
    Homework: think about ways to improve RacingTurtle.move() and
    make it more interesting.
    '''

    def checkWin(self):
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

positions = calculateStartingY(4)

competitors = [
    RacingTurtle("Jeff", "pink", positions[0]),
    RacingTurtle("Bob", "blue", positions[1]),
    RacingTurtle("Harold", "lime", positions[2]),
    RacingTurtle("Marilyn", "red", positions[3])
    ]

won = False
while not won:
    for t in competitors:
        if t.checkWin():
            print(t.name + " wins!")
            won = True
        t.move()

screen.mainloop()
