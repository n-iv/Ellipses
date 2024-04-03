recherche = "ACCTTCG"
texte = "CAATGTCGCTGGTTCGACCTTCGAAGACGCCGGCAGGTGCAGACCTTCGTTATAGGCGAT"

#La première fonction sert juste à afficher ce que le programme fait petit à petit. Elle est un peu technique, il vaut mieux la sauter et faire confiance en première lecture.
def affichage(d,k,s):
  lm=len(recherche)
  lt=len(texte)
  aff=''
  for i in range(d):
    aff+=texte[i]
  if k!=lm:
    for i in range(lm-1-k):
      aff+=texte[d+i]
    aff+='\033[31m'+texte[d+lm-1-k]+'\033[0m'
  for i in range(lm-k,lm):
    aff+='\033[32m'+texte[d+i]+'\033[0m'  
  for i in range(d+lm,lt):
    aff+=texte[i]
  aff+='\n'+' '*d
  if k!=lm:
    for i in range(lm-1-k):
      aff+=recherche[i]
    aff+='\033[31m'+recherche[lm-1-k]+'\033[0m'
  for i in range(lm-k,lm):
    aff+='\033[32m'+recherche[i]+'\033[0m'
  if k!=lm:
    aff+='\nDifférence en position '+str(k)+', saut pour aligner le '+texte[d+lm-1-k]+' suivant : '+str(s[texte[d+lm-1-k]])+'. Donc on décale de '+str(s[texte[d+lm-1-k]]-k)+'.\n'
  else:
    aff+='\nBingo ! Saut pour aligner le '+texte[d+lm-1]+' suivant : '+str(s[texte[d+lm-1]])+'. Donc on décale de '+str(s[texte[d+lm-1]])+'.\n'
  print(aff)

def bm(txt, motif):
  lm = len(motif)
  lt = len(txt)

  #Pré-traitement : on calcule la distance minimale entre chaque caractère et la fin du motif recherché.
  sauts = {'A':lm,'T':lm,'C':lm,'G':lm}
  i=1
  for i in range(0,lm-1): 
    sauts[motif[i]] = lm-1-i
  print(f'Distances : {sauts}')

  #Traitement : 
  res = [] #Liste des positions où l'on trouvera le motif dans le texte.
  decalage = 0 #Pointeur vers l'endroit où l'on est dans le texte.
  while(decalage <= lt-lm): #On ne cherche pas le motif s'il n'y a plus assez de caractères dans le texte pour le contenir.
    j = 0 #Pointeur vers la dernière lettre du motif (à 0 de la fin)
    while j<lm and motif[lm-1-j] == txt[decalage+lm-1-j]: #Tant qu'on peut aller vers la droite parce que les caractères sont égaux, on continue.
      j += 1
    #Les deux lignes suivantes servent seulement à afficher correctement les chaînes comparées, les ignorer en première lecture.
    affichage(decalage,j,sauts)
    #aff=texte+'\n'+' '*decalage+recherche+' j='+str(j)+' saut='+str(sauts[txt[decalage+lm-1-j]])+' '+motif[lm-1-j]+"!="+txt[decalage+lm-1-j]+'\n'
    #print(aff)
    if j>=lm: #Si le motif est trouvé
      res.append(decalage) #On mémorise sa position
      if decalage+lm-1<lt:
        decalage += max(1, sauts[txt[decalage+lm-1]]) #Et on continue
    else: #Sinon
      decalage += max(1, sauts[txt[decalage+lm-1-j]]-j) #On met la lettre qu'on aurait dû avoir là où la correspondance n'allait plus dans le texte.
  return res

print("Le début du motif se trouve à la (aux) position(s) :",bm(texte,recherche))