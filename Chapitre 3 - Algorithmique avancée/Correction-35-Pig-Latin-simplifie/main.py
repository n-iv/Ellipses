phrase=input("Entrez une phrase à traduire.\n")

voyelles = "aeiouy"

liste=phrase.split(" ")

pigLatin = ""

for mot in liste:
  if mot[0] in voyelles:
    mot+='h'
  else:
    mot = mot[1:]+mot[0]
  mot+='ay'
  pigLatin +=mot+' '

print(pigLatin)