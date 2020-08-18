import turtle

class Scoreboard:
    scorefont = ("Arial", 100, "bold")
    scorecolor = "white"
    livesfont = ("Arial", 50, "bold")
    livescolor = "red"

    def __init__(self, gamestate):
        self._scoreboard = turtle.Turtle()
        self._scoreboard.hideturtle() # hide the turtle so we don't see it
        self._scoreboard.penup() # don't draw trails
        self.scorepos = (
            gamestate['min_x'] + 50, # top left corner
            gamestate['max_y'] - 150
        )
        self.update(gamestate) # draw initial score
    
    def update(self, gamestate):
        self._scoreboard.color(self.scorecolor) # set drawing color to white
        self._scoreboard.goto(*self.scorepos)
        self._scoreboard.clear() # clear the previous score

        self._scoreboard.write(gamestate['score'], font=self.scorefont)
        
        self._scoreboard.sety(self._scoreboard.ycor() + 20)

        for _ in range(gamestate['lives']):
            self._scoreboard.color(self.livescolor)
            self._scoreboard.setx(self._scoreboard.xcor() + self.livesfont[1] + 20) 
            self._scoreboard.write("<3", font=self.livesfont)

        # draw the current score (from gamestate) to the screen