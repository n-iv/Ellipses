mot = input("Entrez un mot.\n")

voy = "aeiou"

nbVoyelles=0
nbConsonnes=0

for lettre in mot:
  if lettre in voy:
    nbVoyelles+=1
  else:
    nbConsonnes+=1

print("il y a",nbVoyelles,"voyelles et",nbConsonnes,"consonnes dans le mot.")
