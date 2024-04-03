from random import randint,choice

class Grille():
  def __init__(self):
    self.grille=[' ' for i in range(10)] #Initialisation de la grille. ' ' pour case vide.
    self.winner=None

  def __str__(self): #Pour afficher une grille toute moche
    return f"""\033[2J\033[1;1H\n   |   | 
  {self.grille[1]}| {self.grille[2]} |{self.grille[3]}
  ---------
  {self.grille[4]}| {self.grille[5]} |{self.grille[6]}
  ---------
  {self.grille[7]}| {self.grille[8]} |{self.grille[9]}
   |   |"""

  def placeGrille(self,t,p): #Place un symbole sur la grille. Renvoie faux si la case est non vide.
    if self.grille[p]==" ":
      self.grille[p]=t
      if self.win():
        self.winner = t
      return True
    return False

  def win(self): #Vérifie que la grille actuelle a une victoire et renvoie le symbole victorieux le cas échéant.
    if self.grille[1]== self.grille[2] and self.grille[2]==self.grille[3] and self.grille[1]!=" ":
      return True
    if self.grille[4]== self.grille[5] and self.grille[4]==self.grille[6] and self.grille[4]!=" ":
      return True
    if self.grille[7]== self.grille[8] and self.grille[7]==self.grille[9] and self.grille[7]!=" ":
      return True
    if self.grille[1]== self.grille[4] and self.grille[1]==self.grille[7] and self.grille[1]!=" ":
      return True
    if self.grille[2]== self.grille[5] and self.grille[2]==self.grille[8] and self.grille[2]!=" ":
      return True
    if self.grille[3]== self.grille[6] and self.grille[3]==self.grille[9] and self.grille[3]!=" ":
      return True
    if self.grille[1]== self.grille[5] and self.grille[1]==self.grille[9] and self.grille[1]!=" ":
      return True
    if self.grille[3]== self.grille[5] and self.grille[3]==self.grille[7] and self.grille[3]!=" ":
      return True
    return False

  def legit(self): #Renvoie les cases libres.
    res=[]
    for i in range(1,10):
      if self.grille[i]==' ':
        res.append(i)
    return res

class Joueur(): #Super classe de joueur
  def __init__(self,symb):
    self.symb = symb

  def joue(self, partie):
    pass

class Humain(Joueur):
  def __init__(self,symb):
    super().__init__(symb) # initialise dans la super classe

  def joue(self,symb): #Jeu du joueur avec toutes les précautions.
    ligne=None
    while True:
      p=input("Où ? ")
      possibles=partie.legit()
      try:
        p=int(p)
        if p<1 or p>9:
          print("Entre 1 et 9")
        else:
          if p not in partie.legit():
            print("Emplacement déjà occupé.")
          else:
            return p
      except:
        print("Un entier entre 1 et 9.")

class Cpu(Joueur):
  def __init__(self,symb):
    super().__init__(symb) # initialise dans la super classe

  def joue(self,symb): #L'ordinateur joue au hasard.
    return choice(partie.legit())

class SmartCpu(Joueur):
  def __init__(self,symb):
    super().__init__(symb) # initialise dans la super classe

  def joue(self,symb):
    if len(partie.legit())==9:
      return randint(1,9)
    return self.smart(partie,self.symb)['emplacement']

  def smart(self,etat,joueur): #etat est un état du jeu, joueur est le symbole de celui qui doit jouer
    moi = self.symb
    lAutre = 'X' if joueur == 'O' else 'O'

    if etat.winner == lAutre: #si l'autre a gagné en l'état
      return {'emplacement':None,'score':(1 if lAutre==moi else -1)*(len(etat.legit())+1)}
    if len(etat.legit())==0:
      return {'emplacement':None,"score":0}
    if joueur == moi:
      best = {'emplacement':None,'score':-10000}
    else:
      best = {'emplacement':None,'score':10000}

    for p in etat.legit():
      etat.placeGrille(joueur,p)
      resultat = self.smart(etat,lAutre)

      #Backtrack
      etat.grille[p]=' '
      etat.winner = None
      resultat['emplacement']=p

      if joueur == moi:
        if resultat['score'] > best['score']:
          best = resultat
      else:
        if resultat['score'] < best['score']:
          best = resultat

    return best

partie = Grille()
p1 = Humain('X')
p2 = SmartCpu('O')

current = 'X'

while (not partie.winner) and len(partie.legit())>0:
  print(partie)
  if current == 'X':
    partie.placeGrille('X',p1.joue('X'))
  else:
    partie.placeGrille('O',p2.joue('O'))
  current = 'O' if current == 'X' else 'X'
  winner = partie.winner

print(partie)
if (not winner) and len(partie.legit())==0:
  print('Egalité.')
else:
  print(winner+' gagne.')