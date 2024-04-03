commandes={'read':'R','write':'W','execute':'X'}

#Chargement des droits
droits={}
doperations={}
with open("accessRights.txt","r") as ar: 
    for line in ar:
      ligne=line.strip().split(" ")
      droits[ligne[0]]="".join(ligne[1:])

#Vérification des opérations
with open("operations.txt","r") as op:
  for line in op:
    ligne=line.strip().split(" ")
    if ligne[0] not in commandes:
      print("This operation does not exist.")
    elif ligne[1] not in droits:
      print("This file does not exist.")
    elif commandes[ligne[0]] not in droits[ligne[1]]:
      print("Access denied.")
    else:
      print("OK.")