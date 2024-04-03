age = float(input(" Entrez votre âge: "))
print(" Vous avez " + str(age) + " ans. ")

if age >= 18: 
  print(" Vous êtes majeur. ")
elif age >= 13: 
  print(" Vous êtes adolescent. ")
else:
  print(" Vous êtes mineur. ")