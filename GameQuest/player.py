import turtle, math

class Player:
    outline_color = (0.1, 0.9, 0.1) # lime color in r,g,b
    fill_color = "black"
    invuln_color = (0.1, 0.5, 1.0) # turquoise
    size = 1.5
    radius = 10
    move_speed = 5
    turn_speed = 15
    MAX_LIVES = 3
    invuln_frames = 10

    # Pythagorean distance formula between two points.
    def distance(self, p1, p2):
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)

    def __init__(self):
        self._player = turtle.Turtle()
        self._player.shapesize(self.size, self.size)
        self._player.penup()
        self._player.shape("turtle")
        self._player.color(self.outline_color)
        self._player.fillcolor(self.fill_color)

        self.score = 0 # initial score of 0
        self.dest = (0,0) # where the player should be moving towards

        self.invulnerable = False
        self.lives = self.MAX_LIVES
        self.framecount = 0

    # checks if the player collides with the game borders.
    def check_border_collision(self, gamestate):
        left   = self._player.xcor() - self.radius < gamestate['min_x']
        right  = self._player.xcor() + self.radius > gamestate['max_x']
        bottom = self._player.ycor() - self.radius < gamestate['min_y']
        top    = self._player.ycor() + self.radius > gamestate['max_y']

        if left or right or bottom or top:
            return True
        else:
            return False

    # checks if the player collides with an object with given coordinates and hitbox radius
    def check_object_collision(self, coords, radius):
        if radius + self.radius > self.distance(self._player.pos(), coords):
            return True
        else:
            return False

    # called externally from Game class to tell the player where to go
    # (towards mouse click)
    def update_destination(self, dest):
        self.dest = dest

    def food_pickup_handler(self):
        self.score += 1 # if you collect food, add to your score.
                            # like with enemy collisions, we can change this.
        

    def enemy_collision_handler(self):
        if not self.invulnerable:
            self.lives -= 1
            self.invulnerable = True

    # update/movement method
    def update(self, gamestate):
        if self.invulnerable:
            self.framecount += 1
            self._player.color(self.invuln_color)
            if self.framecount == self.invuln_frames:
                self.invulnerable = False
                self.framecount = 0
        else:
            self._player.color(self.outline_color)
            

        # if you hit the border, back up
        if self.check_border_collision(gamestate):
            self._player.backward(25)

        # check for enemy collisions.
        for coord in gamestate['enemies']:
            if self.check_object_collision(coord, gamestate['enemy_radius']):
                self.enemy_collision_handler()

        # check for food collisions.
        if self.check_object_collision(gamestate['food'], gamestate['food_radius']):
            self.food_pickup_handler()

        # tell the _player where to go!
        # if you haven't reached the destination, set your direction
        # towards that point and move forwards.
        if self.distance(self._player.pos(), self.dest) > self.radius:
            self._player.setheading(self._player.towards(*self.dest))
            self._player.forward(self.move_speed)