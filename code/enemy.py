import pygame
import random


class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y, sprite_sheet, life, speed, ia_type):
        super().__init__()
        self.position = [x, y]
        self.sprite_sheet = pygame.image.load(sprite_sheet)
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.life = life
        self.speed = speed
        self.type = ia_type
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 6)
        self.old_position = self.position.copy()
        self.next_direction = pygame.Vector2(1, 0)  # Direction initiale, par exemple vers la droite
        self.position = [x, y]
        self.last_move_time = pygame.time.get_ticks()
        self.pause_duration = 0


    def save_position(self):
        self.old_position = self.position.copy()

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move(self, walls):
        now = pygame.time.get_ticks()
        time_since_last_move = now - self.last_move_time

        if time_since_last_move >= random.randint(1000, 3000):  # Choisissez une nouvelle direction aléatoirement toutes les 1 à 3 secondes
            self.last_move_time = now

            # Choisir une nouvelle direction de déplacement aléatoire
            x_direction, y_direction = random.choice([(-1, 0), (0, -1), (1, 0), (0, 1)])
            self.next_direction = pygame.Vector2(x_direction, y_direction).normalize()

        # Essayer de déplacer l'ennemi dans la direction actuelle
        new_position = self.position + self.next_direction * self.speed
        new_rect = self.image.get_rect(topleft=new_position)

        # Vérifier les collisions avec les murs
        if new_rect.collidelist(walls) == -1:
            self.position = new_position
            self.rect.topleft = self.position
        else:
            # Si une collision avec un mur est détectée, choisir une nouvelle direction aléatoire
            x_direction, y_direction = random.choice([(-1, 0), (0, -1), (1, 0), (0, 1)])
            self.next_direction = pygame.Vector2(x_direction, y_direction).normalize()

    def get_image(self, x, y):
        image = pygame.Surface([16, 16])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 16, 16))
        return image