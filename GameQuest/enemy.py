import turtle, random

class Enemy:
    outline_color = (1.0, 0.0, 0.0) # red
    size = 1.0
    min_move_speed = 0
    max_move_speed = 10
    min_turn_speed = -15
    max_turn_speed = 15

    def __init__(self, game_borders):
        self.enemy = turtle.Turtle()
        self.enemy.shapesize(self.size, self.size)
        self.enemy.penup()
        self.enemy.color(self.outline_color)
        self.enemy.goto(
            random.randint(game_borders['min_x'], game_borders['max_x']), # x
            random.randint(game_borders['min_y'], game_borders['max_y'])  # y
        )

    def check_border_collision(self, game_borders):
        left = self.enemy.xcor() < game_borders['min_x']
        right = self.enemy.xcor() > game_borders['max_x']
        bottom = self.enemy.ycor() < game_borders['min_y']
        top = self.enemy.ycor() > game_borders['max_y']

        if left or right or bottom or top:
            return True
        else:
            return False

    def update(self, game_borders):
        self.enemy.left(random.randint(
            self.min_turn_speed, self.max_turn_speed))

        if not self.check_border_collision(game_borders):
            self.enemy.forward(random.randint(
                self.min_move_speed, self.max_move_speed))
        else:
            self.enemy.right(180)
            self.enemy.forward(self.max_move_speed)