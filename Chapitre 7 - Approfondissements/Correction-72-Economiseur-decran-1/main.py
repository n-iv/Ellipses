import pygame #importe la librairie pygame gérant le SDL en Python
from pygame.locals import * #importe les constantes de pygame directement dans le script

pygame.init() #initialisation de pygame
fenetre = pygame.display.set_mode((640,480), RESIZABLE) #taille de la fenêtre. On peut mettre FULLSCREEN pour être en plein écran.

class Perso():
  def __init__(self,image,x=0,y=0,directionX=1,directionY=1):
    self.image = pygame.image.load(image).convert_alpha()
    self.x = x
    self.y = y
    self.directionX = directionX
    self.directionY = directionY

fond = pygame.image.load("background.png").convert_alpha()
naruto = Perso("naruto.png")
tobi = Perso("tobi.png",250,100)

while True:
  couleur = Color(255,255,255)

  fenetre.blit(fond,(0,0))
  fenetre.blit(naruto.image,(naruto.x,naruto.y))
  fenetre.blit(tobi.image,(tobi.x,tobi.y))

  if naruto.x==0:
    naruto.directionX=1
  if naruto.x==640-60:
    naruto.directionX=-1
  if naruto.y==0:
    naruto.directionY=1
  if naruto.y==480-100:
    naruto.directionY=-1
  naruto.x+=naruto.directionX
  naruto.y+=naruto.directionY

  if tobi.x==0:
    tobi.directionX=1
  if tobi.x==640-60:
    tobi.directionX=-1
  if tobi.y==0:
    tobi.directionY=1
  if tobi.y==480-100:
    tobi.directionY=-1
  tobi.x+=tobi.directionX
  tobi.y+=tobi.directionY

  pygame.time.Clock().tick(30) #30 fps

  pygame.display.update() # Mise à jour de l'affichage