import turtle, math

class Player:
    outline_color = (0.1, 0.9, 0.1) # lime color in r,g,b
    fill_color = "black"
    size = 3.0
    radius = 20
    move_speed = 10
    turn_speed = 15

    def __init__(self):
        self.player = turtle.Turtle()
        self.player.shapesize(self.size, self.size)
        self.player.penup()
        self.player.shape("turtle")
        self.player.color(self.outline_color)
        self.player.fillcolor(self.fill_color)

    def check_border_collision(self, gamestate):
        left   = self.player.xcor() - self.radius < gamestate['min_x']
        right  = self.player.xcor() + self.radius > gamestate['max_x']
        bottom = self.player.ycor() - self.radius < gamestate['min_y']
        top    = self.player.ycor() + self.radius > gamestate['max_y']

        if left or right or bottom or top:
            return True
        else:
            return False

    def check_object_collision(self, coords, radius):
        x1 = self.player.xcor()
        y1 = self.player.ycor()
        x2 = coords[0] # (x, y)
        y2 = coords[1]
        distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)

        if radius + self.radius > distance:
            return True
        else:
            return False

    def update(self, gamestate):
        if self.check_border_collision(gamestate):
            self.player.backward(25)
        for coord in gamestate['enemies']:
            if self.check_object_collision(coord, gamestate['enemy_radius']):
                self.player.goto(0,0)