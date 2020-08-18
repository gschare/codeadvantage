import turtle
from player import Player   # Player()
from enemy import Enemy     # Enemy()
from food import Food       # Food()
from scoreboard import Scoreboard

class Game:

    num_enemies = 20 # we could attach this to a difficulty scale
    gamestate = {} # dictionary containing information about the game
                   # we pass this info to other objects so they can know
                   # what's going on in the game without directly accessing
                   # each other's info.

    def __init__(self, screen):

        # define the game borders
        self.gamestate['min_x'] = -screen.window_width()/2
        self.gamestate['max_x'] = screen.window_width()/2
        self.gamestate['min_y'] = -screen.window_height()/2
        self.gamestate['max_y'] = screen.window_height()/2

        self.gamestate['enemies'] = [] # list of enemy positions
        self.gamestate['enemy_radius'] = Enemy.radius # the collision box
        self.gamestate['food_radius'] = Food.radius   # the collision box

        self.me = Player() # initialize the player
        self.gamestate['score'] = self.me.score # get player's initial score (0)
        self.gamestate['lives'] = self.me.lives

        self.food = Food(self.gamestate) # initialize the food
        self.gamestate['food'] = self.food._food.pos() # get the food position

        self.enemies = [] # initialize list of enemies
        for _ in range(self.num_enemies):
            self.enemies.append(Enemy(self.gamestate)) # create enemies one by one
            # add each enemy's initial position to gamestate
            self.gamestate['enemies'].append(self.enemies[-1]._enemy.pos())

        # create the scoreboard
        self.scoreboard = Scoreboard(self.gamestate)

    # player movement functions (not really used)
    def move_forward(self):
        self.me._player.forward(10)

    def move_backward(self):
        self.me._player.backward(10)

    def turn_left(self):
        self.me._player.left(15)

    def turn_right(self):
        self.me._player.right(15)

    # iterate over list of enemies and call their update methods
    def move_enemies(self):
        for enemy in self.enemies:
            enemy.update(self.gamestate)

    # gather information from game objects every frame and update info
    def update_gamestate(self):
        positions = []
        for e in self.enemies:
            positions.append(e._enemy.pos())
        self.gamestate["enemies"] = positions # gather enemy positions

        self.gamestate["food"] = self.food._food.pos() # get food position
        self.gamestate["score"] = self.me.score # get current score
        self.gamestate['lives'] = self.me.lives

    def gameOver(self):
        for e in self.enemies:
            e._enemy.hideturtle()
        self.me._player.hideturtle()
        self.food._food.hideturtle()
        self.gameover = turtle.Turtle()
        self.gameover.color("white")
        self.gameover.penup()
        self.gameover.hideturtle()
        self.gameover.setx(self.gameover.xcor()-200)
        self.gameover.write("GAME OVER", font=("Arial", 50, "bold"))

    def update(self):

        update_score = False

        self.move_enemies()
        self.me.update(self.gamestate)

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
            update_score = True

        if self.me.lives != self.gamestate["lives"]:
            update_score = True
        
        self.update_gamestate()
        
        if update_score:
            self.scoreboard.update(self.gamestate)

        if self.gamestate["lives"] == 0:
            self.gameOver()