class Compte():
  nbCompte=0
  argentBanque=0
  def __init__(self , nom , prenom, solde=0):
    self.nom=nom
    self.prenom=prenom
    self.solde=solde
    Compte.nbCompte+=1
    Compte.argentBanque+=solde
  def depot(self,somme):
    self.solde+=somme
    Compte.argentBanque+=somme
  def retrait(self,difference):
    self.solde-=difference
    Compte.argentBanque-=difference

compte1=Compte("Martin","Paul",1000) #1 compte, argent total : 1000
compte1.retrait(100) #argent total : 900

compte2=Compte("Martin","Paul",10000) #2 comptes, argent total : 10900
compte2.depot(5000) #argent total : 15900

print(compte1.nbCompte, Compte.argentBanque)
print(Compte.nbCompte, compte2.argentBanque)