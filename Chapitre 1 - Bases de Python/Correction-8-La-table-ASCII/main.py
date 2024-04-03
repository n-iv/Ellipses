resultat = ""

for val in "66 111 110 106 111 117 114".split(" "):
  resultat +=chr(int(val))

print(resultat)

resultat = ""

for car in "Et voilà !":
  resultat+=str(hex(ord(car)))+" "

print(resultat)