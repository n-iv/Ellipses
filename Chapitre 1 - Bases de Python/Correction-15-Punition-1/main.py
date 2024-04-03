pronoms=["Je","Tu","Il","Nous","Vous","Ils"]
verbes=["dois","dois","doit","devons","devez","doivent"]
adjectifs=["concentré","concentré","concentré", "concentrés","concentrés","concentrés"]
for i in range(50):
  print(pronoms[i%6],"ne",verbes[i%6]," pas parler en classe, mais rester", adjectifs[i%6], "et travailler assidûment.")