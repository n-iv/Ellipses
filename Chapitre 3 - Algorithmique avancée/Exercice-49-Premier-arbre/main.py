def createTree(valeur):
  return [valeur,None,None]

def appendLeftTree(tree,leftTree):
  return [tree[0],leftTree,tree[2]]

def appendRightTree(tree,rightTree):
  return [tree[0],tree[1],rightTree]

cinq=createTree(5)
onze=createTree(11)
six=createTree(6)

six = appendLeftTree(six,cinq)
six = appendRightTree(six,onze)

print(six)