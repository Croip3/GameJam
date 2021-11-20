import pygame
import movement as mv

#############
import jesus

pygame.init()

#setting the screen values
h, w = 540, 960

screen = pygame.display.set_mode([w, h])

#buttonpress-constants
steps = 30
source = [200,200]
obstacle = pygame.Rect(0,400,800,20)

#game variable
running = True

#framerate
FPS = 60

x = 10
y = 10

steps = 10


clock = pygame.time.Clock()
delta = 1

#player sprite
moving_sprites = pygame.sprite.Group()
player = jesus.Jesus(x, y, 0.5)
moving_sprites.add(player)

#falling acceleration
fallAcceleration = 1.1
isFalling = True

while running:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False
                
    screen.fill((100, 0, 0))

    moving_sprites.draw(screen)
    moving_sprites.update(0.20)


    if pygame.Rect.colliderect(player.rect, obstacle):
        isFalling = False
        source[1] = obstacle.y - player.rect.height-1
    else:
        isFalling = True

    source = mv.movementHandler(steps, source, delta, events, player)
    source = mv.applyGravitation(fallAcceleration, source, isFalling, steps, delta)
    player.setPos(source[0], source[1])

    pygame.draw.rect(screen, (255, 255, 0), obstacle)

    pygame.display.flip()
    delta = clock.tick(FPS)/60

pygame.quit()