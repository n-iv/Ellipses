class Compte():
  nbCompte=0
  nbTotaleA=0
  def __init__(self , nom , prenom, solde=0):
    self.nom=nom
    self.prenom=prenom
    self.solde=solde
  def depot(self,somme):
    self.solde+=somme

compte1=Compte("Martin","Paul",1000)
compte1.depot(100)
print(compte1.solde)