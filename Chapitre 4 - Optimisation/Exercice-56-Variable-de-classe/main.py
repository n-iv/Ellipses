"""
1) Créer une classe Compte qui contient un nom, un prénom, et un solde. Peut-on initialiser un compte sans solde ?
2) Ajouter =0 à côté de solde dans __init__. Que se passe-t-il lorsqu’on initialise la classe avec ousans solde ?
3) On ajoute une méthode pour déposer de l’argent :
"""
def depot(self,somme):
  self.solde+=somme
"""
Initialiser le compte à 1000€ et y ajouter 100€ en appelant la méthode dépot.
4) Créer une méthode retrait pour retirer de l’argent du compte, et la tester.
5) Ajouter une variable de classe comptant le nombre de comptes.
6) Ajouter une variable de classe comptant l’argent total sur les comptes, et vérifier qu’elle fonctionneavec les méthodes retrait et depot.
"""