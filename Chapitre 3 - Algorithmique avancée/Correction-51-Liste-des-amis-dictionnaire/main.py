relations = {
  "Matthieu":("Claire","Charly"),
  "Claire":("Matthieu","Sébastien","Charly"),
  "Sébastien":("Claire","Alice"),
  "Alice":("Sébastien","Charly","Aurélie"),
  "Charly":("Matthieu","Claire","Alice"),
  "Aurélie":("Alice")
}

def listeAmis(a):
  return "Les amis de "+a+" sont "+", ".join(relations[a]) #donne la liste des amis d'une personne a

print(listeAmis("Matthieu"))