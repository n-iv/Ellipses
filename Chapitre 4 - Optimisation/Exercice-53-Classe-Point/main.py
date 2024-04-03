class Client():
  def __init__(self, prenom, nom, ville, cp, age, numeroClient):
    self.prenom = prenom                # On déclare les variables
    self.nom = nom                      # internes de la classe.
    self.ville = ville                   
    self.cp = cp                        
    self.age = age
    self.numeroClient = numeroClient

jpv = Client("Jean-Pierre", "Vernant", "Sèvres", 92310, 93, "JV123456") # On créé le client.
jpv.numeroClient = "JV654321" # On change le numéro client.
print(jpv.numeroClient) # On utilise le nouveau numéro client.

"""
Dans un jeu on a besoin de localiser les coordonnées des points sur l'écran en pixels. Les abscisses x et les ordonnées y des pixels ont des valeurs de type int.

Coder une classe Point contenant une abscisse x et une ordonnée y.
"""