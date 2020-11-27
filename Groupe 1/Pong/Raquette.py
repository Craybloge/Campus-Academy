import pygame
BLACK = (0,0,0)

class Raquette(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0,0, width, height])
        self.rect = self.image.get_rect()


    def moveUp(self, mouvement):
        self.rect.y -= mouvement
        if self.rect.y < 0:
            self.rect.y = 0
    
    def moveDown(self, mouvement):
        self.rect.y += mouvement
        if self.rect.y > 400:
            self.rect.y = 400
    
    def moveLeft(self, mouvement):
        self.rect.x -= mouvement
        if self.rect.x < 0:
            self.rect.x = 0
        
    def moveRight(self, mouvement):
        self.rect.x += mouvement
        if self.rect.x >600:
            self.rect.x = 600