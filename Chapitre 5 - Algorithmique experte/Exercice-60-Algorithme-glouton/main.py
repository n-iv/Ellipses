def nbPieces(somme,valeurs):
  if somme==0:
    return 0
  for v in valeurs[::-1]:
    if v<=somme:
      print(f'On utilise une pièce de {v}.')
      return 1+nbPieces(somme-v,valeurs)

aRendre = 177
pieces = [2,5,10,50,100]

print(f'Il faudra {nbPieces(aRendre,pieces)} pièces pour rendre {aRendre} centimes.')