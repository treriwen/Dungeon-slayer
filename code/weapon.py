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
        self.original_image = self.image
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

        # Obtenir les coordonnées locales de la souris par rapport au joueur
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_x = mouse_x-400
        mouse_y = mouse_y - 300

        # Calculer l'angle en radians entre le joueur et la position de la souris
        angle_rad = math.atan2(mouse_x, mouse_y)

        # Convertir l'angle en degrés
        angle_deg = math.degrees(angle_rad)
        angle_deg = angle_deg-90

        # Effectuer la rotation autour du centre de l'image
        self.image = pygame.transform.rotate(self.original_image, angle_deg)
        self.rect = self.image.get_rect(center=self.rect.center)

    def get_image(self, x, y):
        image = pygame.Surface([32, 16])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 16))
        return image
