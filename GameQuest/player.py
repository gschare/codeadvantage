import turtle

class Player:
    outline_color = (0.1, 0.9, 0.1) # lime color in r,g,b
    fill_color = "black"
    size = 3.0
    move_speed = 10
    turn_speed = 15

    def __init__(self):
        self.player = turtle.Turtle()
        self.player.shapesize(self.size, self.size)
        self.player.penup()
        self.player.shape("turtle")
        self.player.color(self.outline_color)
        self.player.fillcolor(self.fill_color)

    def check_border_collision(self, game_borders):
        left = self.player.xcor() < game_borders['min_x']
        right = self.player.xcor() > game_borders['max_x']
        bottom = self.player.ycor() < game_borders['min_y']
        top = self.player.ycor() > game_borders['max_y']

        if left or right or bottom or top:
            return True
        else:
            return False

    def update(self, game_borders):
        if self.check_border_collision(game_borders):
            self.player.backward(25)