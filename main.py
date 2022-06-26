import pygame, sys
from os.path import join
from settings import *
from level import Level

class Game:
    def __init__(self):

        # General Setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('RPG')
        self.clock = pygame.time.Clock()

        self.level = Level()

        # bg main sound
        main_bg_sound = pygame.mixer.Sound(join('.','assets','audio','main.ogg'))
        main_bg_sound.set_volume(0.1)
        main_bg_sound.play(loops = -1)
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()
            
            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()