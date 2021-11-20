import pygame
import movement as mv
import colliding as cl

pygame.init()

#setting the screen values
h, w = 540, 960

screen = pygame.display.set_mode([w, h])

#movement variables
steps = 30
source = [200,200]
player = pygame.Rect(source[0], source[1], 20, 20)
listOfObstacles = [pygame.Rect(0,400,800,20), pygame.Rect(200,300,800,20),pygame.Rect(400,380,20,20)]
listOfBlessings = [pygame.Rect(300,370,20,20)]
listOfCookies = []

#game variables
running = True
lifes = 0

#text variables
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

#framerate variables
FPS = 60
clock = pygame.time.Clock()
delta = 1

#falling acceleration variables
fallAcceleration = 3
isFalling = True

#collision variables
collideInfo = [0,0,""]
collideArray = []

while running:

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    #applying HardCollision for strong objects
    result = cl.applyHardCollision(player,listOfObstacles,source)
    closedKeys = result[0].copy()
    source = result[1].copy()

    if "up" in closedKeys:
        isFalling = False

    for collectible in listOfBlessings:
        if pygame.Rect.colliderect(player,collectible):
            listOfBlessings.remove(collectible)
            lifes += 1

    #draw the game
    player.update(source[0], source[1], 20, 20)
    screen.fill((255, 0, 0))
    textsurface = myfont.render('Punkte: '+str(lifes), False, (0, 0, 0))
    screen.blit(textsurface, (0,0))
    for obstacle in listOfObstacles:
        pygame.draw.rect(screen, (255, 255, 0), obstacle)
    for collectibles in listOfBlessings:
        pygame.draw.rect(screen, (255, 255, 0), collectibles)
    pygame.draw.rect(screen, (255, 255, 255), player)

    #calculating destiny of player and updating it
    source = mv.movementHandler(steps, source, delta, events, collideArray)
    source = mv.applyGravitation(fallAcceleration, source, isFalling, steps, delta)
    player.update(source[0], source[1], 20, 20)

    #update window
    pygame.display.flip()

    #deleting used values for movement and collision
    collideInfo = [0,0,""]
    collideArray = []
    isFalling = True

    #calculating delta
    milli = clock.tick(FPS)
    delta = milli/60

pygame.quit()