import pygame

pygame.init()

#setting the screen values
h, w = 540, 960

screen = pygame.display.set_mode([w, h])

#buttonpress-constants
steps = 10
source = [200,200]
direction = [0, 0, 0, 0]
ButtonPresses = [False, False, False, False]

#game variable
running = True

#framerate
FPS = 60
clock = pygame.time.Clock()

while running:
    #resetting direction list
    direction = [0, 0, 0, 0]

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
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

    player = pygame.Rect(source[0], source[1], 20, 20)

    screen.fill((255, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()