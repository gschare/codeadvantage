import turtle
from player import Player   # Player()
from enemy import Enemy     # Enemy()

class Game:

    num_enemies = 20
    gamestate = {}

    def __init__(self, screen):

        self.gamestate['min_x'] = -screen.window_width()/2
        self.gamestate['max_x'] = screen.window_width()/2
        self.gamestate['min_y'] = -screen.window_height()/2
        self.gamestate['max_y'] = screen.window_height()/2
        self.gamestate['enemies'] = []
        self.gamestate['enemy_radius'] = Enemy.radius

        self.me = Player()
        self.enemies = []
        for _ in range(self.num_enemies):
            self.enemies.append(Enemy(self.gamestate))
            self.gamestate['enemies'].append(self.enemies[-1].enemy.pos())

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
        positions = []
        for e in self.enemies:
            positions.append(e.enemy.pos())
        self.gamestate["enemies"] = positions

    def update(self):
        self.update_gamestate()
        self.move_enemies()
        self.me.update(self.gamestate)