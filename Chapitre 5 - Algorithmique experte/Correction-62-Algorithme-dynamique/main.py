def nbPieces(somme,valeurs):
  if somme==0: #Pour rendre 0,
    return 0   #Il faut 0 pièce.
  if mem[somme]>0: #Si on a déjà calculé cette somme,
    return mem[somme] #On renvoie le résultat déjà calculé.
  mini = 10**6 #On initialise le mini à une grande valeur.
  for v in valeurs: #Pour chaque valeur de pièce possible,
    print(mem) #On affiche le tableau "mémoire".
    if v<=somme:#Si la valeur de la pièce est inférieure ou égale à la somme à rendre,
      nb = 1+nbPieces(somme-v,valeurs)#On calcule le nombre de pièces possibles en enlevant cette valeur du total à rendre,
      if nb < mini:#Si le nombre de pièces est inférieur au mini déjà trouvé,
        mini = nb #On met à jour le mini.
        mem[somme] = nb #On met à jour le tableau "mémoire".
  return mini #On renvoie le mini.

aRendre = 11
pieces = [2,5,10,50,100]
mem = [0]*(aRendre+1) #On va mémoriser le minimum de pièces à rendre pour chaque somme entre 0 et la valeur à rendre.

print(f'Il faudra {nbPieces(aRendre,pieces)} pièces pour rendre {aRendre} centimes.')