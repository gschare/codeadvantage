import turtle, math

class Player:
    outline_color = (0.1, 0.9, 0.1) # lime color in r,g,b
    fill_color = "black"
    size = 1.5
    radius = 10
    move_speed = 5
    turn_speed = 15
    score = 0 # initial score of 0
    dest = (0,0) # where the player should be moving towards

    # Pythagorean distance formula between two points.
    def distance(self, p1, p2):
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)

    def __init__(self):
        self.player = turtle.Turtle()
        self.player.shapesize(self.size, self.size)
        self.player.penup()
        self.player.shape("turtle")
        self.player.color(self.outline_color)
        self.player.fillcolor(self.fill_color)

    # checks if the player collides with the game borders.
    def check_border_collision(self, gamestate):
        left   = self.player.xcor() - self.radius < gamestate['min_x']
        right  = self.player.xcor() + self.radius > gamestate['max_x']
        bottom = self.player.ycor() - self.radius < gamestate['min_y']
        top    = self.player.ycor() + self.radius > gamestate['max_y']

        if left or right or bottom or top:
            return True
        else:
            return False

    # checks if the player collides with an object with given coordinates and hitbox radius
    def check_object_collision(self, coords, radius):
        if radius + self.radius > self.distance(self.player.pos(), coords):
            return True
        else:
            return False

    # called externally from Game class to tell the player where to go
    # (towards mouse click)
    def update_destination(self, dest):
        self.dest = dest

    # update/movement method
    def update(self, gamestate):
        # if you hit the border, back up
        if self.check_border_collision(gamestate):
            self.player.backward(25)

        # check for enemy collisions.
        for coord in gamestate['enemies']:
            if self.check_object_collision(coord, gamestate['enemy_radius']):
                self.player.goto(0,0) # what to do if you collide with enemy.
                                      # we will put this in a separate method
                                      # on Monday and change what it does.

        # check for food collisions.
        if self.check_object_collision(gamestate['food'], gamestate['food_radius']):
            self.score += 1 # if you collect food, add to your score.
                            # like with enemy collisions, we can change this.

        # tell the player where to go!
        # if you haven't reached the destination, set your direction
        # towards that point and move forwards.
        if self.distance(self.player.pos(), self.dest) > self.radius:
            self.player.setheading(self.player.towards(*self.dest))
            self.player.forward(self.move_speed)