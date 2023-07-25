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
        self.position = pygame.Vector2(x, y)
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

        if time_since_last_move >= self.pause_duration:
            direction = self.next_direction.normalize()

            # Déterminer si l'ennemi doit s'arrêter après ce mouvement
            should_pause = random.randint(1, 3) == 1
            if should_pause:
                self.pause_duration = random.randint(1000, 2000)  # Pause aléatoire entre 1 et 2 secondes
                self.last_move_time = now
            else:
                self.pause_duration = 0

                # Déplacer l'ennemi dans la direction actuelle
                self.position += direction * self.speed
                self.rect.topleft = self.position

                # Vérifier les collisions avec les murs
                if self.rect.collidelist(walls) != -1:
                    # En cas de collision avec un mur, revenir à la position précédente
                    self.position -= direction * self.speed
                    self.rect.topleft = self.position

                    # Choisir une nouvelle direction de déplacement aléatoire
                    self.next_direction = pygame.Vector2(1, 0).rotate(pygame.Vector2(0, 0).angle_to(direction))

                self.last_move_time = now
    def get_image(self, x, y):
        image = pygame.Surface([16, 16])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 16, 16))
        return image