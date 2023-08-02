import pygame
import math


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 0, 0))  # Le projectile est un carré rouge de 10x10 pixels (vous pouvez changer l'apparence)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = angle
        self.speed = 5  # Vitesse du projectile (vous pouvez ajuster la vitesse selon vos besoins)

    def update(self):
        # Déplacer le projectile dans la direction de l'angle
        self.rect.x += self.speed * math.cos(math.radians(self.angle))
        self.rect.y -= self.speed * math.sin(math.radians(self.angle))  # Le sin est négatif car l'axe Y est inversé

        # Si le projectile sort de l'écran, le supprimer du groupe
        if not pygame.display.get_surface().get_rect().colliderect(self.rect):
            self.kill()


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

    def shoot(self):


        # Obtenir les coordonnées locales de la souris par rapport au joueur
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_x = mouse_x - 400
        mouse_y = mouse_y - 300

        # Calculer l'angle en radians entre le joueur et la position de la souris
        angle_rad = math.atan2(mouse_x, mouse_y)
        angle_deg = math.degrees(angle_rad)
        angle_deg = angle_deg - 90
        projectile = Projectile(0, 0, angle_deg)

        # Ajouter le projectile au groupe de projectiles
        self.projectiles.add(projectile)
        print('ok')

