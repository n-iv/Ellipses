def affiche(n):
  if n>1:
    affiche(n-1)
  print(n)

affiche(5)