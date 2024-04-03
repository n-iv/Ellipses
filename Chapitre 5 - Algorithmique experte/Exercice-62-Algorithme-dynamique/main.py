def nbPieces(somme,valeurs,mem):
  if somme==0:
    return 0
  if mem[somme]>0:
    return mem[somme]
  mini = 10**6
  for v in valeurs:
    if v<=somme:
      nb = 1+nbPieces(somme-v,valeurs,mem)
      if nb < mini:
        mini = nb
        mem[somme] = nb
  return mini

aRendre = 11
pieces = [2,5,10,50,100]
memoire = [0]*(aRendre+1)

print(f'Il faudra {nbPieces(aRendre,pieces,memoire)} pièces pour rendre {aRendre} centimes.')