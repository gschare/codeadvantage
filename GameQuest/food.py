import turtle, random

class Food:
    size = 1.0
    radius = 10
    color = (0.8, 0.9, 0.3) # arbitrary initial color

    def __init__(self, gamestate):
        self._food = turtle.Turtle()
        self._food.shape("circle")
        self._food.penup()
        self._food.shapesize(self.size, self.size)
        self.reset(gamestate) # initial reset
    
    def reset(self, gamestate):
        # every time you reset, change color to random
        self.color = (
            random.uniform(0.3, 1),
            random.uniform(0.3, 1),
            random.uniform(0.3, 1)
        )
        self._food.color(self.color)

        # every time player picks up _food, reset to a random position on screen
        self._food.goto(
            random.randint(gamestate['min_x'] + 50, gamestate['max_x'] - 50),
            random.randint(gamestate['min_y'] + 50, gamestate['max_y'] - 50)
        )