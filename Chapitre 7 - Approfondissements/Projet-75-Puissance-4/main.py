from tkinter import*



def afficher_grille_tk(tab):
  fen.title("Puissance 4")
  exit=Button(fen,text="Quitter",command=fen.destroy)
  if joueur==1:
    tour=Label(fen,image=player1)
  else:
    tour=Label(fen,image=player2)
  fen.rowconfigure(0,weight=1)
  fen.rowconfigure(1,weight=1)
  for o in range(7):
    fen.columnconfigure(o,weight=1)
    for p in range(6):
      fen.rowconfigure(p+2,weight=1)
      if tab[p][o]==0:
        jeton=Label(fen,image=blanc)
        jeton.grid(row=p+2,column=o)  
      if tab[p][o]==1:
        jeton=Label(fen,image=jeton1)
        jeton.grid(row=p+2,column=o)  
      if tab[p][o]==2:
        jeton=Label(fen,image=jeton2)
        jeton.grid(row=p+2,column=o) 
  global gagné
  rejouer=Button(fen,command=rejoue,text="Rejouer",state=DISABLED)
  gagné=Label(fen,text="                                                                                  ")
  gagné.grid(row=0,column=0,columnspan=7)
  if gagne(tab,1):
    gagné=Label(fen,text="Bravo joueur 1 vous avez triomphé!")
    gagné.grid(row=0,column=0,columnspan=7)
    but1=Button(fen,command=colonne1,image=button1,state=DISABLED)
    but2=Button(fen,command=colonne1,image=button2,state=DISABLED)
    but3=Button(fen,command=colonne3,image=button3,state=DISABLED)
    but4=Button(fen,command=colonne4,image=button4,state=DISABLED)
    but5=Button(fen,command=colonne5,image=button5,state=DISABLED)
    but6=Button(fen,command=colonne6,image=button6,state=DISABLED)
    but7=Button(fen,command=colonne7,image=button7,state=DISABLED)
    but1.grid(column=0,row=1)
    but2.grid(column=1,row=1)
    but3.grid(column=2,row=1)
    but4.grid(column=3,row=1)
    but5.grid(column=4,row=1)
    but6.grid(column=5,row=1)
    but7.grid(column=6,row=1)
    rejouer=Button(fen,command=rejoue,text="Rejouer")
  if gagne(tab,2):
    gagné=Label(fen,text="Bravo joueur 2 vous avez triomphé!")
    gagné.grid(row=0,column=0,columnspan=7)
    but1=Button(fen,command=colonne1,image=button1,state=DISABLED)
    but2=Button(fen,command=colonne1,image=button2,state=DISABLED)
    but3=Button(fen,command=colonne3,image=button3,state=DISABLED)
    but4=Button(fen,command=colonne4,image=button4,state=DISABLED)
    but5=Button(fen,command=colonne5,image=button5,state=DISABLED)
    but6=Button(fen,command=colonne6,image=button6,state=DISABLED)
    but7=Button(fen,command=colonne7,image=button7,state=DISABLED)
    but1.grid(column=0,row=1)
    but2.grid(column=1,row=1)
    but3.grid(column=2,row=1)
    but4.grid(column=3,row=1)
    but5.grid(column=4,row=1)
    but6.grid(column=5,row=1)
    but7.grid(column=6,row=1)
    rejouer=Button(fen,command=rejoue,text="Rejouer")
  if egalite(tab):
    égalité=Label(fen,text="Beau match! Malheureusement c'est une égalité.")
    égalité.grid(row=0,column=0,columnspan=7)
    but1=Button(fen,command=colonne1,image=button1,state=DISABLED)
    but2=Button(fen,command=colonne1,image=button2,state=DISABLED)
    but3=Button(fen,command=colonne3,image=button3,state=DISABLED)
    but4=Button(fen,command=colonne4,image=button4,state=DISABLED)
    but5=Button(fen,command=colonne5,image=button5,state=DISABLED)
    but6=Button(fen,command=colonne6,image=button6,state=DISABLED)
    but7=Button(fen,command=colonne7,image=button7,state=DISABLED)
    but1.grid(column=0,row=1)
    but2.grid(column=1,row=1)
    but3.grid(column=2,row=1)
    but4.grid(column=3,row=1)
    but5.grid(column=4,row=1)
    but6.grid(column=5,row=1)
    but7.grid(column=6,row=1)
    rejouer=Button(fen,command=rejoue,text="Rejouer")
  exit.grid(row=0,column=7)
  rejouer.grid(row=1,column=7)
  tour.grid(row=2,column=7)

