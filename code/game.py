import pygame
import pyscroll
import pytmx

class GAME:

    def __init__(self):

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Dungeon Slayer')

        tmx_data = pytmx.util_pygame.load_pygame('../map/salle/dungeon/4.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        self.groupe = pyscroll.group.PyscrollGroup(map_layer=map_layer, default_layer=1, zoom=9)



    def run(self):

        running = True

        while running:

            self.groupe.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


        pygame.quit()


