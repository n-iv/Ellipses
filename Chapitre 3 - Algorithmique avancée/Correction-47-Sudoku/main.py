grille=[]
with open("sudoku.txt",'r') as fichier:
  for ligne in fichier:
    t = []
    for car in ligne:
      if car != '\n':
        t.append(int(car))
    grille.append(t)

def affGrille(g):
  t = ""
  for i in range(9):
    for j in range(9):
      t+=str(g[i][j])+" "
      if j%3 == 2:
        t += "  "
    t += "\n"
    if i%3 == 2:
      t += "\n\n"
  return t

def possible(x,y,n):
  for i in range(9):
    if grille[x][i]==n:
      return False
    if grille[i][y]==n:
      return False
  for i in range(3):
    for j in range(3):
      if grille[(x//3)*3+i][(y//3)*3+j]==n:
        return False
  return True

def solve():
  for x in range(9):
    for y in range(9):
      if grille[x][y] == 0:
        for chiffre in range(1, 10):
          if possible(x, y, chiffre):
            grille[x][y] = chiffre
            solve()
            grille[x][y] = 0
        return 

  print("====== Forme résolue ======\n")
  print(affGrille(grille))
  return

print("====== Forme initiale ======\n")
print(affGrille(grille))
solve()