class Tree():
  taille = 0
  def __init__(self, data, left=None, right=None):
      self.data = data
      self.left = left
      self.right = right
      Tree.taille+=1

  def profondeur(self):
    if self.left != None and self.right!= None:
     return  1+max(self.left.profondeur(),self.right.profondeur())
    elif self.left != None:
        return 1+ self.left.profondeur()
    elif self.right != None:
        return 1+ self.right.profondeur()
    return 1

  def size(self):
    return Tree.taille

  def arbreGauche(self):
    if self.left != None:
      return self.left

  def arbreDroite(self):
    if self.right != None:
      return self.right

  def parcoursPrefixe(self):
    return str(self.data)+" "+(self.left.parcoursPrefixe() if self.left!=None else "")+" "+(self.right.parcoursPrefixe() if self.right!=None else "")

  def parcoursInfixe(self):
    return (self.left.parcoursInfixe() if self.left!=None else "")+" "+str(self.data)+" "+(self.right.parcoursInfixe() if self.right!=None else "")

  def parcoursSuffixe(self):
    return (self.left.parcoursSuffixe() if self.left!=None else "")+" "+(self.right.parcoursSuffixe() if self.right!=None else "")+str(self.data)+" "

  def affEtage(self,n,ch=""):
    if n==1:
      ch+=str(self.data)
      return ch
    else:
      if self.left!=None and self.right!=None:
        return ch+self.left.affEtage(n-1,ch)+" "+self.right.affEtage(n-1,ch)+" "
      if self.left!=None:
        return ch+self.left.affEtage(n-1,ch)+" "
      if self.right!=None:
        return ch+self.right.affEtage(n-1,ch)+" "
      return ch+" "

  def parcoursLargeur(self):
    for i in range(1,self.size()):
      print(self.affEtage(i))

  def pos_valeur (self):
    pass

  def __str__(self):
    affichage=f"""
"""
    for i in range(1,self.size()):
      affichage+=' '*(self.size()-i)
      affichage+=self.affEtage(i)
      affichage+="\n"
    return affichage

  def trouver(self, valeur):
    for i in range(1,self.size()):
      if str(valeur) in self.affEtage(i):
        place = 1
        for ch in self.affEtage(i):
          if ch==str(valeur):
            print(valeur,"trouvé à l'étage",i,"position",place)
          elif ch!=" ":
            place+=1

  def minimum(self):
    return min(self.data,self.left.minimum() if self.left!=None else self.data,self.right.minimum() if self.right!=None else self.data)

  def maximum(self):
    return max(self.data,self.left.maximum() if self.left!=None else self.data,self.right.maximum() if self.right!=None else self.data)

arbre = Tree(2,Tree(7,Tree(2),Tree(6,Tree(5),Tree(11))),Tree(5,None,Tree(9,Tree(4))))

print(arbre)
print ("profondeur :",arbre.profondeur())
print("nombre de noeuds :",arbre.size())
print("Sous-arbre de gauche :",arbre.arbreGauche())
print("Sous-arbre de droite du précédent :",arbre.arbreGauche().arbreDroite())
arbre.parcoursLargeur()
print(arbre.parcoursPrefixe())
print(arbre.parcoursInfixe())
print(arbre.parcoursSuffixe())
print(arbre.trouver(6))
print(arbre.minimum())
print(arbre.maximum())