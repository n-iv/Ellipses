import random

liste=[random.randint(1,100)for i in range(10)]
print(liste)

for k in range(len(liste)):
  for i,val in enumerate(liste[k:]):
    if val<liste[k]:
      liste[k],liste[i+k]=liste[i+k],liste[k]

print(liste)