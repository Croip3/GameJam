import pygame
import movement as mv

pygame.init()

#setting the screen values
h, w = 540, 960

screen = pygame.display.set_mode([w, h])

#buttonpress-constants
steps = 30
source = [200,200]
player = pygame.Rect(source[0], source[1], 20, 20)
obstacle = pygame.Rect(0,400,800,20)

#game variable
running = True

#framerate
FPS = 60
clock = pygame.time.Clock()
delta = 1

#falling acceleration
fallAcceleration = 1.1
isFalling = True

while running:

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    if pygame.Rect.colliderect(player,obstacle):
        isFalling = False
        source[1] = obstacle.y -19
    else:
        isFalling = True

    source = mv.movementHandler(steps, source, delta, events)
    source = mv.applyGravitation(fallAcceleration, source, isFalling, steps, delta)

    player.update(source[0], source[1], 20, 20)

    screen.fill((255, 0, 0))
    pygame.draw.rect(screen, (255, 255, 0), obstacle)
    pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.display.flip()
    delta = clock.tick(FPS)/60

pygame.quit()