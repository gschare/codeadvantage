import turtle, random

class Enemy:
    outline_color = (1.0, 0.0, 0.0) # red
    # maybe disguise as food? same shape, random colors?
    size = 1.0
    radius = 5
    min_move_speed = 0
    max_move_speed = 2
    min_turn_speed = -15
    max_turn_speed = 15

    def __init__(self, gamestate):
        self._enemy = turtle.Turtle()
        self._enemy.shapesize(self.size, self.size)
        self._enemy.penup()
        self._enemy.color(self.outline_color)
        self._enemy.goto(
            random.randint(gamestate['min_x'], gamestate['max_x']), # x
            random.randint(gamestate['min_y'], gamestate['max_y'])  # y
        )

    # same as player border collision
    def check_border_collision(self, gamestate):
        left   = self._enemy.xcor() - self.radius < gamestate['min_x']
        right  = self._enemy.xcor() + self.radius> gamestate['max_x']
        bottom = self._enemy.ycor() - self.radius < gamestate['min_y']
        top    = self._enemy.ycor() + self.radius > gamestate['max_y']

        if left or right or bottom or top:
            return True
        else:
            return False

    # in some sense, we might want to add an object collision function here
    # to check whether a given enemy has collided with the player.
    # Advantages of doing it this way include:
    #  - we can have direct effects on the enemy when they collide with the player
    #       (e.g. if player has shields on then enemy should die)

    # We probably only want one of them to check, though. So either player checks
    # for collision with enemy, or enemy checks with collision with player.
    # If we do both, we are wasting computer power. 

    # If the player is the one checking, it will be more difficult to tell
    # WHICH enemy you collided with. Whereas if the enemy is checking, there's
    # only one person it can be: the player. So we just need to report the
    # collision to the gamestate and then the effects will be dictated to the
    # player indirectly but just as effectively.

    # If we really care about processing speed, this will also make it much easier
    # to optimize since having each enemy check if they're anywhere near the player
    # is much easier than have the player check if they're near any enemy.

    # movement/update function
    def update(self, gamestate):

        # turn randomly left or right
        self._enemy.left(random.randint(
            self.min_turn_speed, self.max_turn_speed))

        # move a random amount forward
        if not self.check_border_collision(gamestate):
            self._enemy.forward(random.randint(
                self.min_move_speed, self.max_move_speed))

        # if you collide with the border, turn around and move away
        else: 
            self._enemy.right(180)
            self._enemy.forward(self.max_move_speed)