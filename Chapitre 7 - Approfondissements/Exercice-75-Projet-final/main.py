import sys

import pygame
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Page blanche...')
while True:
   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
   pygame.display.update()