def jouer_colonne(colonne):
  global joueur
  global but1
  if colonne_libre(tab,colonne):
    placer_jeton(tab, colonne, joueur)
  if colonne_libre(tab,colonne)==False:
    if colonne==1:
      but1=Button(fen,command=colonne1,image=button1,state=DISABLED)
      but1.grid(column=0,row=1)
    elif colonne==2:
      but2=Button(fen,command=colonne1,image=button2,state=DISABLED)
      but2.grid(column=1,row=1)
    elif colonne==3:
      but3=Button(fen,command=colonne3,image=button3,state=DISABLED)
      but3.grid(column=2,row=1)
    elif colonne==4:
      but4=Button(fen,command=colonne4,image=button4,state=DISABLED)
      but4.grid(column=3,row=1)
    elif colonne==5:
      but5=Button(fen,command=colonne5,image=button5,state=DISABLED)
      but5.grid(column=4,row=1)
    elif colonne==6:
      but6=Button(fen,command=colonne6,image=button6,state=DISABLED)
      but6.grid(column=5,row=1)
    elif colonne==7:
      but7=Button(fen,command=colonne7,image=button7,state=DISABLED)
      but7.grid(column=6,row=1)
  if joueur==2:
    joueur-=2   #pour avoir une variable joueur qui s'incrémente correctement jusqu'a la fin du match.
  joueur+=1
  afficher_grille_tk(tab)
    
def colonne1():
  jouer_colonne(1) 

def colonne2():
  jouer_colonne(2)

def colonne3():
  jouer_colonne(3)

def colonne4():
  jouer_colonne(4)

def colonne5():
  jouer_colonne(5)

def colonne6():
  jouer_colonne(6)

def colonne7():
  jouer_colonne(7)

def grille_zero():
  tab=[[0]*7 for x in range(6)] #on crée le tablau de jeu qui ne seras pas l'interface vue par le joueur, juste le lieu de calcul et de test.
  return tab



def afficher_grille(tab):
  txt_jetons=[" ","◉","◎"]
  print("╔"+"═══╦"*6+"═══╗")
  for i in range(0,6,1):
    for j in range(0,7,1):
      print("║"+" "+txt_jetons[tab[i][j]]+" ",end="")
    print("║")
    if i==5: #derniere ligne tableau
        print("╚"+"═══╩"*6+"═══╝")
    else: #interligne intérieur tableau
      print("╠"+"═══╬"*6+"═══╣")



def colonne_libre(tab, colonne) :
  if tab[0][colonne-1]==0:
    return True
  else:    
    return False

def placer_jeton(tab, colonne, joueur) : 
  i=5
  while tab[i][colonne-1]>0:
    i=i-1
  tab[i][colonne-1]=joueur

def quatre_horizontale(tab, joueur): 
  for i in range(6): 
    compte=0
    for j in range(6):
      if tab[i][j]==tab[i][j+1] and tab[i][j]==joueur:
         compte+=1
      else:
        compte=0
      if compte>=3:
        return True



def quatre_verticale(tab, joueur):
  for i in range(7):
    compte=0
    for j in range(5):
      if tab[j][i]==tab[j+1][i] and tab[j][i]==joueur:
         compte+=1
      else:
        compte=0
      if compte==3:
        return True
  return False



def quatre_diagonale(tab, joueur):
  for p in range(3): #ligne de départ pour les tests
    for k in range(0,4,1): #colonne de départ pour le test de gauche à droite
      compte=0
      i=k
      for j in range(p,p+3,1): #test diagonale de gauche à droite avec i la colonne et j la ligne
        if tab[j][i]==tab[j+1][i+1]==joueur:
          compte+=1
        else:
          compte=0
        if compte==3:
          return True
        i+=1
    for k in range(3,7,1): #colonne de départ pour test de droite à gauche
      compte=0
      i=k
      for d in range(p,p+3,1): #test diagonale de droite à gauche avec i la colonne et d la ligne
        if tab[d][i]==tab[d+1][i-1]==joueur:
          compte+=1
        else:
          compte=0
        if compte==3:
          return True 
        i-=1



def gagne(tab, joueur):
  if quatre_verticale(tab,joueur)==True:
    return True
  elif quatre_horizontale(tab, joueur)==True:
    return True
  elif quatre_diagonale(tab, joueur)==True:
    return True
  else:
    return False

def egalite(tab):
  if gagne(tab,1):
    return False
  if gagne(tab,2):
    return False
  for i in range(6):
    for j in range(7):
      if tab[i][j]==0:
        return False #si il reste des 0 dans le tablaux, (cases vides), ce parcours de liste de liste les trouveras et il n'y a donc pas d'égalité
  return True

