import random

def quickSort(t): # algorithme de tri récursif sur une liste
  if len(t) <= 1: # si la liste contient un ou zéro élément
    print(t,"est trié")
    return t # elle est déjà triée...
  pivot = t[0] # on choisit le premier élément
  gauche = [] # on va mettre tous les plus petits dans une liste
  droite = [] # et tous les plus grands dans une autre
  #Comparer, un à un, les éléments du tableau au pivot. S'ils sont plus petits, ils vont à gauche, sinon à droite.
  #Renvoyer ensuite le résultat qui est la concaténation du tableau de gauche (à trier), du pivot et du tableau de droite (à trier aussi).

table=[random.randint(1,100) for i in range(10)]

print("début : ",table)

tableTriee = quickSort(table)

print("\n fin : ",tableTriee)