caractere = input("Entrez un caractère : ")

if 'A' <= caractere <= 'Z':
  print("C'est une majuscule.")
elif 'a' <= caractere <= 'z':
  print("C'est une minuscule.")
else:
  print("Ce n'est pas une simple lettre de l'alphabet.")