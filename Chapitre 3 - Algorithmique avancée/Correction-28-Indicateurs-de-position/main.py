nombre = int(input ("Combien de valeurs ? "))
liste = []
for i in range(nombre): 
  liste.append(int(input("Entrez une valeur : ")))

minimum = liste[0]
for valeur in liste:
  if valeur < minimum:
    minimum = valeur

maximum = liste[0]
for valeur in liste:
  if valeur > maximum:
    maximum = valeur

moyenne = 0
for i in liste:
  moyenne += i
moyenne = moyenne/len(liste)

print(liste)
print("Cette liste a un minimum de",minimum,"un maximum de",maximum,"et une moyenne de",moyenne)