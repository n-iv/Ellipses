# Question 6)
def freq(phrase,lettre):
  compt=0
  for caractere in phrase.lower():
    if caractere==lettre:
      compt+=1
  return (compt/len(phrase))

def alphabet():
  return [chr(i+97)for i in range(26)]

fichiers = ["turing.txt","1792.txt","python.txt","plante.txt","turingEN.txt","snowboardEN.txt","turingES.txt"]

frequences={lettre:"" for lettre in alphabet()}

for i in range(len(fichiers)):
  with open(fichiers[i],"r",encoding="utf-8") as texte:
    page=""
    for ligne in texte:
      page+=ligne+"\n"
  for lettre in alphabet():
    frequences[lettre] += str(int(freq(page,lettre)*10000)/100)+' / '

for lettre in frequences:
  print(lettre,":",frequences[lettre])