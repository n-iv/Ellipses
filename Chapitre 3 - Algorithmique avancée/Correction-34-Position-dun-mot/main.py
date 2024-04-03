phrase=input("Entrer une phrase.\n").lower()
liste=phrase.split(" ")
if "jean" not in liste:
   print("Le mot 'jean' n'est pas présent dans la phrase.")
else:  
  rang=0
  curseur=0
  for i in liste:
    if i=="jean":
      rang=curseur
    curseur+=1
  print(f'Le mot "jean" est le {rang+1}{"ième" if rang>0 else "er"} mot de la phrase.')