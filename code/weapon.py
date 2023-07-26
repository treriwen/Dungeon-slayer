import pygame


class Weapon(pygame.sprite.Sprite):

    def __init__(self, sprite, name, damage, cost, attackType, criticalChance ):
        super().__init__()
        self.sprite = sprite
        self.name = name
        self.damage = damage
        self.cost = cost
        self.attackType = attackType
        self.criticalChance = criticalChance
