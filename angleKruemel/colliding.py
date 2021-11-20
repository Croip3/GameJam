import pygame
import numpy as np

#this method is there to return the directions in which the player is colliding with something
def directionCollided(old, new, obstacle):
    #calculating the deltavalues to determine directions
    delta_x = new.x - old.x
    delta_y = new.y - old.y

    CollideDir = [0, 0, ""]

    #simple distinction of cases
    if delta_x > 0:
        CollideDir[0] = 1
    elif delta_x < 0:
        CollideDir[0] = -1
    else:
        CollideDir[0] = 0
    if delta_y > 0:
        CollideDir[1] = -1
    elif delta_y < 0:
        CollideDir[1] = 1
    else:
        CollideDir[1] = 0

    #if the values didn't changed from the player, then he must stand on a obstackle
    if CollideDir[0] == 0 and CollideDir[1] == 0:
        return [0, 0, "up"]

    #if you were left to a obstackle before colliding, then you safely came from the left
    if old.x + old.width < obstacle.x:
        CollideDir[2] = "left"
    #same thing, just from the right
    elif old.x > obstacle.x + obstacle.width:
        CollideDir[2] = "Right"
    #if both dont apply, than you are under or over the obstackle. Therefore we need a simple distinction of cases
    else:
        if CollideDir[1] < 0:
            CollideDir[2] = "up"
        elif CollideDir[1] > 0:
            CollideDir[2] = "down"

    return CollideDir