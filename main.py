import pygame, sys
from pygame.locals import QUIT

from test import Player


pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hello World!')

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

shooter = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    DISPLAYSURF.fill(GREEN)

    shooter.display(DISPLAYSURF, BLACK)
  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
