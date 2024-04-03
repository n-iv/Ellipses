import pygame #importe la librairie pygame gérant le SDL en Python
from pygame.locals import * #importe les constantes de pygame directement dans le script
from datetime import datetime #pour récupérer l'heure courante
import math #pour faire un peu de trigonométrie

pygame.init() #initialisation de pygame
fenetre = pygame.display.set_mode((640,480), RESIZABLE) #taille de la fenêtre. On peut mettre FULLSCREEN pour être en plein écran.

blue=Color(0,0,255) # Couleur des aiguilles
white = Color(255,255,255) # Couleur initiale du fond

fond = pygame.image.load("fond2.jpg").convert_alpha()
fond = pygame.transform.scale(fond,(400,475))

while True:
  now = datetime.now() #instant actuel
  heures = int(now.strftime("%H"))+2 #heure actuelle avec décalage horaire de 2h
  minutes = int(now.strftime("%M")) #minute actuelle
  secondes = int(now.strftime("%S")) #seconde actuelle

  angleHeures = heures*2*math.pi/12-math.pi/2 #on calcule l'angle que fait l'aiguille des heures avec midi
  angleMinutes = minutes*2*math.pi/60-math.pi/2 #on calcule l'angle que fait l'aiguille des minutes avec midi
  angleSecondes = secondes*2*math.pi/60-math.pi/2 #on calcule l'angle que fait l'aiguille des secondes avec midi

  fenetre.blit(fond,(118,27))

  pygame.draw.line(fenetre,blue,(320,240),(320+80*math.cos(angleHeures),240+80*math.sin(angleHeures)),5) # chargement de l'aiguille des heures
  pygame.draw.line(fenetre,blue,(320,240),(320+130*math.cos(angleMinutes),240+120*math.sin(angleMinutes)),3) # chargement de l'aiguille des minutes
  pygame.draw.line(fenetre,blue,(320,240),(320+120*math.cos(angleSecondes),240+130*math.sin(angleSecondes)),1) # chargement de l'aiguille des secondes

  pygame.time.Clock().tick(30) #30 fps

  pygame.display.update() # Mise à jour de l'affichage