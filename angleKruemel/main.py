print ("angleKruemel gestartet")

import pygame

pygame.init()
screen = pygame.display.set_mode([400, 400])

running = True

x = 25
y = 250
#this is my test

steps = 10

while running:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                y += 1 * steps
            if event.key == pygame.K_UP:
                y -= 1 * steps
            if event.key == pygame.K_LEFT:
                x -= 1 * steps
            if event.key == pygame.K_RIGHT:
                x += 1 * steps
                
    screen.fill((255, 0, 0))

    pygame.draw.rect(screen, (255, 255, 255), (x, y, 20, 20))    

    #screen update
    pygame.display.flip()

pygame.quit()