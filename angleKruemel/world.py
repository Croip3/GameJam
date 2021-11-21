import pygame
class WorldObject(pygame.sprite.Sprite):
    def __init__(self, src, x, y, scale):
        super().__init__()
        self.image = pygame.image.load(src)

        self.size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.size[0]*scale), int(self.size[1]*scale)))

        self.rect = self.image.get_rect()
        print(self.rect)
        self.rect.topleft = [x, y]