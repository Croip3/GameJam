import pygame

#buttonpress-constants
direction = [0, 0, 0, 0]
ButtonPresses = [False, False, False, False]

def movementHandler(steps, source, events):
    
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
    
    source[0] = source[0] + direction[3] - direction[2]
    source[1] = source[1] + direction[0] - direction[1]

    return source