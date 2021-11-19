import pygame
import movement as mv

pygame.init()

#setting the screen values
h, w = 540, 960

screen = pygame.display.set_mode([w, h])

#buttonpress-constants
steps = 10
source = [200,200]

#game variable
running = True

#framerate
FPS = 60
clock = pygame.time.Clock()

while running:

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    source = mv.movementHandler(steps, source, events)

    player = pygame.Rect(source[0], source[1], 20, 20)

    screen.fill((255, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()