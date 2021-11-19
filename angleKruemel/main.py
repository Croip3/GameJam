import pygame

pygame.init()

#setting the screen values
h, w = 540, 960

screen = pygame.display.set_mode([w, h])


#game variable
running = True

FPS = 60
x = 250
y = 250

steps = 10

clock = pygame.time.Clock()

while running:

    player = pygame.Rect(x, y, 20, 20)

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
    #screen update
    pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()