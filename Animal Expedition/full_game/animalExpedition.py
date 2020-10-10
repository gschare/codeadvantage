# GAME FILE
import os, sys, math, random, turtle

def rnum(n0,n1): return random.randint(n0,n1)
def distForm(a,b): return math.sqrt((a.xcor()-b.xcor())**2 + (a.ycor()-b.ycor())**2)

tpool = {}

gridX = 1
gridY = 1
current_biome = 'plains'

gameDesign = {
    '1,1':'plains',
    '1,2':'river',
    '1,3':'ocean',
    '2,1':'forest',
    '2,2':'rain_forest',
    '2,3':'glacier',
    '3,1':'mountain',
    '3,2':'valleys',
    '3,3':'desert'
}

biomes = {
    'ocean':['goldfish','shark'],
    'plains':['lion','hyenna'],
    'rain_forest':['sloth','fire_ant'],
    'river':['bass','salmon'],
    'glacier':['penguin','polar_bear'],
    'mountain':['goat','wolf'],
    'valleys':['lizard','komodo_dragon'],
    'desert':['vulture','rattle_snake'],
    'forest':['jackrabbit','jaguar']
}

current_animals = biomes['plains']
move_animals = False
animal_house = []

s = turtle.Screen()
s.bgcolor('black')
s.title('Animal Expedition')
s.screensize(1000,500); s.setup(1050,550)

for biome, animals in biomes.items():

    for a in animals:
        tpool[a] = turtle.Turtle()
        tpool[a].hideturtle()
        tpool[a].penup()
        tpool[a].shapesize(rnum(1,5),rnum(1,5))
        tpool[a].setpos(rnum(-300,300),rnum(-200,200))


        # Tie animal shapes into the game
        s.register_shape(f"{a}.gif")
        tpool[a].shape(f"{a}.gif")



# MAKE GAME BORDERS
gameBorders = {'min_x':-550,'max_x':550,'min_y':-225,'max_y':225}

# MAKE PLAYER
player = turtle.Turtle()
player.penup()
player.shape('turtle')
player.color('red')
player.shapesize(2,2)

# Add player shape
s.register_shape('player.gif')
player.shape('player.gif')



def checkBorders(x,xs,borders=gameBorders):

    global gridX
    global gridY

    # HANDLE Y Direction -----------------------------------------
    if x.ycor() >= borders['max_y']:

        if gridY < 3:
            x.hideturtle(); x.sety(borders['min_y']+20)
            gridY += 1
            set_biome(); x.showturtle()

        else:
            x.sety(borders['max_y']-20)

    elif x.ycor() <= borders['min_y']:

        if gridY > 1:
            x.hideturtle(); x.sety(borders['max_y']-20)
            gridY -= 1
            set_biome(); x.showturtle()

        else:
            x.sety(borders['min_y']+20)

    # HANDLE X DIRECTION -----------------------------------------
    elif x.xcor() >= borders['max_x']:

        if gridX < 3:
            x.hideturtle(); x.setx(borders['min_x']+20)
            gridX += 1
            set_biome(); x.showturtle()

        else:
            x.setx(borders['max_x']-20)

    elif x.xcor() <= borders['min_x']:

        if gridX > 1:
            x.hideturtle(); x.setx(borders['max_x']-20)
            gridX -= 1
            set_biome(); x.showturtle()

        else:
            x.setx(borders['min_x']+20)


def m_up():     player.sety(player.ycor()+10); checkBorders(player,s)
def m_left():   player.setx(player.xcor()-10); checkBorders(player,s)
def m_right():  player.setx(player.xcor()+10); checkBorders(player,s)
def m_down():   player.sety(player.ycor()-10); checkBorders(player,s)

s.onkeypress(m_up,'Up')
s.onkeypress(m_left,'Left')
s.onkeypress(m_right,'Right')
s.onkeypress(m_down,'Down')

def set_biome():

    global current_biome
    global current_animals
    global animal_house
    global move_animals

    global gridX
    global gridY

    move_animals = False
    for a in animal_house: a.hideturtle()

    tempX = gridX
    tempY = gridY

    if tempX < 1: tempX = 1
    if tempX > 3: tempX = 3
    
    if tempY < 1: tempY = 1
    if tempY > 3: tempY = 3

    gridX, gridY = tempX, tempY

    current_biome =     gameDesign[f"{gridX},{gridY}"]
    s.bgpic(f"{current_biome}.gif")
    current_animals =   biomes[current_biome]
    animal_house =      [tp for tk, tp in tpool.items() if tk in current_animals]

    for a in animal_house: a.showturtle()

    print(f"Welcome to the {current_biome} biome, enjoy the:\n",current_animals)

    move_animals = True
    do_move_animals()

def checkAnimalBorders(x,borders=gameBorders):

    if (x.xcor() >= borders['max_x'] or
        x.xcor() <= borders['min_x'] or
        x.ycor() >= borders['max_y'] or
        x.ycor() <= borders['min_y']):
        x.rt(180)
        x.fd(10)


def do_move_animals():

    if move_animals:

        for a in animal_house:

            if is_whistling:

                dist_to_player = distForm(a,player)

                move_x, move_y = 0,0

                if a.xcor() < player.xcor(): move_x = 5
                else: move_x = -5

                if a.ycor() < player.ycor(): move_y = 5
                else: move_y = -5

                #a.setheading(a.heading()+move_x+move_y)
                a.setpos(a.xcor()+move_x,a.ycor()+move_y)

            elif food_is_used:

                dist_to_food = distForm(a,food)

                move_x, move_y = 0,0

                if a.xcor() < food.xcor(): move_x = 5
                else: move_x = -5

                if a.ycor() < food.ycor(): move_y = 5
                else: move_y = -5

                #a.setheading(a.heading()+move_x+move_y)
                a.setpos(a.xcor()+move_x,a.ycor()+move_y)

            else:
                
                if rnum(1,100) > 50: a.rt(rnum(5,15))
                else: a.lt(rnum(5,15))
                a.fd(5)

            checkAnimalBorders(a)
            
        s.ontimer(do_move_animals,100)


# MAKE FOOD
food = turtle.Turtle()
food.hideturtle()
food.penup()
food.shape('square')
food.color('green')
food.shapesize(2,2)

food_is_used = False
is_whistling = False

def whistle():

    global is_whistling

    if is_whistling:
        is_whistling = False
        print('STOPPED Whistling')
        
    else:
        is_whistling = True
        print('STARTED Whistling')

def handleFood():

    global food_is_used
    
    if food.isvisible():

        for a in animal_house:

            if distForm(food,a) <= 50:
                food_is_used = False
                food.hideturtle()
                break

    s.ontimer(handleFood,100)

def placeFood(x,y):

    global food_is_used

    if not food_is_used:
        food_is_used = True
        food.setpos(x,y)
        food.showturtle()




s.onclick(placeFood)
s.onkeypress(whistle,'w')


set_biome()
handleFood()


# Last 2 Lines
s.listen()
s.mainloop()
