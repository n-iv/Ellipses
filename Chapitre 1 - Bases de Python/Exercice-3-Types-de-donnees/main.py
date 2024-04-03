print("L'ordinateur va maintenant vous demander votre âge et l'âge de l'un de vos parents \n")
ageEnfant = input("Quel est votre âge ? ")
ageParent = input("Quel est l'âge de l'un de vos parents ? ")
print("Vous avez "+ageEnfant+" ans.")
print("L'un de vos parents a "+ageParent+" ans.")

#calcul de la différence d age 
differenceAge = int(ageParent) - int(ageEnfant)
print("Votre différence d'âge s'élève à "+str(differenceAge)+" ans.")