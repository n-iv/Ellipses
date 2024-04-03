from random import randint, choice
from math import sqrt
import time
import pygame #importe la librairie pygame gérant le SDl en Python
from pygame.locals import * #importe les constantes de pygame directement dans le script
pygame.init() #initialisation de pygame

xfen,yfen=640,480
fenetre = pygame.display.set_mode((xfen,yfen), RESIZABLE) #taille de la fenêtre. On peut mettre FUllSCREEN pour être en plein écran.



#Définition des couleurs:
red=Color(255,0,0)
green=Color(0,255,0)
yellow=Color(255,255,0)
blue=Color(0,0,255)
white=Color(255,255,255)
black=Color(0,0,0)


#Définition des paramètres du rectangle :
x,y = 320,240 # raccourci pour affecter plusieurs variables à la fois
longueur,hauteur = 25,68
hauteur1,hauteur2=68,68
radius=20
a=choice([-1,1])
b=choice([-1,1])
c=1
w1,z1=0,yfen/2
w2,z2=xfen-longueur,yfen/2-hauteur/2
score=[0,0]
mal=[1,1,1,2,2,2,3,3,3,4]
bon=[5,5,5,6,6,6,7,7,7,8]


monImage=pygame.image.load("win pong.png").convert_alpha()
restart=pygame.image.load("restart.png").convert_alpha()
bonus=pygame.image.load("bonuspong.png").convert_alpha()
#malu=pygame.image.load("malus_pong.png").convert_alpha()
#malus=pygame.transform.scale(malu,(32,33))
bonusnoir=pygame.image.load("bonusnoir.png").convert_alpha()
monexplosion1=pygame.image.load("ep/explosion1.png").convert_alpha()
monexplosion2=pygame.image.load("ep/explosion2.png").convert_alpha()
monexplosion3=pygame.image.load("ep/explosion3.png").convert_alpha()
monexplosion4=pygame.image.load("ep/explosion4.png").convert_alpha()
monexplosion5=pygame.image.load("ep/explosion5.png").convert_alpha()
monexplosion6=pygame.image.load("ep/explosion6.png").convert_alpha()
monexplosion7=pygame.image.load("ep/explosion7.png").convert_alpha()
monexplosion8=pygame.image.load("ep/explosion8.png").convert_alpha()
monexplosion9=pygame.image.load("ep/explosion9.png").convert_alpha()
monexplosion10=pygame.image.load("ep/explosion10.png").convert_alpha()
monexplosion11=pygame.image.load("ep/explosion11.png").convert_alpha()


rectangle1 = Rect(w1,z1,longueur,hauteur1)
pygame.draw.rect(fenetre,blue,rectangle1)

rectangle2 = Rect(w2,z2,longueur,hauteur2)
pygame.draw.rect(fenetre,red,rectangle2)

