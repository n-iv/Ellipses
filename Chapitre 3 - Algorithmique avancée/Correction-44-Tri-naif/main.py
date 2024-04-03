import random

def cherche_min(t):
  minimum = t[0]
  indice = 0

  for k,valeur in enumerate(t):
    if valeur<minimum:
      minimum=valeur
      indice=k

  return indice

def tri_naif(t): # algorithme de tri récursif sur une liste
  if len(t) == 1: # si la liste contient un seul élément, elle est déjà triée
    return [t[0]]
  else: # sinon
    return [t[cherche_min(t)]] + tri_naif(t[:cherche_min(t)] + t[cherche_min(t)+1:])

table=[random.randint(1,100) for i in range(10)]

print("début : ",table)

tableTriee = tri_naif(table)

print("\n fin : ",tableTriee)