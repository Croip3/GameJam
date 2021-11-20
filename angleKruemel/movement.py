import pygame

#buttonpress variables
direction = [0, 0, 0, 0]
ButtonPresses = [False, False, False, False]

#speed of falling
fallSpeed = 1

def movementHandler(steps, source, delta, events, collideArray, isFalling):
    #set the variables global to adjust them in runtime
    global direction
    global ButtonPresses
    direction = [0, 0, 0, 0]
    #initialize a set for infunctional key because you collided
    closedKeys = set()
    for collideInfo in collideArray:
        closedKeys.add(collideInfo[2])

    #starting event loop
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and "up" not in closedKeys:
                ButtonPresses[0] = True
            if event.key == pygame.K_UP and "down" not in closedKeys and not isFalling:
                ButtonPresses[1] = True
            if event.key == pygame.K_LEFT and "right" not in closedKeys:
                ButtonPresses[2] = True
            if event.key == pygame.K_RIGHT and "left" not in closedKeys:
                ButtonPresses[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                ButtonPresses[0] = False
            if event.key == pygame.K_UP:
                ButtonPresses[1] = False
            if event.key == pygame.K_LEFT:
                ButtonPresses[2] = False
            if event.key == pygame.K_RIGHT:
                ButtonPresses[3] = False

    for i in range(0,4,1):
        if ButtonPresses[i]:
            direction[i] += 1 * steps
    
    #applying the direction which was pressed
    source[0] = source[0] + direction[3]*delta - direction[2]*delta
    source[1] = source[1] - direction[1]*delta

    return source

def applyGravitation(fall, source, isFalling, steps, delta):
    #set the variables global to adjust them in runtime
    global fallSpeed
    
    #maximum fallspeed shouldn't be higher than a specific value near "steps"
    if isFalling and fallSpeed<2*steps:
        if fallSpeed == 0:
            fallSpeed = 1
        fallSpeed += fall*delta
    elif not(isFalling):
        fallSpeed = 0

    source[1] += fallSpeed*delta

    return source