normal1,normal2 = True,True
act_bonus=False
gagner=False
continuer=True
pygame.key.set_repeat(100,25)
while continuer:
  recommencer=True
  pygame.time.Clock().tick(150)
  pygame.draw.circle(fenetre, black, (int(x.__round__(0)),int(y.__round__(0))) , radius)

  if x>=xfen-radius:
    rectanglenoir2=Rect(0,y-radius,x,2*radius)
    pygame.draw.rect(fenetre,black,rectanglenoir2)
    #explosion
    pygame.draw.circle(fenetre, black, (int(x.__round__(0)),int(y.__round__(0))) , radius)
    fenetre.blit(monexplosion1,(x,y))
    pygame.time.wait(50)
    pygame.display.update()
    fenetre.blit(monexplosion11,(x-50,y-50))
    fenetre.blit(monexplosion2,(x-50,y-50))
    pygame.time.wait(50)
    pygame.display.update()
    fenetre.blit(monexplosion11,(x-50,y-50))
    fenetre.blit(monexplosion3,(x-50,y-50))
    pygame.time.wait(50)
    pygame.display.update()
    fenetre.blit(monexplosion11,(x-50,y-50))
    fenetre.blit(monexplosion4,(x-50,y-50))
    pygame.time.wait(50)
    pygame.display.update()
    fenetre.blit(monexplosion11,(x-50,y-50))
    fenetre.blit(monexplosion5,(x-50,y-50))
    pygame.time.wait(50)
    pygame.display.update()
    fenetre.blit(monexplosion11,(x-50,y-50))
    fenetre.blit(monexplosion6,(x-50,y-50))
    pygame.time.wait(50)
    pygame.display.update()
    fenetre.blit(monexplosion11,(x-50,y-50))
    fenetre.blit(monexplosion7,(x-50,y-50))
    pygame.time.wait(50)
    pygame.display.update()
    fenetre.blit(monexplosion11,(x-50,y-50))
    fenetre.blit(monexplosion8,(x-50,y-50))
    pygame.time.wait(50)
    pygame.display.update()
    fenetre.blit(monexplosion11,(x-50,y-50))
    fenetre.blit(monexplosion9,(x-50,y-50))
    pygame.time.wait(50)
    pygame.display.update()
    fenetre.blit(monexplosion11,(x-50,y-50))
    fenetre.blit(monexplosion10,(x-50,y-50))
    pygame.time.wait(50)
    pygame.display.update()
    fenetre.blit(monexplosion11,(x-50,y-50))
    pygame.time.wait(50)
    pygame.display.update()
    fenetre.blit(bonusnoir,(rdm_x,rdm_y))
    fenetre.blit(monImage,(180,150))
    pygame.display.update()
    fenetre.blit(restart,(150,350))
    score[0]+=1
    font=pygame.font.Font("freesansbold.ttf",30)
    score1=font.render(str(score[0]),True,(255,255,255))
    score2=font.render(str(score[1]),True,(255,255,255))
    barre=font.render("|",True,(255,255,255))
    pos1=(290,10)
    pos0=(320,10)
    pos2=(340,10)
    fenetre.blit(score1,pos1)
    fenetre.blit(score2,pos2)
    fenetre.blit(barre,pos0)
    pygame.display.update()
    gagner=True
    

    while recommencer:
      rectanglenoir=Rect(w2,z2,longueur,hauteur2)
      pygame.draw.rect(fenetre,black,rectanglenoir)
      rectanglenoir=Rect(w1,z1,longueur,hauteur1)
      pygame.draw.rect(fenetre,black,rectanglenoir)
      mal=[1,1,1,2,2,2,3,3,3,4]
      bon=[5,5,5,6,6,6,7,7,7,8]
      x,y = 320,240 # raccourci pour affecter plusieurs variables à la fois
      longueur,hauteur1,hauteur2 = 25,68,68
      radius=20
      a=choice([-1,1])
      b=choice([-1,1])
      c=1
      red=Color(255,0,0)
      green=Color(0,255,0)
      blue=Color(0,0,255)
      white=Color(255,255,255)
      black=Color(0,0,0)
      w1,z1=0,yfen/2
      w2,z2=xfen-longueur,yfen/2

      keys=pygame.key.get_pressed()
      if keys[pygame.K_SPACE]:
        
        rectangle1 = Rect(w1,z1,longueur,hauteur1)
        pygame.draw.rect(fenetre,blue,rectangle1)
        rectangle2 = Rect(w2,z2,longueur,hauteur2)
        pygame.draw.rect(fenetre,red,rectangle2)
        recommencer,gagner,act_bonus=False,False,False
        normal1,normal2 = True,True
  elif y>=yfen-radius:
    b=-1
    x,y=x+a*c,y+b
  elif x<=radius:
    rectanglenoir2=Rect(0,y-radius,x,2*radius)
    pygame.draw.rect(fenetre,black,rectanglenoir2)
    #explosion

    pygame.draw.circle(fenetre, black, (int(x.__round__(0)),int(y.__round__(0))) , radius)
    fenetre.blit(monexplosion1,(x,y))
    pygame.time.wait(50)
    pygame.display.update()
    fenetre.blit(monexplosion11,(x-50,y-50))
    fenetre.blit(monexplosion2,(x-50,y-50))
    pygame.time.wait(50)
    pygame.display.update()
    fenetre.blit(monexplosion11,(x-50,y-50))
    fenetre.blit(monexplosion3,(x-50,y-50))
    pygame.time.wait(50)
    pygame.display.update()
    fenetre.blit(monexplosion11,(x-50,y-50))
    fenetre.blit(monexplosion4,(x-50,y-50))
    pygame.time.wait(50)
    pygame.display.update()
    fenetre.blit(monexplosion11,(x-50,y-50))
    fenetre.blit(monexplosion5,(x-50,y-50))
    pygame.time.wait(50)
    pygame.display.update()
    fenetre.blit(monexplosion11,(x-50,y-50))
    fenetre.blit(monexplosion6,(x-50,y-50))
    pygame.time.wait(50)
    pygame.display.update()
    fenetre.blit(monexplosion11,(x-50,y-50))
    fenetre.blit(monexplosion7,(x-50,y-50))
    pygame.time.wait(50)
    pygame.display.update()
    fenetre.blit(monexplosion11,(x-50,y-50))
    fenetre.blit(monexplosion8,(x-50,y-50))
    pygame.time.wait(50)
    pygame.display.update()
    fenetre.blit(monexplosion11,(x-50,y-50))
    fenetre.blit(monexplosion9,(x-50,y-50))
    pygame.time.wait(50)
    pygame.display.update()
    fenetre.blit(monexplosion11,(x-50,y-50))
    fenetre.blit(monexplosion10,(x-50,y-50))
    pygame.time.wait(50)
    pygame.display.update()
    fenetre.blit(monexplosion11,(x-50,y-50))
    pygame.time.wait(50)
    pygame.display.update()
    fenetre.blit(bonusnoir,(rdm_x,rdm_y))
    fenetre.blit(monImage,(180,150))
    pygame.display.update()
    fenetre.blit(restart,(150,350))
    score[1]+=1
    font=pygame.font.Font("freesansbold.ttf",30)
    score1=font.render(str(score[0]),True,(255,255,255))
    score2=font.render(str(score[1]),True,(255,255,255))
    barre=font.render("|",True,(255,255,255))
    pos1=(290,10)
    pos0=(320,10)
    pos2=(340,10)
    fenetre.blit(score1,pos1)
    fenetre.blit(score2,pos2)
    fenetre.blit(barre,pos0)
    pygame.display.update()
    gagner=True
 
    while recommencer:
      rectanglenoir=Rect(w2,z2,longueur,hauteur2)
      pygame.draw.rect(fenetre,black,rectanglenoir)
      rectanglenoir=Rect(w1,z1,longueur,hauteur1)
      pygame.draw.rect(fenetre,black,rectanglenoir)
      x,y = 320,240 # raccourci pour affecter plusieurs variables à la fois
      longueur,hauteur1,hauteur2 = 25,68,68
      radius=20
      a=choice([-1,1])
      b=choice([-1,1])
      mal=[1,1,1,2,2,2,3,3,3,4]
      bon=[5,5,5,6,6,6,7,7,7,8]
      c=1
      w1,z1=0,yfen/2
      w2,z2=xfen-longueur,yfen/2
      red=Color(255,0,0)
      green=Color(0,255,0)
      blue=Color(0,0,255)
      white=Color(255,255,255)
      black=Color(0,0,0)

      keys=pygame.key.get_pressed()
      if keys[pygame.K_SPACE]:
       
        rectangle1 = Rect(w1,z1,longueur,hauteur1)
        pygame.draw.rect(fenetre,blue,rectangle1)
        rectangle2 = Rect(w2,z2,longueur,hauteur2)
        pygame.draw.rect(fenetre,red,rectangle2)
        recommencer,gagner,act_bonus=False,False,False
        normal1,normal2 = True,True

    #stopper et reprendre le programme après victoire
    #replacer explosion a lendroit de la balle
    #calculer le temps entre les explosions
    #un compteur de victoire

  elif y<=radius:
    b=1
    x,y=x+a*c,y+b


  elif x<=longueur+radius and y>=z1-hauteur+radius and y<=z1+hauteur+radius:
    
    milieu1=z1+hauteur/2
    if y ==milieu1:
      b=0
    elif y<milieu1:
      b=(y-milieu1)/10
    elif y>milieu1:
      b=(y-milieu1)/10
    a=1
    c*=1.09
    x,y=x+a*c,y+b
    touch=True


  elif x>=xfen-longueur-radius and y>=z2-hauteur+radius and y<=z2+hauteur+radius:

    milieu2=z2+hauteur/2
    if y ==milieu2:
      b=0
    elif y<milieu2:
      b=(y-milieu2)/10
    elif y>milieu2:
      b=(y-milieu2)/10
    a=-1
    c=c*1.09
    x,y=x+a*c,y+b
    touch=True




  else:
    x,y=x+a*c,y+b
  if gagner==False:
    pygame.draw.circle(fenetre,white, (int(x.__round__(0)),int(y.__round__(0))) , radius)
    #x,y=x*1.2,y*1.2

