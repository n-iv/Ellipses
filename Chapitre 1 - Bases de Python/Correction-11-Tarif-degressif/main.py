montant_brut = float(input(" Quel est votre montant brut ? "))
if montant_brut >= 2000 and montant_brut <= 5000:
  print("Votre montant net à payer s'élève à " +str(0.99 * montant_brut) + " euros.")
elif montant_brut > 5000:
  print(f" Votre montant net à payer s'élève à {.98 * montant_brut} euros.")