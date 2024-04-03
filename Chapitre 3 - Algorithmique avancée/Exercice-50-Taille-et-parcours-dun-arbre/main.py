def parcoursGauche(t):
  if t!=None:
    print(t[0])
    parcoursGauche(t[1])
    parcoursGauche(t[2])

def size(t):
  pass #fonction récursive permettant le calcul du nombre de noeuds de l'arbre
  return None


tree = [2,[7,[2,None,None],[6,[5,None,None],[11,None,None]]],[5,None,[9,[4,None,None],None]]]

parcoursGauche(tree)

print("nombre de noeuds : ",size(tree))