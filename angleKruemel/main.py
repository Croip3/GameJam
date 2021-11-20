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
oldsource = [200,200]
player = pygame.Rect(source[0], source[1], 20, 20)
listOfObstacles = [pygame.Rect(0,400,800,20), pygame.Rect(200,300,800,20),pygame.Rect(400,380,20,20)]

#game variables
running = True

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

    #find out which obstacle the player is colliding with
    for obstacle in listOfObstacles:
        if pygame.Rect.colliderect(player,obstacle):
            #get infos about the direction, which the player is colliding
            collideInfo = cl.directionCollided(pygame.Rect(oldsource[0],oldsource[1],20,20), player, obstacle)
            collideArray.append(collideInfo)
            #preserve gravitation
            if collideInfo[2] == "up":
                isFalling = False
            #collision resets you to your old point
            source = oldsource.copy()
    
    #draw the game
    player.update(source[0], source[1], 20, 20)
    screen.fill((255, 0, 0))
    for obstacle in listOfObstacles:
        pygame.draw.rect(screen, (255, 255, 0), obstacle)
    pygame.draw.rect(screen, (255, 255, 255), player)

    #save the previus position
    oldsource = source.copy()

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