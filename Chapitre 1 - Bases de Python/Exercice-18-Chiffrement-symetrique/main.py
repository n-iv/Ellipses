"""
On souhaite ouvrir un fichier, et le chiffrer/déchiffrer à l’aide d’une clef de chiffrage. L’idée est, à l’instar du programme précédent, d’ajouter une quantité à chaque caractère. On choisira d’ajouter le code ASCII des lettres du mot "secret" dans cet ordre.

Ainsi, le premier caractère sera augmenté de 115, le second de 101, etc.

La procédure pour ouvrir un fichier en lecture et un en écriture est la suivante :
"""

with open("texteClair.txt", "r") as fichier: #ouvre "texteClair.txt" en lecture
  with open("texteChiffre.txt", "w") as fichierChiffre: #créé ou efface et recréé "texteChiffre.txt" et l'ouvre en écriture
    for ligne in fichier: #on balaye les lignes les unes après les autres
      for car in ligne: #on parcourt tous les caractères
        pass #à remplacer par le code nécessaire