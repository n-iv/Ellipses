def createTree(valeur):
  return [valeur,None,None]

def appendLeftTree(tree,leftTree):
  return [tree[0],leftTree,tree[2]]

def appendRightTree(tree,rightTree):
  return [tree[0],tree[1],rightTree]

cinq=createTree(5)
onze=createTree(11)
six=createTree(6)
sept=createTree(7)
deuxg=createTree(2)
deux=createTree(2)
cinqd=createTree(5)
neuf=createTree(9)
quatre=createTree(4)


six = appendLeftTree(six,cinq)
six = appendRightTree(six,onze)
sept = appendLeftTree(sept,deuxg)
sept = appendRightTree(sept,six)
neuf = appendLeftTree(neuf,quatre)
cinqd = appendRightTree(cinqd,neuf)
deux = appendLeftTree(deux,sept)
deux = appendRightTree(deux,cinqd)

print(deux)