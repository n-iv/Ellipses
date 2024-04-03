from random import randint

def quickSort(t): 
  if len(t) <= 1: 
    return t 

  pivot = t[0] 
  gauche = [] 
  droite = [] 

  for valeur in t[1:]:
    if valeur < pivot:
      gauche.append(valeur)
    else:
      droite.append(valeur)

  return quickSort(gauche) + [pivot] + quickSort(droite)

table=[randint(1,100) for i in range(10)]
tableTriee = quickSort(table)

print("début: ",table)
print("\nfin: ",tableTriee)
