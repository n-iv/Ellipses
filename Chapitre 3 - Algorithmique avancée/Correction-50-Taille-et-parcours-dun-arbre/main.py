def parcoursGauche(t):
  if t!=None:
    print(t[0])
    parcoursGauche(t[1])
    parcoursGauche(t[2])

def size(t):
  if t!=None:
    if t[1] != None and t[2]!= None:
      return 1+ size(t[1])+size(t[2])
    elif t[1] != None:
      return 1+ size(t[1])
    elif t[2] != None:
      return 1+ size(t[2])
    return 1
  return 0

tree = [2,[7,[2,None,None],[6,[5,None,None],[11,None,None]]],[5,None,[9,[4,None,None],None]]]

print("Parcours à gauche :")
parcoursGauche(tree)

print("\nNombre de noeuds : ",size(tree))