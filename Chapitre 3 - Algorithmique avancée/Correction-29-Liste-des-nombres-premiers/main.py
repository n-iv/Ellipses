n = int(input("Entrez un nombre supérieur à 2: "))

liste = [] #liste des nombres premiers déjà trouvés

for test in range(2,n): #On teste chaque nombre pour vérifier s'il est premier
  premier = True #On suppose qu'il l'est

  for diviseur in liste: #On va essayer de diviser notre nombre test par tous les nombres premiers déjà trouvés
    if test % diviseur == 0: #Si la division s'effectue
      premier = False #Ce n'était pas un nombre premier
      break #On s'arrête (ligne facultative)

  if premier: #à la fin, si on n'a trouvé aucun diviseur
    liste.append(test) #C'est qu'on a trouvé un nouveau nombre premier !

print(liste)
