def pgcd(a,b):
  if a>b:
    a, b = b, a
  if a == 0:
    return b
  return pgcd(a, b-a)
  
print(pgcd(19929,31577)) # Doit renvoyer 91