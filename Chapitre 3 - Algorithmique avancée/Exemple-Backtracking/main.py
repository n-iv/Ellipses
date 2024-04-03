from random import randint

liste=[]

def de():
  return randint(1,6)

def jets():
  liste.append(de())
  print(liste)
  for k,v in enumerate(liste):
    if v in liste[:k]+liste[k+1:]:#Remarquer que liste[valeurTropGrande:] est vide.
      liste.pop() #backtracking
      jets() #et on réessaye
  if len(liste)<6:
    jets()
  return

jets()