import math

class Point ():
  def __init__(self , abscisse , ordonnee):
    self.abscisse=abscisse
    self.ordonnee=ordonnee

def distance(abs1, ord1, abs2, ord2):
  return math.sqrt((abs2-abs1)**2 + (ord2-ord1)**2)

liste = [Point(3,1),Point(2,4),Point(2,5),Point(0,4),Point(-1,2)]
a = Point(1,3)

distMin = distance(liste[0].abscisse,liste[0].ordonnee,a.abscisse,a.ordonnee)
plusProche = liste[0]

for p in liste[1:]:
  if distance(p.abscisse,p.ordonnee,a.abscisse,a.ordonnee) < distMin:
    distMin = distance(p.abscisse,p.ordonnee,a.abscisse,a.ordonnee)
    plusProche = p

print("Le point le plus proche a pour coordonnées (",plusProche.abscisse, ";",plusProche.ordonnee,").")