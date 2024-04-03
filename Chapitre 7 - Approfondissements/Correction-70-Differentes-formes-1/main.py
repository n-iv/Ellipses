import pygame #importe la librairie pygame gérant le SDL en Python
from pygame.locals import * #importe les constantes de pygame directement dans le script

pygame.init() #initialisation de pygame
fenetre = pygame.display.set_mode((640,480), RESIZABLE) #taille de la fenêtre. On peut mettre FULLSCREEN pour être en plein écran.

#Définition des couleurs:
red=Color(255,0,0)
green=Color(0,255,0)
blue=Color(0,0,255)
white=Color(255,255,255)
black=Color(0,0,0)

#Définition des paramètres du rectangle :
x,y = 10,10 # raccourci pour affecter plusieurs variables à la fois
radius = 50
pygame.time.Clock().tick(30)#Maximum 30 frames par seconde .

while x<640 and y<480:
  pygame.time.Clock().tick(30)#Maximum 30 frames par seconde .
  pygame.draw.circle(fenetre,red,[x,y],radius) #disque
  pygame.display.update() # raffraîchit l'affichage de la fenêtre.
  x+=1
  y+=1
  pygame.draw.rect(fenetre,black,Rect(0,0,640,480))