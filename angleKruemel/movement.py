import pygame

#buttonpress-constants
direction = [0, 0, 0, 0]
ButtonPresses = [False, False, False, False]

#speed of falling
fallSpeed = 1

def movementHandler(steps, source, delta, events):
    
    global direction
    global ButtonPresses
    direction = [0, 0, 0, 0]

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                ButtonPresses[0] = True
            if event.key == pygame.K_UP:
                ButtonPresses[1] = True
            if event.key == pygame.K_LEFT:
                ButtonPresses[2] = True
            if event.key == pygame.K_RIGHT:
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
    
    source[0] = source[0] + direction[3]*delta - direction[2]*delta
    source[1] = source[1] - direction[1]*delta
    #source[1] = source[1] + direction[0]*delta - direction[1]*delta

    return source

def applyGravitation(fall, source, isFalling, steps, delta):
    
    global fallSpeed
    
    if isFalling and fallSpeed<2*steps:
        if fallSpeed == 0:
            fallSpeed = 1
        fallSpeed *= fall*fall
    elif not(isFalling):
        fallSpeed = 0

    source[1] += fallSpeed*delta

    return source