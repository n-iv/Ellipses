compteur = 0

def affiche(n):
  global compteur
  compteur +=1
  print(f'On rentre dans la fonction pour la {compteur}{"ième" if compteur>1 else "ère"} fois.')
  if n>1:
    print(f"On n'affiche pas n qui vaut {n} mais on appelle affiche({n-1}).")
    affiche(n-1)
    print(f"On a fini d'appeler affiche({n-1}).")
  print(f"Ca y est, on peut l'afficher :")
  print(n)

affiche(5)