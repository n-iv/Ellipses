clef="secret"
cpt=0

with open ("texteClair.txt","r") as fichier: 
  with open ("texteChiffre.txt","w",encoding="utf-8") as fichierChiffre:
    for ligne in fichier: 
      for car in ligne:
        fichierChiffre.write(chr(ord(car)+ord(clef[cpt%len(clef)])))
        cpt+=1

cpt=0

with open ("texteChiffre.txt","r") as fichierChiffre: 
  with open ("texteDeChiffre.txt","w",encoding="utf-8") as fichierDechiffre:
    for ligne in fichierChiffre: 
      for car in ligne:
        fichierDechiffre.write(chr(ord(car)-ord(clef[cpt%len(clef)])))
        cpt+=1
