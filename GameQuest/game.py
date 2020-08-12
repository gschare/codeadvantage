import turtle
from player import Player   # Player()
from enemy import Enemy     # Enemy()

class Game:

    num_enemies = 50
    gamestate = {}

    def __init__(self, screen):

        self.gamestate['min_x'] = -screen.window_width()/2
        self.gamestate['max_x'] = screen.window_width()/2
        self.gamestate['min_y'] = -screen.window_height()/2
        self.gamestate['max_y'] = screen.window_height()/2

        self.me = Player()
        self.enemies = []
        for _ in range(self.num_enemies):
            self.enemies.append(Enemy(self.gamestate))

    def move_forward(self):
        self.me.player.forward(10)
        self.me.update(self.gamestate)

    def move_backward(self):
        self.me.player.backward(10)
        self.me.update(self.gamestate)

    def turn_left(self):
        self.me.player.left(15)
        self.me.update(self.gamestate)

    def turn_right(self):
        self.me.player.right(15)
        self.me.update(self.gamestate)

    def move_enemies(self):
        for enemy in self.enemies:
            enemy.update(self.gamestate)

    def update_gamestate(self):
        #self.gamestate["enemies"] = 
        pass

    def update(self):

        self.move_enemies()
        self.me.update(self.gamestate)