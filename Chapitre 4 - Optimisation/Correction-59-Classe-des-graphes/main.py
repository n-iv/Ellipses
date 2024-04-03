class Graph():
  def __init__(self,matrice,noms=[]):
    if noms!=[]:
      self.noms=noms
    else:
      self.noms=[chr(ord('a')+i) for i in range(len(matrice))]
    self.matrice = matrice
    self.noeuds=len(matrice)

  def __str__(self):
    affichage = "  "
    for ch in self.noms:
      affichage+=str(ch)+' '
    affichage+='\n'
    for i,ligne in enumerate(self.matrice):
      affichage+=self.noms[i]+' '
      for ch in ligne:
        affichage+=str(ch)+' '
      affichage+='\n'
    return affichage

  def ajoutNoeud(self,nom):
    self.noms.append(nom)
    for i in range(self.noeuds):
      self.matrice[i].append(0)
    self.noeuds+=1
    self.matrice.append([0 for i in range(self.noeuds)])

  def modifArrete(self,noeud1,noeud2,poids):
    rang1=self.noms.index(noeud1)
    rang2=self.noms.index(noeud2)
    self.matrice[rang1][rang2]=poids
    self.matrice[rang2][rang1]=poids

  def effaceNoeud(self,nom):
    rang=self.noms.index(nom)
    for i in range(self.noeuds):
      del self.matrice[i][rang]
    self.matrice.pop(rang)
    self.noms.pop(rang)
    self.noeuds-=1

  def dijkstra(self, depart, arrivee):
    distances = {noeud: float('inf') for noeud in self.noms}
    distances[depart] = 0
    listeDistances = [0]
    listeNoeuds = [depart]

    while len(listeDistances)>0:
      distanceCourante,noeudCourant = min(listeDistances),listeNoeuds[listeDistances.index(min(listeDistances))]
      del listeNoeuds[listeDistances.index(min(listeDistances))]
      listeDistances.remove(min(listeDistances))
      if distanceCourante > distances[noeudCourant]:
        continue
      for i, poids in enumerate(self.matrice[self.noms.index(noeudCourant)]):
        if poids > 0:
          nouvelleDistance = distanceCourante + poids
          if nouvelleDistance < distances[self.noms[i]]:
            distances[self.noms[i]] = nouvelleDistance
            listeNoeuds.append(self.noms[i])
            listeDistances.append(nouvelleDistance)
    return distances[arrivee]

  def bellmanFord(self, depart, arrivee):
    inf = float('inf')
    distances = {noeud: inf for noeud in self.noms}
    distances[depart] = 0
    noeuds = [noeud for noeud in self.noms]
    precedents = {}
    chemin = [arrivee]

    for _ in range(self.noeuds - 1):
      for noeud in noeuds:
        for i, poids in enumerate(self.matrice[self.noms.index(noeud)]):
          if poids != 0:
            nouvelleDistance = distances[noeud] + poids
            if nouvelleDistance < distances[self.noms[i]]:
              distances[self.noms[i]] = nouvelleDistance
              precedents[self.noms[i]]=noeud
    if arrivee not in precedents:
      chemin = "Il n'y a pas de chemin possible."
    else:
      while depart not in chemin:
        chemin.append(precedents[chemin[-1]])
      chemin=chemin[::-1]

    return chemin
    #return distances[arrivee]

graph = Graph([
        [0,1,0,0,0,1,1],
        [1,0,1,0,0,1,1],
        [0,1,0,0,1,0,1],
        [0,0,0,0,1,0,0],
        [0,0,1,1,0,0,0],
        [1,1,0,0,0,0,1],
        [1,1,1,0,0,1,0]])

graph.ajoutNoeud('h')
graph.modifArrete('h','c',1)
#graph.modifArrete('e','c',0)
graph.modifArrete('g','h',1)
graph.effaceNoeud('f')

print(graph)
print("distance minimale entre a et d :",graph.dijkstra('a','d'))
print("distance minimale entre a et d :",graph.bellmanFord('a','d'))