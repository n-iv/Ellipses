import random

global N #déclare une variable commune à TOUTES les fonctions !
N=0 #comptage des opérations de l'algorithme naif
global Q
Q=0 #comptage des opérations de l'algorithme rapide
global M
M=0 #comptage des opérations de l'algorithme fusion

def chercheMin(t):#Oui, il est aussi possible d'appeler la fonction min()
  global N
  minimum=t[0]
  indice=0
  N+=2 #deux affectations aux lignes précédentes
  for k,valeur in enumerate(t):
    N+=1 #comparaison à la ligne suivante
    if valeur<minimum:
      minimum=valeur
      indice=k
      N+=2 #deux modifications aux lignes précédentes
  return indice

def triNaif(t): # algorithme de tri récursif sur une liste
  global N
  N+=1 #une comparaison à la ligne suivante
  if len(t) == 1: # si la liste contient un seul élément
    return [t[0]]
  else: # sinon
    indiceMin=chercheMin(t)
    N+=1 #une affectation à la ligne précédente / sans elle, il faudrait appeler chercheMin(t) 3 fois à la ligne suivante, ce qui serait pire !
    return [t[indiceMin]]+triNaif(t[:indiceMin]+t[indiceMin+1:])

def quickSort(t): # algorithme de tri récursif sur une liste
  global Q
  Q+=1 #une comparaison à la ligne suivante
  if len(t) <= 1: # si la liste contient un ou zéro élément
    return t # elle est déjà triée...
  pivot = t[0] # on choisit le premier élément
  gauche = [] # on va mettre tous les plus petits dans une liste
  droite = [] # et tous les plus grands dans une autre
  Q+=3 #trois affectations aux lignes précédentes
  for i in range(1,len(t)): # parmi tous les éléments du tableau, sauf le premier
    Q+=1 #une comparaison à la ligne suivante
    if t[i]<pivot: # si l'élément est plus petit
      gauche.append(t[i]) # il va à gauche
      Q+=1 #une affectation à la ligne précédente
    else: # sinon
      droite.append(t[i]) # il va à droite
      Q+=1 #une affectation à la ligne précédente
  return quickSort(gauche)+[pivot]+quickSort(droite) #on va relancer ça sur les "demies-listes", forcément plus petites, et rassembler les résultats

def merge(gauche, droite):#fusion ordonnée de tableaux
    global M
    result = []
    indiceGauche, indiceDroite = 0, 0 #on compare les tableaux à fusionner à partir de la gauche, car ils sont triés
    M+=3 #trois affectations aux lignes précédentes
    M+=1.5 #une à deux comparaisons aux lignes suivantes : on rappelle que and n'évalue pas la seconde condition si la première est fausse
    while indiceGauche < len(gauche) and indiceDroite < len(droite): #tant qu'on n'a pas épuisé l'un des tableaux
        M+=1 #une comparaison à la ligne suivante
        if gauche[indiceGauche] <= droite[indiceDroite]:#si l'élément à gauche est plus petit que celui de droite, on l'ajoute à notre tableau
            result.append(gauche[indiceGauche])
            indiceGauche += 1
        else:
            result.append(droite[indiceDroite])#sinon, on ajoute celui de droite
            indiceDroite += 1
        M+=2 #deux opérations au dessus, quel que soit le résultat.

    #Add any remaining elements in the gauche or droite lists. 
    if indiceGauche < len(gauche):#quand on a épuisé le tableau de droite, on rajoute tout le tableau de gauche
        result+=gauche[indiceGauche:]
        M+=len(gauche[indiceGauche:]) #affectations supplémentaires
    if indiceDroite < len(droite):#quand on a épuisé le tableau de gauche, on rajoute tout le tableau de droite 
        result+=droite[indiceDroite:]
        M+=len(gauche[indiceDroite:]) #affectations supplémentaires
    return result

def mergeSort(t): # algorithme de coupe naive d'un tableau en deux
  global M
  M+=1 #une affectation à la ligne suivante
  if len(t) <= 1: # si la liste contient un ou zéro élément
    return t # elle est déjà assez petite...
  M+=5 #cinq affectations aux lignes suivantes
  milieu = len(t) // 2
  gauche = t[:milieu] #on prend la partie avant le milieu (strictement avant)
  droite = t[milieu:] #on prend la partie après le milieu (largement, i.e. dont le milieu)
  gauche = mergeSort(gauche) #on casse la partie de gauche
  droite = mergeSort(droite) #on casse la partie de droite
  return list(merge(gauche, droite)) #et on fusionne les résultats.

etalementValeurs=[10,100,1000]

for etalement in etalementValeurs:
  print(f'Avec des valeurs entre 0 et {etalement},')
  table=[random.randint(1,etalement) for i in range(900)] #On peut modifier ces valeurs, mais si le range devient trop grand, repl.it est limité.

  tableNaive = triNaif(table)
  tableRapide = quickSort(table)
  tableFusion = mergeSort(table)

  print(f'La table naive est créée avec {N} opérations.')
  print(f'La table quick est créée avec {Q} opérations.')
  print(f'La table merge est créée avec {int(M)} opérations.')
  print('\n')