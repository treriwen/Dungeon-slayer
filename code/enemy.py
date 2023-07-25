import pygame


class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y, sprite, life, speed, ia_type):
        super().__init__()
        self.position = [x, y]
        self.sprite = sprite
        self.life = life
        self.speed = speed
        self.type = ia_type
