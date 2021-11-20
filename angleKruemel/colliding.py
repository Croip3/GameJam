import pygame

oldsource = [-1,-1]
collideArray = []

def applyHardCollision(player, listOfObstacles, source):

    global oldsource
    global collideArray

    closedKeys = set()
    collideArray = []

    if oldsource == [-1,-1]:
        oldsource = source

    for obstacle in listOfObstacles:
        if pygame.Rect.colliderect(player,obstacle):
            #get infos about the direction, which the player is colliding
            collideInfo = directionCollided(pygame.Rect(oldsource[0],oldsource[1],20,20), player, obstacle)
            collideArray.append(collideInfo)
            #preserve gravitation
            for collideInfo in collideArray:
                closedKeys.add(collideInfo[2])
            
            #collision resets you to your old point

            if "left" == collideInfo[2]:
                source[0] = obstacle.x - player.width + 1
            if "right" == collideInfo[2]:
                source[0] = obstacle.x + obstacle.width - 1
            if "up" == collideInfo[2]: 
                source[1] = obstacle.y - player.height + 1 
            if "down" == collideInfo[2]:
                source[1] = obstacle.y + obstacle.height - 1

    oldsource = source.copy()

    return [closedKeys,source]

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

    #if you were left to a obstackle before colliding, then you safely came from the left
    if old.x + old.width < obstacle.x + 2:
        CollideDir[2] = "left"
    #same thing, just from the right
    elif old.x > obstacle.x + obstacle.width - 2:
        CollideDir[2] = "right"
    #if both dont apply, than you are under or over the obstackle. Therefore we need a simple distinction of cases
    else:
        if CollideDir[1] < 0:
            CollideDir[2] = "up"
        elif CollideDir[1] > 0:
            CollideDir[2] = "down"

    return CollideDir