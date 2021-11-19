import pygame

pygame.init()

#setting the screen values
h, w = 540, 960

screen = pygame.display.set_mode([w, h])

ButtonPresses = [False, False, False, False]
pressed = False

#game variable
running = True

FPS = 60
source = [200,200]
direction = [0, 0, 0, 0]

steps = 10

clock = pygame.time.Clock()

while running:

    source[0] = source[0] + direction[0] - direction[1]
    source[1] = source[1] + direction[2] - direction[3]

    direction = [0, 0, 0, 0]

    player = pygame.Rect(source[0], source[1], 20, 20)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                source[0] += 1 * steps
                ButtonPresses[0] = True
            if event.key == pygame.K_UP:
                source[0] -= 1 * steps
                ButtonPresses[1] = True
            if event.key == pygame.K_LEFT:
                source[1] -= 1 * steps
                ButtonPresses[2] = True
            if event.key == pygame.K_RIGHT:
                source[1] += 1 * steps
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

    
    screen.fill((255, 0, 0))
    #screen update
    pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()