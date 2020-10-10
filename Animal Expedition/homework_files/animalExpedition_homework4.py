# Import
import turtle, random

# Screen
screen = turtle.Screen()
screen.bgcolor('black')
screen.title("Homework 4")

npcs = []

for i in range(100):
    npcs.append(turtle.Turtle())
    npcs[-1].speed(0)
    npcs[-1].shape('circle')
    npcs[-1].color('red')
    npcs[-1].setpos(random.randint(-200,200), random.randint(-200,200))

def move_the_npcs():

    for npc in npcs:
        npc.forward(random.randint(-50,50))
        npc.right(random.randint(-360,360))
    screen.ontimer(move_the_npcs,10)

move_the_npcs()


# LAST 2 LINES -----
screen.listen()
screen.mainloop()



