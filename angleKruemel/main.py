import pygame

#############
import jesus

pygame.init()

#setting the screen values
h, w = 540, 960

screen = pygame.display.set_mode([w, h])


#game variable
running = True

FPS = 60
x = 10
y = 10

steps = 10

clock = pygame.time.Clock()

moving_sprites = pygame.sprite.Group()
player = jesus.Jesus(x, y, 0.5, 10)
moving_sprites.add(player)

while running:

    #player = pygame.Rect(x, y, 20, 20)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player.down()
            if event.key == pygame.K_UP:
                player.up()
            if event.key == pygame.K_LEFT:
                player.left()
                player.walk()
            if event.key == pygame.K_RIGHT:
                player.right()
                player.walk()
                
    screen.fill((100, 0, 0))
    #screen update
    #pygame.draw.rect(screen, (255, 255, 255), player)

    moving_sprites.draw(screen)
    moving_sprites.update(0.20)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()