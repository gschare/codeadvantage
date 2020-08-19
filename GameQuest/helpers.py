import math

# Pythagorean distance formula between two points.
def distance(p1, p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

# check if an object hits the game border
def check_border_collision(p, radius, gamestate):
    left   = p[0] - radius < gamestate['min_x']
    right  = p[0] + radius > gamestate['max_x']
    bottom = p[1] - radius < gamestate['min_y']
    top    = p[1] + radius > gamestate['max_y']

    if left or right or bottom or top:
        return True
    else:
        return False

# check if two objects collide
def check_object_collision(p1, p2, r1, r2):
    if r1 + r2 > distance(p1, p2):
        return True
    else:
        return False