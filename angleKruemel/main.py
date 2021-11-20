import pygame
import movement as mv
import colliding as cl

pygame.init()

#setting the screen values
h, w = 540, 960

screen = pygame.display.set_mode([w, h])

#movement variables
steps = 40
closedKeys = set()
source = [200,200]
player = pygame.Rect(source[0], source[1], 20, 20)
listOfObstacles = [pygame.Rect(0,400,800,20), pygame.Rect(200,300,800,30),pygame.Rect(400,370,20,30)]
listOfBlessings = [pygame.Rect(300,370,20,20)]
listOfCookies = []
listOfHostileObstacles = [pygame.Rect(0,300,100,20)]

#game variables
running = True
lifes = 0
damaged = False

#text variables
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

#framerate variables
FPS = 300
clock = pygame.time.Clock()
delta = 1

#falling acceleration variables
fallAcceleration = 5
isFalling = True

#collision variables
collideInfo = [0,0,""]
collideArray = []

while running:

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    if player.width == 0 and player.height == 0:
        running = False

    #applying HardCollision for strong objects
    result = cl.applyHardCollision(player,listOfObstacles + listOfHostileObstacles,source, isFalling)
    if len(result[0]) != 0:
        closedKeys = result[0].copy()
    source = result[1].copy()

    if "up" in closedKeys:
        isFalling = False

    print(closedKeys)

    for collectible in listOfBlessings:
        if pygame.Rect.colliderect(player,collectible):
            listOfBlessings.remove(collectible)
            lifes += 1

    #draw the game
    player.update(source[0], source[1], player.width, player.height)
    screen.fill((255, 0, 0))
    textsurface = myfont.render('Punkte: '+str(lifes), False, (0, 0, 0))
    screen.blit(textsurface, (0,0))
    for obstacle in listOfObstacles:
        pygame.draw.rect(screen, (255, 255, 0), obstacle)
    for collectibles in listOfBlessings:
        pygame.draw.rect(screen, (255, 255, 0), collectibles)
    for hostiles in listOfHostileObstacles:
        pygame.draw.rect(screen, (0, 0, 0), hostiles)
    pygame.draw.rect(screen, (255, 255, 255), player)

    #calculating destiny of player and updating it
    source = mv.movementHandler(steps, source, delta, events, collideArray, isFalling)
    source = mv.applyGravitation(fallAcceleration, source, isFalling, steps, delta)
    player.update(source[0], source[1], player.width, player.height)

    for hostile in listOfHostileObstacles:
        if pygame.Rect.colliderect(player,hostile) and not damaged:
            if lifes == 0:
                player.width = 0
                player.height = 0
                break
            lifes -= 1
            damaged = True
        elif not pygame.Rect.colliderect(player,hostile):
            damaged = False

    #update window
    pygame.display.flip()

    #deleting used values for movement and collision
    collideInfo = [0,0,""]
    collideArray = []
    isFalling = True
    closedKeys.clear()

    #calculating delta
    milli = clock.tick(FPS)
    delta = milli/60

pygame.quit()