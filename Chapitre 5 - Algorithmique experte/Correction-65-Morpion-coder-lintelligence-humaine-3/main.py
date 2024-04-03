from random import randint

class Grille():

  def __init__(self):
        self.grille =[' ' for i in range(10)]
        self.current = randint(0,1)

  def affGrille(self):
    print('\033[2J\033[1;1H')
    print(f"""    |   | 
   {self.grille[1]}| {self.grille[2]} |{self.grille[3]}
  ---------
   {self.grille[4]}| {self.grille[5]} |{self.grille[6]}
  ---------
   {self.grille[7]}| {self.grille[8]} |{self.grille[9]}
    |   |""")

  def placeGrille(self,t,p):
    if self.grille[p]==" ":
      self.grille[p]=t
      return True
    return False

  def win(self):
    if self.grille[1]== self.grille[2] and self.grille[2]==self.grille[3] and self.grille[1]!=" ":
      return self.grille[1]
    if self.grille[4]== self.grille[5] and self.grille[4]==self.grille[6] and self.grille[4]!=" ":
      return self.grille[4]
    if self.grille[7]== self.grille[8] and self.grille[7]==self.grille[9] and self.grille[7]!=" ":
      return self.grille[7]
    if self.grille[1]== self.grille[4] and self.grille[1]==self.grille[7] and self.grille[1]!=" ":
      return self.grille[1]
    if self.grille[2]== self.grille[5] and self.grille[2]==self.grille[8] and self.grille[2]!=" ":
      return self.grille[2]
    if self.grille[3]== self.grille[6] and self.grille[3]==self.grille[9] and self.grille[3]!=" ":
      return self.grille[3]  
    if self.grille[1]== self.grille[5] and self.grille[1]==self.grille[9] and self.grille[1]!=" ":
      return self.grille[1]
    if self.grille[3]== self.grille[5] and self.grille[3]==self.grille[7] and self.grille[3]!=" ":
      return self.grille[3]
    if self.grille.count(' ')==1:
      return ' '
    return False

  def legit(self): 
    res=[]
    for i in range(1,10):
      if self.grille[i]==' ':
        res.append(i)
    return res

class Cpu():
  def cpuJoue(self,symb):
    possibles=partie.legit()
    for i in possibles:
      partie.placeGrille(symb,i)
      if partie.win():
        return
      partie.grille[i]=' '
    if 5 in possibles:
      partie.placeGrille(symb,5)
    elif any(i in possibles for i in [1,3,7,9]):
      coins = [i for i in possibles if i in [1,3,7,9]]
      partie.placeGrille(symb,coins[randint(0,len(coins)-1)])
    else:
      i = randint(0,len(possibles)-1)
      partie.placeGrille(symb,possibles[i])

class Joueur():
  def __init__(self):
        self.grille =[' ' for i in range(10)]

  def joueurJoue(self,symb):
    while True:
      p=input("Où ? ")
      possibles=partie.legit()
      try:
        p=int(p)
        if p<1 or p>9:
          print("Entre 1 et 9")
        else:
          if not partie.placeGrille(symb,p):
            print("Emplacement déjà occupé.")
          else:
            print("ok")
            return
      except:
        print("Un entier entre 1 et 9.")

winner = False
ordi = Cpu()
partie = Grille()
player = Joueur()

while not winner:
  partie.affGrille()
  if partie.current == 1:
    ordi.cpuJoue('X')
  else:
    player.joueurJoue('O')

  partie.current = 1-partie.current

  winner = partie.win()

  partie.affGrille()
  if winner not in ['X','O']:
    print('Egalité.')
  else:
    print(winner+' gagne.')