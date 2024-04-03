# Question 1)
def freq(phrase,lettre):
  compt=0
  for caractere in phrase.lower():
    if caractere==lettre:
      compt+=1
  return (compt/len(phrase))

# Question 2)
def alphabet():
  return [chr(i+97)for i in range(26)]

# Question 3)
# Le fichier a été nommé "turing.txt"

# Question 4)
with open("turing.txt","r",encoding="utf-8") as texte:
  frequences={}
  page=""
  for ligne in texte:
    page+=ligne+"\n"
for lettre in alphabet():
  frequences[lettre] = freq(page,lettre)

# Question 5)
for lettre in frequences:
  print(lettre,":",int(frequences[lettre]*10000)/100)