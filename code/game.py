import pygame
import pyscroll
import pytmx
from player import Player


class GAME:

    def __init__(self):

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Dungeon Slayer')

        tmx_data = pytmx.util_pygame.load_pygame('../map/salle/dungeon/1.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        self.player = Player(30, 40)

        self.groupe = pyscroll.group.PyscrollGroup(map_layer=map_layer, default_layer=1, zoom=9)
        self.groupe.add(self.player)

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_d]:
            self.player.move('right')

        if pressed[pygame.K_q]:
            self.player.move('left')

        if pressed[pygame.K_z]:
            self.player.move('top')

        if pressed[pygame.K_s]:
            self.player.move('bottom')

    def run(self):

        running = True

        while running:

            self.handle_input()
            self.groupe.update()
            self.groupe.center(self.player.rect.center)
            self.groupe.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()
