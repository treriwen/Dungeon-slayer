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
        self.last_direction_change_time = pygame.time.get_ticks()
        self.direction_change_delay = random.randint(1000, 2000)


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

        if time_since_last_move >= random.randint(1000, 3000):  # Choose a new direction randomly every 1 to 3 seconds
            self.last_move_time = now

            # Choose a new random direction
            x_direction, y_direction = random.choice([(-1, 0), (0, -1), (1, 0), (0, 1)])
            self.next_direction = pygame.Vector2(x_direction, y_direction).normalize()

            # Reset the direction change delay
            self.direction_change_delay = random.randint(1000, 2000)  # 1 to 2 seconds

        # Check if it's time to change the direction again
        time_since_last_direction_change = now - self.last_direction_change_time
        if time_since_last_direction_change >= self.direction_change_delay:
            x_direction, y_direction = random.choice([(-1, 0), (0, -1), (1, 0), (0, 1)])
            self.next_direction = pygame.Vector2(x_direction, y_direction).normalize()
            self.direction_change_delay = random.randint(1000, 2000)  # 1 to 2 seconds
            self.last_direction_change_time = now

        # Try to move the enemy in the current direction
        new_position = self.position + self.next_direction * self.speed
        new_rect = self.image.get_rect(topleft=new_position)

        # Check for collisions with walls
        if new_rect.collidelist(walls) == -1:
            self.position = new_position
            self.rect.topleft = self.position

    def get_image(self, x, y):
        image = pygame.Surface([16, 16])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 16, 16))
        return image