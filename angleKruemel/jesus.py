import pygame
class Jesus(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, size):
        super().__init__()
        self.x = pos_x
        self.y = pos_y
        self.walk_animation = False
        self.sprites = []

        self.sprites.append(pygame.image.load('./angleKruemel/sprites/jesus/JesusStraight.png'))
        self.sprites.append(pygame.image.load('./angleKruemel/sprites/jesus/JesusLeg2.png'))
        self.sprites.append(pygame.image.load('./angleKruemel/sprites/jesus/JesusStraight.png'))
        self.sprites.append(pygame.image.load('./angleKruemel/sprites/jesus/JesusLeg1.png'))

        for i in range(len(self.sprites)):
            sprite = self.sprites[i]
            self.size = sprite.get_size()
            self.sprites[i] = pygame.transform.scale(sprite, (int(self.size[0]*size), int(self.size[1]*size)))



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self, speed):
        self.rect.topleft = [self.x, self.y]
        if self.walk_animation == True:
            self.current_sprite += 1 * speed
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.walk_animation = False
            self.image = self.sprites[int(self.current_sprite)]

    def updateRect(self):
        self.rect.topleft = [self.x, self.y]

    def walk(self):
	    self.walk_animation = True

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def getCollisionZone(self):
        self.player_collision_zone = pygame.Rect(self.rect.left  + 90 , self.rect.top, self.rect.width-155 , self.rect.height)
        print(self.player_collision_zone)
        return self.player_collision_zone