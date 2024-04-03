phrase=input("Entrez une phrase à traduire.\n")

voyelles = "aeiou"
majuscules = [chr(i) for i in range(ord('A'),ord('A')+26)]

liste=phrase.split(" ")

pigLatin = ""

for mot in liste:
  if mot[0].lower() in voyelles and mot[0] in majuscules: # Voyelle majuscule au début du mot
    if mot[-1] in majuscules: # Mot finissant par une majuscule
      mot+='HAY'
    elif mot[-1].upper() in majuscules: # Mot finissant par une minuscule
      mot+='hay'
    else: # Mot finissant par un signe de ponctuation
      mot=mot[:-1]+'hay'+mot[-1]
      if mot[-5] in majuscules: # mot écrit en majuscules avec un signe de ponctuation à la fin
        mot = mot.upper()
  elif mot[0].lower() not in voyelles and mot[0] in majuscules:# Consonne majuscule au début au début du mot
    if mot[-1] in majuscules: # Mot finissant par une majuscule
      mot = mot[1:]+mot[0]+'AY' 
    elif mot[-1].upper() in majuscules: # Mot finissant par une minuscule
      mot = mot[1].upper()+mot[2:]+mot[0].lower()+'ay'
    elif mot[-2] in majuscules: # Mot finissant par une majuscule et signe de ponctuation
      mot=mot[1].upper()+mot[2:-1]+mot[0]+'AY'+mot[-1]
    else: # Mot finissant par une minuscule et un signe de ponctuation
      mot=mot[1].upper()+mot[2:-1]+mot[0].lower()+'ay'+mot[-1]
  elif mot[0].lower() in voyelles: # Voyelle minuscule au début
    if mot[-1].upper() in majuscules: # Mot finissant par une lettre
      mot+='hay'
    else: # Mot finissant par un signe de ponctuation
      mot=mot[:-1]+'hay'+mot[-1]
  else: # Consonne minuscule au début
    if mot[-1].upper() in majuscules: # Mot finissant par une lettre
      mot = mot[1]+mot[2:]+mot[0].lower()+'ay'
    else: # Mot finissant par un signe de ponctuation
      mot=mot[1:-1]+mot[0]+'ay'+mot[-1]
  pigLatin+=mot+' '

print(pigLatin)
