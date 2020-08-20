import turtle
from player import Player   # Player()
from enemy import Enemy     # Enemy()
from food import Food       # Food()
from scoreboard import Scoreboard
from bullet import Bullet

class Game:

    num_enemies = 20 # we could attach this to a difficulty scale
    gamestate = {} # dictionary containing information about the game
                   # we pass this info to other objects so they can know
                   # what's going on in the game without directly accessing
                   # each other's info.

    def __init__(self, screen):

        self.gamestate["gameover"] = False

        # define the game borders
        self.gamestate['min_x'] = -screen.window_width()/2
        self.gamestate['max_x'] = screen.window_width()/2
        self.gamestate['min_y'] = -screen.window_height()/2
        self.gamestate['max_y'] = screen.window_height()/2

        self.gamestate['enemies'] = [] # list of enemy positions
        self.gamestate['enemy_radius'] = Enemy.radius # the collision box
        self.gamestate['food_radius'] = Food.radius   # the collision box
        self.gamestate['bullet_radius'] = Bullet.radius

        self.me = Player() # initialize the player
        self.gamestate['score'] = self.me.score # get player's initial score (0)
        self.gamestate['lives'] = self.me.lives

        self.bullets = []
        self.gamestate['bullets'] = []

        self.food = Food(self.gamestate) # initialize the food
        self.gamestate['food'] = self.food._food.pos() # get the food position

        self.enemies = [] # initialize list of enemies
        for _ in range(self.num_enemies):
            self.enemies.append(Enemy(self.gamestate)) # create enemies one by one
            # add each enemy's initial position to gamestate
            self.gamestate['enemies'].append(self.enemies[-1]._enemy.pos())

        # create the scoreboard
        self.scoreboard = Scoreboard(self.gamestate)

    # player controls
    def move(self, x, y):
        self.me.update_destination((x,y))

    def shoot(self, x, y):
        self.me.shoot(x, y)
        if self.me.score > 0 and not self.gamestate["gameover"]:
            self.create_bullet(*self.me._player.pos(), self.me._player.heading())
            self.me.score -= 1

    # iterate over list of enemies and call their update methods
    def move_enemies(self):
        for enemy in self.enemies:
            enemy.update(self.gamestate)

    # gather information from game objects every frame and update info
    def update_gamestate(self):
        new_enemies = []
        positions = []
        for e in self.enemies:
            if not e.dead:
                new_enemies.append(e)
                positions.append(e._enemy.pos())
        if len(self.enemies) != len(new_enemies):
            self.update_score = True
        self.enemies = new_enemies
        self.gamestate["enemies"] = positions # gather enemy positions
        
        self.gamestate["food"] = self.food._food.pos() # get food position
        self.gamestate["score"] = self.me.score # get current score
        self.gamestate['lives'] = self.me.lives

        new_bullets = []
        positions = []
        for bullet in self.bullets:
            if not bullet.dead:
                new_bullets.append(bullet)
                positions.append(bullet._bullet.pos())
        self.bullets = new_bullets
        self.gamestate["bullets"] = positions

        # alternate ways of doing this:
        # self.bullets = [b for b in self.bullets if not b.dead]
        # self.gamestate["bullets"] = [b._bullet.pos() for b in self.bullets]

        # self.bullets = filter(lambda x: not x.dead, self.bullets)
        # self.gamestate["bullets"] = [b._bullet.pos() for b in self.bullets]

    def create_bullet(self, x, y, angle):
        self.bullets.append(Bullet(x, y, angle))
        self.gamestate["bullets"].append((x,y))

    def gameOver(self):
        self.gamestate["gameover"] = True
        for e in self.enemies:
            e.dead = True
        self.me._player.hideturtle()
        self.food._food.hideturtle()
        self.gameover = turtle.Turtle()
        self.gameover.color("white")
        self.gameover.penup()
        self.gameover.hideturtle()
        self.gameover.setx(self.gameover.xcor()-200)
        self.gameover.write("GAME OVER", font=("Arial", 50, "bold"))

    def update(self):

        self.update_score = False

        self.move_enemies()
        self.me.update(self.gamestate)

        for bullet in self.bullets:
            bullet.update(self.gamestate)

        # if the player's score has increased since the last frame,
        # then reset the food position.
        # debug note: the reason this wasn't working before is because we hadn't updated the player score yet!
        # self.me.score updates after self.me.update() runs. That's why I moved that line to above.
        # Now, the order is as follows:
        # 1. move all the enemies
        # 2. move the player (and check for collisions with enemies and food, possibly increasing the score)
        # 3. move the food if the player picked it up
        # 4. update the gamestate (including new score)
        # 5. update the scoreboard using the updated gamestate
        if self.me.score != self.gamestate["score"]:
            self.food.reset(self.gamestate)
            self.update_score = True

        if self.me.lives != self.gamestate["lives"]:
            self.update_score = True
        
        self.update_gamestate()
        
        if self.update_score and not self.gamestate["gameover"]:
            self.scoreboard.update(self.gamestate)

        if self.gamestate["lives"] == 0:
            self.gameOver()