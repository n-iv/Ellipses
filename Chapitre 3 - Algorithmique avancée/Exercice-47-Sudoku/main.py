#Déclaration de la grille à partir du fichier txt
grille=[]
with open("sudoku.txt",'r') as fichier:
  for ligne in fichier:
    t=[]
    for car in ligne:
      if car!='\n':
        t.append(int(car))
    grille.append(t)

#Fonction pour afficher la grille joliment
def affGrille(g):
  t=""
  for i in range(9):
    for j in range(9):
      t+=str(g[i][j])+" "

      if j%3==2:
        t+="  "
    t+="\n"
    if i%3==2:
      t+="\n\n"
  return t

#Fonction pour vérifier s'il est possible de placer un nombre n à un endroit donné de la grille (x,y)
def possible(x,y,n):
  for i in range(9):
    if grille[x][i]==n:#le nombre est déjà sur la même colonne ?
      return False
    if grille[i][y]==n:#le nombre est déjà sur la même ligne ?
      return False
  for i in range(3):
    for j in range(3):
      if grille[(x//3)*3+i][(y//3)*3+j]==n:#le nombre est dans le même "carré" ?
        return False
  return True

#Solveur récursif à compléter
def solve():
  #L'esprit est de vérifier, pour chaque case, donc en parcourant toutes les lignes et toutes les colonnes, s'il y a un zéro, et le cas échéant, de vérifier pour tous les nombres de 1 à 9 s'ils peuvent être placés à cet endroit.
  #Si c'est le cas, on modifie la grille en fonction, et on résout la nouvelle grille !
  #Si ce n'est pas le cas, c'est qu'on s'est trompé : on fait un backtrack, i.e. on remet le 0 (et les boucles continuent de s'éxécuter).
  #Si aucun des 9 nombres n'est plaçable, c'est qu'on s'est planté quelque part : on fait un return pour laisser les fonctions ayant appelé la fonction courante s'exécuter.
  #En fin de solve, lorsque toutes les cases ont été remplies pour une fois, on affiche le résultat et on quitte. Ces lignes sont déjà écrites :
  print("====== Forme résolue ======\n")
  print(affGrille(grille))
  return

print("====== Forme initiale ======\n")
print(affGrille(grille))
solve()