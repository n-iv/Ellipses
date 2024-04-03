def creerFile():
  return []

def ajout(x,f):
  f.append(x)

def retrait(f):
  a = f[0]
  del f[0]
  return a

def longueur(f):
  return len(f)

def estVide(f):
  return longueur(f)==0

file = creerFile()

with open("stock.txt","r") as stock: #Ce fichier contient les numéros de série des objets stockés à vendre.
  for line in stock:
    ajout(line.strip(),file)

#2 éléments sont vendus.
if not(estVide(file)):
  retrait(file)
if not(estVide(file)):
  retrait(file)

#L'élément CKYZZU43 est ajouté.
ajout("CKYZZU43",file)

#3 éléments sont encore vendus.

if not(estVide(file)):
  retrait(file)
if not(estVide(file)):
  retrait(file)
if not(estVide(file)):
  retrait(file)

#Remettre le nouveau stock dans le fichier.
with open("stock.txt","w") as stock:
  for i in file:
    stock.write(i+"\n")