def tour_joueur(tab, joueur):
  colonne=input("Dans quelle colonne voulez vous jouer ?  ")
  while colonne.isnumeric()==False: #vérification que la variable rentrée est un chiffre
    print("Entrez un numéro de colonne pas autre chose svp.")
    colonne=input("Dans quelle colonne voulez vous jouer ?  ")
  colonne=int(colonne)
  while colonne>7 or colonne==0:
    print("Cette colonne n'existe pas ou vous avez fait une faute de frappe. Réessayez.")
    colonne=input("Dans quelle colonne voulez vous jouer ?  ")
    while colonne.isnumeric()==False:
      print("Entrez un numéro de colonne pas autre chose svp.")
      colonne=input("Dans quelle colonne voulez vous jouer ?  ")
    colonne=int(colonne)
  while colonne_libre(tab, colonne-1)==False:
    print("La colonne est pleine, veuillez en choisire une autre")   
    colonne=int(input("Dans quelle colonne voulez vous jouer ?  "))
  placer_jeton(tab, colonne, joueur)

def jouer():
  tab=grille_zero()   #le jeu peut donc commencer avec la grille initiale et vide
  joueur=1
  while gagne(tab,1)==False and gagne(tab,2)==False and egalite(tab)==False:
    # tant qu'aucune condition de fin de jeux est validé, le jeu continue en montrant a chaque fin de tour/boucle la nouvelle grille
    afficher_grille(tab)
    tour_joueur(tab,joueur)
    if joueur==2:
      joueur-=2
    joueur+=1
  if gagne(tab,1)==True:
    afficher_grille(tab)
    print("Bravo joueur 1 vous avez triomphé!")
  elif gagne(tab,2)==True:
    afficher_grille(tab)
    print("Bravo joueur 2 vous avez triomphé!")
  elif egalite(tab)==True:            
    afficher_grille(tab)
    print("Beau match! Malheureusement c'est une égalité. Votre pouvoir est égal.")
    #ici nous mettons en lien toutes les fonctions qui signifie une fin de jeux, quand ces dernières ont lieu, le jeu s'arrette et un message s'affiche.

#initialisation du puissance 4 en tkinter
def initialisation():
  global fen
  global jeton1
  global jeton2
  global blanc
  global button1
  global button2
  global button3
  global button4
  global button5
  global button6
  global button7
  global tab
  global joueur
  global player1
  global player2
  fen=Tk()
  jeton1=PhotoImage(file="images/puissance 4 jaune.png")
  jeton2=PhotoImage(file="images/puissance 4 rouge.png")
  blanc=PhotoImage(file="images/puissance 4 blanc.png")
  button1=PhotoImage(file="images/billy.png")
  button2=PhotoImage(file="images/billynv.png")
  button3=PhotoImage(file="images/billyjsp.png")
  button4=PhotoImage(file="images/billy3.png")
  button5=PhotoImage(file="images/billy4.png")
  button6=PhotoImage(file="images/billy1.png")
  button7=PhotoImage(file="images/billy2.png")
  player1=PhotoImage(file="images/player1.png")
  player2=PhotoImage(file="images/player2.png")
  tab=grille_zero()
  joueur=1
  afficher_grille_tk(tab)
  but1=Button(fen,command=colonne1,image=button1)
  but2=Button(fen,command=colonne2,image=button2)
  but3=Button(fen,command=colonne3,image=button3)
  but4=Button(fen,command=colonne4,image=button4)
  but5=Button(fen,command=colonne5,image=button5)
  but6=Button(fen,command=colonne6,image=button6)
  but7=Button(fen,command=colonne7,image=button7)
  but1.grid(column=0,row=1)
  but2.grid(column=1,row=1)
  but3.grid(column=2,row=1)
  but4.grid(column=3,row=1)
  but5.grid(column=4,row=1)
  but6.grid(column=5,row=1)
  but7.grid(column=6,row=1)
  fen.mainloop()

def rejoue():
  global tab
  global joueur
  tab=grille_zero()
  joueur=1
  but1=Button(fen,command=colonne1,image=button1)
  but2=Button(fen,command=colonne2,image=button2)
  but3=Button(fen,command=colonne3,image=button3)
  but4=Button(fen,command=colonne4,image=button4)
  but5=Button(fen,command=colonne5,image=button5)
  but6=Button(fen,command=colonne6,image=button6)
  but7=Button(fen,command=colonne7,image=button7)
  but1.grid(column=0,row=1)
  but2.grid(column=1,row=1)
  but3.grid(column=2,row=1)
  but4.grid(column=3,row=1)
  but5.grid(column=4,row=1)
  but6.grid(column=5,row=1)
  but7.grid(column=6,row=1)
  afficher_grille_tk(tab)

a=input("Mode texte ou normal ?(T pour texte et N pour normal)     ")
if a=="T" or a=="t":
  jouer()
elif a=="N" or a=="n":
  print("Attention les smileys sont des boutons pour jouer")
  initialisation()
while a!="T" and a!="N":
  a=input("Mode texte ou normal ?(T pour texte et N pour normal)     ")
if a=="T" or a=="t":
  jouer()
elif a=="N" or a=="n":
  print("Attention les smileys sont des boutons pour jouer")
  initialisation()
