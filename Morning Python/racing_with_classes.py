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

    def move(self):
        speed = random.randint(0, 10)
        self.turtle.setx(self.turtle.xcor() + speed)
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

Jeff = RacingTurtle("Jeff", "pink", 20)
Bob = RacingTurtle("Bob", "blue", -20)

while True:
  if Bob.checkWin():
    print("Bob wins!")
    break
  if Jeff.checkWin():
    print("Jeff wins!")
    break
  Jeff.move()
  Bob.move()

screen.mainloop()
