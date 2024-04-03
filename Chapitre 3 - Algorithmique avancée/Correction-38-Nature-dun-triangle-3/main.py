import math

# Question 7)
def presquEgales(a,b):
  return math.fabs(a/b-1)<10**-15

def distance2(abs1, ord1, abs2, ord2):
  return (abs2-abs1)**2 + (ord2-ord1)**2

def identiques(a,b,c):
  if presquEgales(a,b) and presquEgales(a,c):
    return 3
  if presquEgales(a,b) or presquEgales(a,c) or presquEgales(b,c):
    return 2
  return 0

def rectangle(a,b,c):
  if a>c:
    a,c=c,a
  if b>c:
    b,c=c,b
  if presquEgales(a+b,c):
    return "rectangle"
  return "non rectangle"

def nature(a,b,c):
  if identiques(a,b,c) == 3:
    return "équilatéral"
  if identiques(a,b,c) ==2:
    return "isocèle "+rectangle(a,b,c)
  return "scalène "+rectangle(a,b,c)

print(nature(distance2(1,3,1,-1),distance2(1,-1,4,-1),distance2(4,-1,1,3)))
print(nature(distance2(0,1,-2,4),distance2(-2,4,2,4),distance2(2,4,0,1)))
print(nature(distance2(2,-2,1,-1),distance2(1,-1,3,-1),distance2(3,-1,2,-2)))
print(nature(distance2(0,0,2,0),distance2(2,0,1,math.sqrt(3)),distance2(1,math.sqrt(3),0,0)))
print(nature(distance2(0,0,0,1),distance2(0,1,1,10**-10),distance2(1,0,0,10**-10)))
