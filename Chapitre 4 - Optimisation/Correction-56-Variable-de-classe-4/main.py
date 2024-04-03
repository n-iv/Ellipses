class Compte():
  def __init__(self , nom , prenom, solde=0):
    self.nom=nom
    self.prenom=prenom
    self.solde=solde
  def depot(self,somme):
    self.solde+=somme
  def retrait(self,difference):
    self.solde-=difference

compte1=Compte("Martin","Paul",1000)
compte1.retrait(100)
print(compte1.solde)   