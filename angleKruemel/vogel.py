import pygame

class vogel(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, scale):
        super().__init__()
        self.x = pos_x
        self.y = pos_y

        self.image = pygame.image.load("angleKruemel\sprites\hover\BossBieneAnimationHover_0006_Frame-1.png")

        self.size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.size[0]*scale), int(self.size[1]*scale)))

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]