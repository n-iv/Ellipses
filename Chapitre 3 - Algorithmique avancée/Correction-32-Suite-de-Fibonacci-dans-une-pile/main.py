pile = [1,1]

while len(pile)<10:
  a = pile.pop()
  b = pile.pop()
  pile.append(b)
  pile.append(a)
  pile.append(a+b)

print(pile)
