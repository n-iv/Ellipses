import math

# Question 1)
def distance2(abs1, ord1, abs2, ord2):
  return (abs2-abs1)**2 + (ord2-ord1)**2

# Question 2)
def identiques(a,b,c):
  if a==b and a==c:
    return 3
  if a==b or a==c or b==c:
    return 2
  return 0

# Question 3)
def rectangle(a,b,c):
  if a>c:
    a,c=c,a
  if b>c:
    b,c=c,b
  if a + b == c:
    return "rectangle"
  return "non rectangle"

# Question 4)
def nature(a,b,c):
  if identiques(a,b,c) == 3:
    return "équilatéral"
  if identiques(a,b,c) ==2:
    return "isocèle "+rectangle(a,b,c)
  return "scalène "+rectangle(a,b,c)

# Question 5)
print(nature(distance2(1,3,1,-1),distance2(1,-1,4,-1),distance2(4,-1,1,3)))
print(nature(distance2(0,1,-2,4),distance2(-2,4,2,4),distance2(2,4,0,1)))
print(nature(distance2(2,-2,1,-1),distance2(1,-1,3,-1),distance2(3,-1,2,-2)))
print(nature(distance2(0,0,2,0),distance2(2,0,1,math.sqrt(3)),distance2(1,math.sqrt(3),0,0)))
