import turtle

class Scoreboard:
    font = ("Times", 50, "bold")

    def __init__(self, gamestate):
        self.scoreboard = turtle.Turtle()
        self.scoreboard.hideturtle() # hide the turtle so we don't see it
        self.scoreboard.color("white") # set drawing color to white
        self.scoreboard.penup() # don't draw trails
        self.scoreboard.goto(
            gamestate['min_x'] + 50, # top left corner
            gamestate['max_y'] - 100
        )
        self.update(gamestate) # draw initial score
    
    def update(self, gamestate):
        self.scoreboard.clear() # clear the previous score
        self.scoreboard.write(gamestate['score'], font=self.font)
        # draw the current score (from gamestate) to the screen