import random,os.path

#Génération du fichier génétique aléatoire une seule fois
if not os.path.isfile("ADN.txt"):
  with open("ADN.txt","w") as fichier:
    for _ in range(10**6):
      fichier.write(random.choice(['A','T','C','G']))

#Récupération des données en mémoire
with open("ADN.txt","r") as fichier:
  adn = fichier.read()

#Recherche de la séquence
recherche = "ATTTACCC"
comparaisons = 0
occurrence = 0
for curseurFichier in range(len(adn) - len(recherche)+1):
  curseurMot=0
  for j in recherche:
    if j == adn[curseurFichier+curseurMot]:
      curseurMot+=1
    comparaisons+=1
    if curseurMot == len(recherche):
      comparaisons+=1
      occurrence+=1
      print(f"Occurrence #{occurrence} à la position {curseurFichier} après {comparaisons} comparaisons.")
      break
    comparaisons+=1