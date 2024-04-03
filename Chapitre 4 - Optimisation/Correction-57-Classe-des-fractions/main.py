import math

class Frac():
  def __init__(self,num,denom=1):
    self.num = num
    self.denom = denom
  def __add__(self, other):
    if type(other)!=Frac:
      other = Frac(other)
    nouveauNum = self.num*other.denom+other.num*self.denom 
    nouveauDenom = self.denom*other.denom 
    simplification = math.gcd(nouveauNum,nouveauDenom) 
    nouveauNum = nouveauNum//simplification 
    nouveauDenom = nouveauDenom//simplification 
    return Frac(nouveauNum,nouveauDenom) 
  def __sub__(self, other): 
    if type(other)!=Frac:
      other = Frac(other)
    nouveauNum = self.num*other.denom-other.num*self.denom 
    nouveauDenom = self.denom*other.denom 
    simplification = math.gcd(nouveauNum,nouveauDenom) 
    nouveauNum = nouveauNum//simplification 
    nouveauDenom = nouveauDenom//simplification 
    return Frac(nouveauNum,nouveauDenom) 
  def __mul__(self, other): 
    if type(other)!=Frac:
      other = Frac(other)
    nouveauNum = self.num*other.num 
    nouveauDenom = self.denom*other.denom 
    simplification = math.gcd(nouveauNum,nouveauDenom) 
    nouveauNum = nouveauNum//simplification 
    nouveauDenom = nouveauDenom//simplification 
    return Frac(nouveauNum,nouveauDenom) 
  def __truediv__(self, other): 
    if type(other)!=Frac:
      other = Frac(other)
    nouveauNum = self.num*other.denom 
    nouveauDenom = self.denom*other.num
    simplification = math.gcd(nouveauNum,nouveauDenom) 
    nouveauNum = nouveauNum//simplification 
    nouveauDenom = nouveauDenom//simplification 
    return Frac(nouveauNum,nouveauDenom) 
  def __lt__(self, other): 
    if type(other)!=Frac:
      other = Frac(other)
    return self.num*other.denom<other.num*self.denom
  def __le__(self, other): 
    if type(other)!=Frac:
      other = Frac(other)
    return self.num*other.denom<=other.num*self.denom
  def __eq__(self, other): 
    if type(other)!=Frac:
      other = Frac(other)
    return self.num*other.denom==other.num*self.denom
  def __ne__(self, other): 
    if type(other)!=Frac:
      other = Frac(other)
    return self.num*other.denom!=other.num*self.denom
  def __gt__(self, other): 
    if type(other)!=Frac:
      other = Frac(other)
    return not self<=other
  def __ge__(self, other): 
    if type(other)!=Frac:
      other = Frac(other)
    return not self<other
  def __neg__(self): 
    return Frac(-self.num, self.denom)     
  def __str__(self): 
    return str(self.num)+"/"+str(self.denom)

print(Frac(3,4) >= -Frac(1,3))
print(Frac(3,4) < -Frac(1,3))
print(Frac(3,4) > -Frac(1,3))
print(Frac(3,4) < -Frac(1,3))
print(Frac(1,2)+Frac(1,4) == -Frac(-5,8)-Frac(-1,8))
print(Frac(3,2)*Frac(1,2) != Frac(3,8)/Frac(1,2))
print(Frac(1,2)-Frac(1,3)*2+1)