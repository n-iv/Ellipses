def nbPieces(somme,valeurs):
  if somme==0:
    return 0
  mini = 10**6
  for v in valeurs:
    if v<=somme:
      nb = 1+nbPieces(somme-v,valeurs)
      if nb < mini:
        mini = nb
  return mini

aRendre = 11
pieces = [2,5,10,50,100]

print(f'Il faudra {nbPieces(aRendre,pieces)} pièces pour rendre {aRendre} centimes.')