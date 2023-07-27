import pygame
import math
from player import Player


class Weapon(pygame.sprite.Sprite):

    def __init__(self, player, sprite, name, damage, cost, attackType, criticalChance):
        super().__init__()
        self.player = player
        self.sprite_sheet = pygame.image.load(sprite)
        self.image = self.get_image(0, 80)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.angle = 0

        self.name = name
        self.damage = damage
        self.cost = cost
        self.attackType = attackType
        self.criticalChance = criticalChance

    def update(self):
        # Mettre à jour la position de l'arme pour qu'elle soit devant le joueur
        self.rect.center = self.player.rect.center
        mouse_position_X, mouse_position_Y = pygame.mouse.get_pos()

        # Calculer l'angle entre le joueur et la position de la souris
        dx = mouse_position_X - self.rect.centerx
        dy = mouse_position_Y - self.rect.centery
        self.angle = math.degrees(math.atan2(-dy, dx))

        self.image_weapon = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image_weapon.get_rect(center=self.rect.center)

    def get_image(self, x, y):
        image = pygame.Surface([32, 16])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 16))
        return image
