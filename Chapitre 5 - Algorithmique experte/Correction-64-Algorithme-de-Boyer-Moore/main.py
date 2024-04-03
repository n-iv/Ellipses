motif = "ATTTACCC"
lm = len(motif)
comparaisons = 0
sauts = {chr(i):lm for i in range(256)} #On se prend toute la table ASCII.
i=1
for i in range(0,lm-1): 
  sauts[motif[i]] = lm-1-i
print(f'Distances : {sauts}')

with open("ADN.txt","r") as fichier:
  fich=""
  for line in fichier:
    for car in line:
      fich+=car
  lt=len(fich)
  res = [] #Liste des positions où l'on trouvera le motif dans le texte.
  decalage = 0 #Pointeur vers l'endroit où l'on est dans le texte.
  while(decalage <= lt-lm): 
    comparaisons+=1
    j = 0 #Pointeur vers la dernière lettre du motif (à 0 de la fin)
    while j<lm and motif[lm-1-j] == fich[decalage+lm-1-j]: 
      comparaisons+=2
      j += 1
    if j==lm: 
      comparaisons+=1
      res.append(decalage) 
      if decalage+lm-1<lt:
        comparaisons+=1
        decalage += max(1, sauts[fich[decalage+lm-1]]) 
    else: 
      decalage += max(1, sauts[fich[decalage+lm-1-j]]-j) 
  print("Le début du motif se trouve à la (aux) position(s) :",res)

print("Cela a nécessité",comparaisons,"comparaisons.")