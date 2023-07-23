import pygame
import pyscroll
import pytmx
from player import Player


class GAME:

    def __init__(self):

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Dungeon Slayer')

        tmx_data = pytmx.util_pygame.load_pygame('../map/dungeon/level1/1.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        self.spawnPointPlayer = tmx_data.get_object_by_name('spawnPointPlayer')


        self.player = Player(self.spawnPointPlayer.x, self.spawnPointPlayer.y)

        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == 'wallCollision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.groupe = pyscroll.group.PyscrollGroup(map_layer=map_layer, default_layer=1, zoom=9)
        self.groupe.add(self.player)

    def update(self):
        self.groupe.update()

        for sprite in self.groupe.sprites():
           if sprite.feet.collidelist(self.walls) > -1:
               sprite.move_back()


    def handle_input(self):
        pressed = pygame.key.get_pressed()


        if pressed[pygame.K_z]:
            self.player.move('top')

        if pressed[pygame.K_s]:
            self.player.move('bottom')

        if pressed[pygame.K_d]:
            self.player.move('right')

        if pressed[pygame.K_q]:
            self.player.move('left')




    def run(self):

        clock = pygame.time.Clock()

        running = True

        while running:

            self.player.save_position()
            self.handle_input()
            self.update()
            self.groupe.center(self.player.rect.center)
            self.groupe.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()
