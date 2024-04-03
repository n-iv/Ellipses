import random

n = random.randint(1, 100)
m = 0
essais = 0

while m != n:
  m = int(input("Votre essai ? "))
  if m > n:
    print("C'est moins !")
  elif m < n : 
    print("C'est plus !")
  essais += 1
print("Vous avez gagné au bout de " + str(essais) + " essais.")
