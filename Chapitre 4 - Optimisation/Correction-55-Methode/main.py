import math

class Point ():
  def __init__(self , abscisse , ordonnee):
    self.abscisse=abscisse
    self.ordonnee=ordonnee

  def distanceTo(self, b):
    return math.sqrt((self.abscisse-b.abscisse)**2 + (self.ordonnee-b.ordonnee)**2)

liste = [Point(3,1),Point(2,4),Point(2,5),Point(0,4),Point(-1,2)]
a = Point(1,3)

distMin = a.distanceTo(liste[0])
plusProche = liste[0]

for p in liste[1:]:
  if a.distanceTo(p) < distMin:
    distMin = a.distanceTo(p)
    plusProche = p

print("Le point le plus proche a pour coordonnées (",plusProche.abscisse, ";",plusProche.ordonnee,").")
