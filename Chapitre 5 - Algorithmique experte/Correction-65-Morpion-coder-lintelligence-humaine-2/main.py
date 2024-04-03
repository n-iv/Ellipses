from random import randint

grille = [' ' for i in range(10)] #Initialisation de la grille. ' ' pour case vide.

def affGrille(): #Pour afficher une grille   print('\033[2J\033[1;1H')
  print(f"""  |   | 
 {grille[1]}| {grille[2]} |{grille[3]}
---------
 {grille[4]}| {grille[5]} |{grille[6]}
---------
 {grille[7]}| {grille[8]} |{grille[9]}
  |   |""")

def placeGrille(t,p): #Place un symbole sur la grille. Renvoie faux si la case est non vide.
  if grille[p]==" ":
    grille[p]=t
    return True
  return False

def win(): #Vérifie que la grille actuelle a une victoire et renvoie le symbole victorieux le cas échéant.
  if grille[1]== grille[2] and grille[2]==grille[3] and grille[1]!=" ":
    return grille[1]
  if grille[4]== grille[5] and grille[4]==grille[6] and grille[4]!=" ":
    return grille[4]
  if grille[7]== grille[8] and grille[7]==grille[9] and grille[7]!=" ":
    return grille[7]
  if grille[1]== grille[4] and grille[1]==grille[7] and grille[1]!=" ":
    return grille[1]
  if grille[2]== grille[5] and grille[2]==grille[8] and grille[2]!=" ":
    return grille[2]
  if grille[3]== grille[6] and grille[3]==grille[9] and grille[3]!=" ":
    return grille[3]  
  if grille[1]== grille[5] and grille[1]==grille[9] and grille[1]!=" ":
    return grille[1]
  if grille[3]== grille[5] and grille[3]==grille[7] and grille[3]!=" ":
    return grille[3]
  if grille.count(' ')==1:
    return ' '
  return False

def legit(): #Renvoie les cases libres.
  res=[]
  for i in range(1,10):
    if grille[i]==' ':
      res.append(i)
  return res

def cpuJoue(symb): #L'ordinateur gagne en un coup si c'est possible, sinon il joue en priorité le centre et les coins
  possibles=legit()
  for i in possibles:
    placeGrille(symb,i)
    if win():
      return
    grille[i]=' '
  if 5 in possibles:
    placeGrille(symb,5)
  elif any(i in possibles for i in [1,3,7,9]):
    coins = [i for i in possibles if i in [1,3,7,9]]
    placeGrille(symb,coins[randint(0,len(coins)-1)])
  else:
    i = randint(0,len(possibles)-1)
    placeGrille(symb,possibles[i])

def joueurJoue(symb): #Jeu du joueur avec toutes les précautions.
  ligne=None
  while True:
    p=input("Où ? ")
    possibles=legit()
    try:
      p=int(p)
      if p<1 or p>9:
        print("Entre 1 et 9")
      else:
        if not placeGrille(symb,p):
          print("Emplacement déjà occupé.")
        else:
          print("ok")
          return
    except:
      print("Un entier entre 1 et 9.")

winner = False
current = randint(0,1)

while not winner:
  affGrille()
  if current == 1:
    cpuJoue('X')
  else:
    joueurJoue('O')

  current = 1-current

  winner = win()

  affGrille()
  if winner not in ['X','O']:
    print('Egalité.')
  else:
    print(winner+' gagne.')