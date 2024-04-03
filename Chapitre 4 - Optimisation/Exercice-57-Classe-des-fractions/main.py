import math

class Frac():
  def __init__(self,num,denom=1):
    self.num = num
    self.denom = denom

  def __add__(self, other): #gère le +
    if type(other)!=Frac:#Si on ajoute un entier à une fraction
      other = Frac(other)#On le convertit en fraction
    nouveauNum = self.num*other.denom+other.num*self.denom #calcul du numérateur
    nouveauDenom = self.denom*other.denom #calcul du dénominateur
    simplification = math.gcd(nouveauNum,nouveauDenom) #plus grand commun diviseur
    nouveauNum = nouveauNum//simplification #simplification entière du numérateur
    nouveauDenom = nouveauDenom//simplification #simplification entière du dénominateur
    return Frac(nouveauNum,nouveauDenom) #on renvoie le résultat
  def __sub__(self, other): #gère le - (soustraction)
    pass #à compléter
  def __mul__(self, other): #gère le *
    pass #à compléter
  def __truediv__(self, other): #gère le /
    pass #à compléter
  def __lt__(self, other): #gère le <
    pass #à compléter
  def __le__(self, other): #gère le <=
    pass #à compléter
  def __eq__(self, other): #gère le ==
    pass #à compléter
  def __ne__(self, other): #gère le !=
    pass #à compléter
  def __gt__(self, other): #gère le >
    pass #à compléter
  def __ge__(self, other): #gère le >=
    pass #à compléter
  def __neg__(self): #gère le - (opposé)
    pass #à compléter
  def __str__(self): #gère le print() et le str()
    return str(self.num)+"/"+str(self.denom)

a = Frac(1,3)+Frac(1,6)
print(a)