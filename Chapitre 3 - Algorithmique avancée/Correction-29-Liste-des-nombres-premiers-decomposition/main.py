n = int(input("Entrez un nombre supérieur à 2: "))

liste = [] #liste des nombres premiers déjà trouvés

for test in range(2,n+1): #On teste chaque nombre pour vérifier s'il est premier, et on va bien jusqu'à n cette fois-ci
  premier = True #On suppose qu'il l'est

  for diviseur in liste: #On va essayer de diviser notre nombre test par tous les nombres premiers déjà trouvés
    if test % diviseur == 0: #Si la division s'effectue
      premier = False #Ce n'était pas un nombre premier
      break #On s'arrête (ligne facultative)

  if premier: #à la fin, si on n'a trouvé aucun diviseur
    liste.append(test) #C'est qu'on a trouvé un nouveau nombre premier !

facteurs = [] #liste des nombres premiers dans n
ordres = [] #liste des puissances des nombres premiers dans la décomposition en facteurs premiers
for p in liste: #Pour chaque nombre premier inférieur à n
  if n % p == 0:#S'il est dans la décomposition de n
    a=2 #On essaye de voir s'il rentre deux fois
    while n%p**a == 0: #Si oui, on va essayer encore plus
      a+=1 #Une fois de plus
    facteurs.append(p) #On mémorise le facteur trouvé
    ordres.append(a-1) #Avec la bonne puissance, la dernière essayée n'ayant pas marché...

decomp = str(n)+" = " #On affiche le nombre égal

for i in range(len(facteurs)): #Pour chaque facteur
  decomp+=str(facteurs[i]) #On ajoute le facteur
  if ordres[i]>1: #Si la puissance est plus grande que 1, 
    decomp+="^"+str(ordres[i]) #On affiche la puissance aussi
  decomp+="x" #Et on termine par un multiplié, pour le facteur d'après

print(decomp[:-1]) #On affiche le résultat, sauf le dernier caractère (signe multiplié excédentaire).
