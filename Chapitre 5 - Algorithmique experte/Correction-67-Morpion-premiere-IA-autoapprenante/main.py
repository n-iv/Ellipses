from random import randint

grille = [' ' for i in range(10)]
cerveau = {}
partie = 0

def loadBrain():
  with open('brain.txt','r') as fichier:
    i=0
    for ligne in fichier:
      courant=ligne.split(";")
      eff = []
      for j in range(1,10):
        eff.append(int(courant[j]))
      cerveau[int(courant[0])]=eff
      i+=1
  if len(cerveau)==0:
    input("Rien dans le crâne !")

def trim():
  for i in cerveau:
    couper = 0
    for j in range(9):
      if cerveau[i][j]==100:
        couper = j
    if couper!=0:
      for j in range(9):
        cerveau[i][j]=0
      cerveau[i][couper]=100

def affGrille():
  print('\033[2J\033[1;1H')
  print(f"""  |   | 
 {grille[1]}| {grille[2]} |{grille[3]}
---------
 {grille[4]}| {grille[5]} |{grille[6]}
---------
 {grille[7]}| {grille[8]} |{grille[9]}
  |   |""")

def placeGrille(t,p):
  if grille[p]==" ":
    grille[p]=t
    return True
  return False

def win():
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

def legit():
  res=[]
  for i in range(1,10):
    if grille[i]==' ':
      res.append(i)
  return res

def cpuJoue(symb):
  global partie
  possibles=legit()
  if partie not in cerveau:
    cerveau[partie]=[100//len(legit())]*9
    for i in range(1,10):
      if i not in possibles:
        cerveau[partie][i-1]=0
  ecc=[]
  s=0
  for i in range(9):
    s+=cerveau[partie][i]
    ecc.append(s)
  while True:
    de=randint(0,s)
    for i,e in enumerate(ecc):
      if de<e and i+1 in legit():
        placeGrille(symb,i+1)
        partie=10*partie+i+1
        if partie not in cerveau:
          cerveau[partie]=[100//len(possibles)]*9
          for i in range(1,10):
            if i not in possibles:
              cerveau[partie][i-1]=0
        return

def joueurJoue(symb):
  global partie
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
          partie=10*partie+p
          if partie not in cerveau:
            cerveau[partie]=[100//len(legit())]*9
            for i in range(1,10):
              if i not in possibles:
                cerveau[partie][i-1]=0
            print("ok")
          return
    except:
      print("Un entier entre 1 et 9.")

c = input('train (t) or play (p)')

def remember(win):
  if win in ['X','O']:
    reward=4
  else:
    reward=1
  q=partie
  res = []
  for i in range(len(str(partie))):
    q,r=q//10,q%10
    #print(partie,q,r,i,'%=',len(str(partie)),max(cerveau[q][r-1]+1-reward,1),min(cerveau[q][r-1]+1+reward,99),cerveau[q])
    res.append(cerveau[q][r-1])
    if i==0:
      cerveau[q][r-1]=100
    elif i==1:
      cerveau[q][r-1]==0
    else:
      for j in range(i):
        cerveau[q][r-1]=cerveau[q][r-1]*res[j]**(1/i)
      cerveau[q][r-1]=round(cerveau[q][r-1]**(1/2))

  with open('brain.txt','w') as fichier:
    k=len(cerveau)
    for pickle in cerveau:
      k-=1
      fichier.write(str(pickle)+';')
      for i in range(9):
        fichier.write(str(cerveau[pickle][i]))
        if i<8:
          fichier.write(';')
      if k>0:
        fichier.write('\n')

if c=='t':
  c=input('combien de parties ? ')
  for cpt in range(int(c)):
    print(cpt)
    grille = [' ' for i in range(10)]
    cerveau = {}
    partie = 0
    loadBrain()
    if cpt%10==0:
      trim()
    winner = False
    current = 1
    while not winner:
      #affGrille()
      if current == 1:
        cpuJoue('X')
      else:
        cpuJoue('O')

      current = 1-current

      winner = win()

    #affGrille()
    #print(winner+' gagne.')

    remember(winner)

else:
  grille = [' ' for i in range(10)]
  cerveau = {}
  partie = 0
  loadBrain()
  trim()
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
  remember(winner)
