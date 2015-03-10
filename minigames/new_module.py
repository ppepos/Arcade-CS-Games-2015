import pygame
from pygame.locals import *
import singleplayer
from input_map import *

class ChiotteGame(singleplayer.Minigame):

    name = "Clean this shit!"
    duration = 15

    balai = pygame.image.load('./res/img/chiotte_clean/balai.png')
    bowl = pygame.image.load('./res/img/chiotte_clean/bowl.png')
    fat_turd = pygame.image.load('./res/img/chiotte_clean/fat_turd00.png')
    med_turd = pygame.image.load('./res/img/chiotte_clean/med_turd00.png')
    low_turd = pygame.image.load('./res/img/chiotte_clean/low_turd00.png')

    def __init__(self):
        self.result = False
        self.width, self.height = self.screen.get_size()

    def draw(self):
        self.screen.blit(bowl, 100, 100, 50, 50)

    def tick(self):
        for event in pygame.event.get():
            print event

    def get_results(self):
        return False
