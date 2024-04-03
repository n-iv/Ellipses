import random

#Mieux vaut commencer par lire la seconde fonction, qui casse le tableau en deux à chaque étape. On reviendra ensuite à celle-ci qui fusionne les tableaux en les ordonnant.
def merge(gauche, droite):#fusion ordonnée de tableaux
    result = []
    indiceGauche, indiceDroite = 0, 0 #on compare les tableaux à fusionner à partir de la gauche, car ils sont triés
    while indiceGauche < len(gauche) and indiceDroite < len(droite): #tant qu'on n'a pas épuisé l'un des tableaux
        if gauche[indiceGauche] <= droite[indiceDroite]:#si l'élément à gauche est plus petit que celui de droite, on l'ajoute à notre tableau
            result.append(gauche[indiceGauche])
            indiceGauche += 1
        else:
            result.append(droite[indiceDroite])#sinon, on ajoute celui de droite
            indiceDroite += 1
    #Add any remaining elements in the gauche or droite lists. 
    if indiceGauche < len(gauche):#quand on a épuisé le tableau de droite, on rajoute tout le tableau de gauche
        result+=gauche[indiceGauche:]
    if indiceDroite < len(droite):#quand on a épuisé le tableau de gauche, on rajoute tout le tableau de droite
        result+=droite[indiceDroite:]
    return result

def mergeSort(t): # algorithme naif de coupe d'un tableau en deux
  if len(t) <= 1: # si la liste contient un ou zéro élément
    return t # elle est déjà assez petite...
  milieu = len(t) // 2
  gauche = t[:milieu] #on prend la partie avant le milieu (strictement avant)
  droite = t[milieu:] #on prend la partie après le milieu (largement, i.e. dont le milieu)
  #casser la partie de gauche ici
  #casser la partie de droite ici
  #renvoyer la fusion des résultats.

table=[random.randint(1,100) for i in range(10)]
print("début : ",table)

tableTriee = mergeSort(table)
print("\n fin : ",tableTriee)