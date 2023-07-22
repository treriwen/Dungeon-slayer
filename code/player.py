import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('../character/1 Pink_Monster/Pink_Monster.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.speed = 0.5

    def update(self):
        self.rect.topleft = self.position

    def move(self, direction):
        if direction == 'right':
            self.position[0] += self.speed

        elif direction == 'left':
            self.position[0] -= self.speed

        elif direction == 'top':
            self.position[1] -= self.speed

        elif direction == 'bottom':
            self.position[1] += self.speed


    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image
