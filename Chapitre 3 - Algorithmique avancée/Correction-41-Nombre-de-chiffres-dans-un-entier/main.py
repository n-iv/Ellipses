def nbChiffres(n):
  if n//10 == 0:
    return 1
  return nbChiffres(n//10) + 1

print(nbChiffres(3**1000))