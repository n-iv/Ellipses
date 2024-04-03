commandes={'read':'R','write':'W','execute':'X'}

"""Commencer par charger les droits dans un dictionnaire contenant le nom de du fichier en clef, et les droits en valeur"""
with open("accessRights.txt","r") as ar: 
    pass # à compléter

"""Vérifier ensuite que les commandes sont autorisées. Écrire 'ok' ou 'access denied' selon le cas."""
with open("operations.txt","r") as op:
  for line in op:
    pass # à modifier.