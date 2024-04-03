relations = [
  [0,1,0,0,1,0],
  [1,0,1,0,1,0],
  [0,1,0,1,0,0],
  [0,0,1,0,1,1],
  [1,1,0,1,0,0],
  [0,0,0,1,0,0]
]

noms = {1:"Matthieu",2:"Claire",3:"Sébastien",4:"Alice",5:"Charly",6:"Aurélie"}
numeros = {"Matthieu":1,"Claire":2,"Sébastien":3,"Alice":4,"Charly":5,"Aurélie":6}

def listeAmis(a):#donne la liste des amis d'une personne a
  amis=[]
  i=numeros[a]
  for j in range(len(relations[i-1])):
    if relations[i-1][j]==1:
      amis+=[noms[j+1]]
  return "Les amis de "+a+" sont "+", ".join(amis)

print(listeAmis("Sébastien"))