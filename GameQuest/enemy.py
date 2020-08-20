import turtle, random
from helpers import distance, check_border_collision, check_object_collision

class Enemy:
    outline_color = (1.0, 0.0, 0.0) # red
    # maybe disguise as food? same shape, random colors?
    size = 1.0
    radius = 10
    min_move_speed = 0
    max_move_speed = 2
    min_turn_speed = -15
    max_turn_speed = 15
    dead = False

    def __init__(self, gamestate):
        self._enemy = turtle.Turtle()
        self._enemy.shape("circle")
        self._enemy.shapesize(self.size, self.size)
        self._enemy.penup()
        self.color = (
            random.uniform(0.3, 1),
            random.uniform(0.3, 1),
            random.uniform(0.3, 1)
        )
        self._enemy.color(self.color)
        self._enemy.goto(
            random.randint(gamestate['min_x'], gamestate['max_x']), # x
            random.randint(gamestate['min_y'], gamestate['max_y'])  # y
        )

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

        # check bullet collision
        for coord in gamestate["bullets"]:
            if check_object_collision(
                self._enemy.pos(), coord,
                self.radius, gamestate['bullet_radius']):
                self.dead = True

        if not self.dead:
            
            # turn randomly left or right
            self._enemy.left(random.randint(
                self.min_turn_speed, self.max_turn_speed))

            # move a random amount forward
            if not check_border_collision(self._enemy.pos(), self.radius, gamestate):
                self._enemy.forward(random.randint(
                    self.min_move_speed, self.max_move_speed))

            # if you collide with the border, turn around and move away
            else: 
                self._enemy.right(180)
                self._enemy.forward(self.max_move_speed)

        else:
            self._enemy.hideturtle()