#rapidité de la balle a changer
#écran de victoire
#bonus et malus

  if act_bonus==False :
      rdm_x,rdm_y=randint(0,xfen),randint(0,yfen)
      rdm=randint(1,3000)
      if rdm<=1500:
        #fenetre.blit(malus,(rdm_x,rdm_y))
        act_bonus=True
      else:
        fenetre.blit(bonus,(rdm_x,rdm_y))
        act_bonus=True
  else:
    if sqrt((x-rdm_x)**2+(y-rdm_y)**2)+radius<60:
      #fenetre.blit(bonusnoir,(rdm_x,rdm_y))
      rdm=choice(mal) if act_bonus==True else choice(bon)
      act_bonus=False
      rdm=8
      if rdm==1:
        if a==-1:
          if blue==Color(10,10,10):
            rdm=choice(bon[3:])
          else:
            blue=Color(10,10,10)
        else:
          if red==Color(10,10,10):
            rdm=choice(bon[3:])
          else:
            red=Color(10,10,10)
      if rdm==2:
        if a==-1:
          rectanglenoir=Rect(w1,z1,longueur,hauteur1)
          pygame.draw.rect(fenetre,black,rectanglenoir)
          hauteur1=hauteur1/2
        else:
          rectanglenoir=Rect(w2,z2,longueur,hauteur2)
          pygame.draw.rect(fenetre,black,rectanglenoir)
          hauteur2=hauteur2/2
      if rdm==3:
        pygame.draw.circle(fenetre, black, (int(x.__round__(0)),int(y.__round__(0))) , radius)
        radius=radius//2
      if rdm==4:
        if a==-1:
            normal2=False
        else:
            normal1=False
      if rdm==8:
        if a==1:
            a,b,compt=0,0,0
            rectanglejaune=Rect(x,y-radius,xfen-x,2*radius)
            pygame.draw.rect(fenetre,yellow,rectanglejaune)
            while compt<1000:
                compt+=1
            a=4
            if touch==True:
                rectanglenoir2=Rect(rdm_x,rdm_y-radius,xfen-x,2*radius)
                pygame.draw.rect(fenetre,black,rectanglenoir2)
        else:
            a,b,compt=0,0,0
            rectanglejaune=Rect(0,rdm_y-radius,x,2*radius)
            pygame.draw.rect(fenetre,yellow,rectanglejaune)
            time.sleep(3)
            a=-4
            if touch==True:
                rectanglenoir2=Rect(0,rdm_y-radius,rdm_x,2*radius)
                pygame.draw.rect(fenetre,black,rectanglenoir2)
    else:
      fenetre.blit(bonus,(rdm_x,rdm_y)) if act_bonus==True else fenetre.blit(bonus,(rdm_x,rdm_y))






