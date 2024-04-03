from os import wait
import pygame #importe la librairie pygame gérant le SDL en Python
from pygame.locals import * #importe les constantes de pygame directement dans le script

pygame.init() #initialisation de pygame
fenetre = pygame.display.set_mode((640,480), RESIZABLE) #taille de la fenêtre. On peut mettre FULLSCREEN pour être en plein écran.


class Perso():
  def __init__(self,image,x=0,y=0,directionX=1,directionY=1):
    self.image = pygame.image.load(image).convert_alpha() # chargement du sprite
    self.x = x
    self.y = y
    self.directionX = directionX
    self.directionY = directionY

  def move(self):
      if self.x==0:
        self.directionX=1
      if self.x==640-60:
        self.directionX=-1
      if self.y==0:
        self.directionY=1
      if self.y==480-100:
        self.directionY=-1
      self.x+=self.directionX
      self.y+=self.directionY

  def collision(self,autre):
    if self.x<autre.x+autre.image.get_width() and self.x+self.image.get_width()>autre.x:
      if self.y<autre.y+autre.image.get_height() and self.y+self.image.get_height()>autre.y:
        return True
    return False

class Projectile():
  def __init__(self,image,x=0,y=0,directionX=1,directionY=1):
    self.image = pygame.image.load(image).convert_alpha() # chargement du sprite
    self.image = pygame.transform.scale(self.image, (50,50))
    self.x = x
    self.y = y
    self.directionX = directionX
    self.directionY = directionY

  def move(self):
    self.x+=self.directionX
    self.y+=self.directionY

fond = pygame.image.load("background.png").convert_alpha() #chargement du fond
naruto = Perso("naruto.png") # création d'un personnage
tobi = Perso("tobi.png",250,100) # création d'un second personnage

continuer = True # indicateur du fait que le joueur n'a pas encore quitté

pygame.key.set_repeat(100,25) #autorise le maintient d'une touche appuyée pour activer la répétition au bout de 100 ms, et toutes les 25 ms.

pause = False
last = pygame.time.get_ticks()
rasengans = []
victoire = False
defaite = False

while continuer: # tant que continuer ne devient pas faux
  for event in pygame.event.get():#on parcourt la liste des évènements

    """GESTION DU CLAVIER"""

    if event.type == QUIT:#si l'un d'eux est quitter, on quitte. QUIT est l'une des constantes locales de pygame.
      continuer = False #on sort donc de la boucle infinie
    elif event.type == KEYDOWN:#une touche est appuyée / on a aussi KEYUP : une touche est relâchée
      if not pause:
        if event.key == K_UP: #K_* où étoile est une lettre, un chiffre, ou le nom d'une touche
          naruto.y -= 5 # Naruto va vers le haut
        if event.key == K_DOWN:
          naruto.y += 5 # # Naruto va vers le bas
        if event.key == K_LEFT:
          naruto.x -= 5 # # Naruto va vers la gauche
        if event.key == K_RIGHT:
          naruto.x += 5 # # Naruto va vers la droite
      if event.key == K_SPACE:
        now = pygame.time.get_ticks()
        if now - last >= 500:
          last = pygame.time.get_ticks()
          pause = not pause # On active/désactive la pause

    elif not pause and event.type == MOUSEBUTTONDOWN:
      if event.button == 1:
        x, y = pygame.mouse.get_pos()
        norme = ((x - naruto.x)**2 + (y - naruto.y)**2)**(1/2)
        dir = ((x - naruto.x) / norme, (y - naruto.y) / norme)
        rasengans.append(Projectile("rasengan.png",naruto.x,naruto.y,15*dir[0],15*dir[1]))

  if not pause:
    tobi.move()
    if tobi.collision(naruto):
      defaite = True
    for atk in rasengans:
      atk.move()
      if tobi.collision(atk):
        victoire = True
      if atk.x > 640 or atk.x < 0 or atk.y > 480 or atk.y < 0:
        rasengans.remove(atk)

  fenetre.blit(fond,(0,0))
  fenetre.blit(naruto.image,(naruto.x,naruto.y))
  fenetre.blit(tobi.image,(tobi.x,tobi.y))
  for atk in rasengans:
    fenetre.blit(atk.image, (atk.x, atk.y))

  if any([victoire,defaite]):
    if victoire:
      fond = pygame.image.load("victoire.jpg").convert_alpha() #chargement du fond
    else:
      fond = pygame.image.load("defaite.jpg").convert_alpha() #chargement du fond
    fond = pygame.transform.scale(fond, (640,480))
    fenetre.blit(fond,(0,0))
    pygame.display.update() # Dernière mise à jour de l'affichage

  pygame.time.Clock().tick(30) #30 fps
  if not any([victoire,defaite]):
    pygame.display.update() # Mise à jour de l'affichage