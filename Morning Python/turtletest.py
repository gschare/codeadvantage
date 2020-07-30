import turtle

screen = turtle.Screen()
screen.setup(width=300, height=300)

t = turtle.Turtle(shape="turtle")

def spin():
    t.left(20)

screen.onkey(spin, key="space")
screen.listen()
screen.mainloop()

# turtle.onkey(fun, key)
# fun - a function with no arguments
# key is just a string
