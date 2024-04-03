from random import randint

def merge(gauche, droite):
    result = []
    indiceGauche, indiceDroite = 0, 0
    while indiceGauche < len(gauche) and indiceDroite < len(droite):
        if gauche[indiceGauche] <= droite[indiceDroite]:
            result.append(gauche[indiceGauche])
            indiceGauche += 1
        else:
            result.append(droite[indiceDroite])
            indiceDroite += 1
    if indiceGauche < len(gauche):
        result+=gauche[indiceGauche:]
    if indiceDroite < len(droite):
        result+=droite[indiceDroite:]
    return result

def mergeSort(t): 
  if len(t) <= 1: 
    return t 
  milieu = len(t) // 2
  gauche, droite = t[:milieu], t[milieu:]
  gauche , droite = mergeSort(gauche), mergeSort(droite)
  return merge(gauche, droite)

table = [randint(1,100) for i in range(10)]
tableTriee = mergeSort(table)

print(f"début: {table}")
print(f"\nfin: {tableTriee}")