import pygame
import movement as mv
import colliding as cl
import jesus
import world

pygame.init()

#setting the screen values
h, w = 720, 1280

screen = pygame.display.set_mode([w, h])

#movement variables
steps = 40
closedKeys = set()
source = [200,200]

#merge
#obstacle = pygame.Rect(0,400,800,20)
listOfObstacles = [pygame.Rect(0,700,1100,20), pygame.Rect(200,300,800,30),pygame.Rect(400,670,20,30)]
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
FPS = 30
clock = pygame.time.Clock()
delta = 1

#player sprite
moving_sprites = pygame.sprite.Group()
player = jesus.Jesus(source[0], source[1], 0.5)
moving_sprites.add(player)

#falling acceleration variables
fallAcceleration = 5
isFalling = True


# platforms
platform_scale = 0.2
platform_sprites = pygame.sprite.Group()
platform1 = world.WorldObject('./sprites/platforms/earthmedium.png', 50, 400, platform_scale)
platform_sprites.add(platform1)

#obstacles
#merge
listOfObstacle.append(platform1.rect)


#collision variables
collideInfo = [0,0,""]
collideArray = []

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
                
    screen.fill((100, 0, 0))



    pygame.draw.rect(screen, (255, 255, 0), player.rect)
    pygame.draw.rect(screen, (255, 0, 0), player.getCollisionZone())

    if player.rect.width == 0 and player.rect.height == 0:
        running = False
    #applying HardCollision for strong objects
    result = cl.applyHardCollision(player.rect,listOfObstacles + listOfHostileObstacles,source, isFalling)
    if len(result[0]) != 0:
        closedKeys = result[0].copy()
    source = result[1].copy()

    if "up" in closedKeys:
        isFalling = False

    for collectible in listOfBlessings:
        if pygame.Rect.colliderect(player.rect,collectible):
            listOfBlessings.remove(collectible)
            lifes += 1

    #draw the game
    player.setPos(source[0], source[1])

    screen.fill((255, 0, 0))
    textsurface = myfont.render('Punkte: '+str(lifes), False, (0, 0, 0))
    screen.blit(textsurface, (0,0))
    #for obstacle in listOfObstacles:
    #    pygame.draw.rect(screen, (255, 255, 0), obstacle)
    for collectibles in listOfBlessings:
        pygame.draw.rect(screen, (255, 255, 0), collectibles)
    for hostiles in listOfHostileObstacles:
        pygame.draw.rect(screen, (0, 0, 0), hostiles)

    moving_sprites.draw(screen)
    moving_sprites.update(0.20)
    pygame.draw.rect(screen, (255, 255, 0), obstacle)
    platform_sprites.draw(screen)

    #source = mv.movementHandler(steps, source, delta, events, player)
    #calculating destiny of player and updating it

    source = mv.movementHandler(steps, source, delta, events, closedKeys, isFalling, player)

    source = mv.applyGravitation(fallAcceleration, source, isFalling, steps, delta)
    player.setPos(source[0], source[1])
    player.updateRect()

    for hostile in listOfHostileObstacles:
        if pygame.Rect.colliderect(player.rect,hostile) and not damaged:
            if lifes == 0:
                player.rect.width = 0
                player.rect.height = 0
                break
            lifes -= 1
            damaged = True
        elif not pygame.Rect.colliderect(player.rect,hostile):
            damaged = False

    #update window
    pygame.display.flip()

    #deleting used values for movement and collision
    collideInfo = [0,0,""]
    isFalling = True
    closedKeys.clear()

    #calculating delta
    milli = clock.tick(FPS)
    delta = milli/60

pygame.quit()