#suspent urgent de fou

  for event in pygame.event.get():
    if event.type==QUIT:
      continuer=False


    keys=pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
      if normal1:
          if z2+hauteur<yfen :
              rectanglenoir=Rect(w2,z2,longueur,hauteur2)
              pygame.draw.rect(fenetre,black,rectanglenoir)
              z2+=3*c
              rectangle2 = Rect(w2,z2,longueur,hauteur2)
              pygame.draw.rect(fenetre,red,rectangle2)
      else :
          if z2>0 :
              rectanglenoir=Rect(w2,z2,longueur,hauteur2)
              pygame.draw.rect(fenetre,black,rectanglenoir)
              z2-=3*c
              rectangle2 = Rect(w2,z2,longueur,hauteur2)
              pygame.draw.rect(fenetre,red,rectangle2)


    if keys[pygame.K_s]:
      if normal2:
          if z1>0:
              rectanglenoir=Rect(w1,z1,longueur,hauteur1)
              pygame.draw.rect(fenetre,black,rectanglenoir)
              z1-=3*c
              rectangle1 = Rect(w1,z1,longueur,hauteur1)
              pygame.draw.rect(fenetre,blue,rectangle1)
      else:
          if z1+hauteur<yfen:
              rectanglenoir=Rect(w1,z1,longueur,hauteur1)
              pygame.draw.rect(fenetre,black,rectanglenoir)
              z1+=3*c
              rectangle1 = Rect(w1,z1,longueur,hauteur1)
              pygame.draw.rect(fenetre,blue,rectangle1)

    if keys[pygame.K_x]:
      if normal2:
          if z1+hauteur<yfen:
              rectanglenoir=Rect(w1,z1,longueur,hauteur1)
              pygame.draw.rect(fenetre,black,rectanglenoir)
              z1+=3*c
              rectangle1 = Rect(w1,z1,longueur,hauteur1)
              pygame.draw.rect(fenetre,blue,rectangle1)
      else:
          if z1>0:
              rectanglenoir=Rect(w1,z1,longueur,hauteur1)
              pygame.draw.rect(fenetre,black,rectanglenoir)
              z1-=3*c
              rectangle1 = Rect(w1,z1,longueur,hauteur1)
              pygame.draw.rect(fenetre,blue,rectangle1)

    if keys[pygame.K_UP]:
      if normal1:
          if z2>0 :
              rectanglenoir=Rect(w2,z2,longueur,hauteur2)
              pygame.draw.rect(fenetre,black,rectanglenoir)
              z2-=3*c
              rectangle2 = Rect(w2,z2,longueur,hauteur2)
              pygame.draw.rect(fenetre,red,rectangle2)
      else:
          if z2+hauteur<yfen :
              rectanglenoir=Rect(w2,z2,longueur,hauteur2)
              pygame.draw.rect(fenetre,black,rectanglenoir)
              z2+=3*c
              rectangle2 = Rect(w2,z2,longueur,hauteur2)
              pygame.draw.rect(fenetre,red,rectangle2)

    if keys[pygame.K_h]:
      fenetre.blit(bonusnoir,(rdm_x,rdm_y))
      act_bonus=False
    touch=False
  pygame.display.update() # raffraîchit l'affichage de la fenêtre.


