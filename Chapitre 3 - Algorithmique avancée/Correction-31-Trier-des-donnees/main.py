import random

liste=[random.randint(1,100)for i in range(10)]
print(liste)
listeOrdonnee = []

for _ in range(len(liste)):
  minimum=liste[0]
  for valeur in liste:
    if valeur<minimum:
      minimum=valeur
  listeOrdonnee.append(minimum)
  liste.remove(minimum)

print(listeOrdonnee)
