from random import random
from math import log
from numpy import exp

p = lambda _: str(int(round(_*100)))

q = lambda _: str(round(_/10**6))+"m" if abs(_)>=10**6 else str(round(_/10**3))+"k" if abs(_)>=10**3 else str(round(_)) if _>=1 else str(round(_*100)/100)

def affCa():
  print("Accuracy =", p(BestAccuracy))
  for row in Best:
    print(
      [
        str(neuron) if neuron is not None else "None"
        for neuron in row
      ]
    )
  for out in range(21):
    print(out - 10, "-->", q(BestOutput[out][0]))

def ca():
  result = 0
  for output,fin in L:
    if output/fin < 0:
      result -=.5
    elif abs(output) > 10**3:
      result-=.05*log(abs(output),10)
    else:
      result+=1/(abs(output - fin)+1)
  return result / len(L)

class Neurone:
    def __init__(self):
        self.p1 = 2*random()-1
        self.p2 = 2*random()-1
        self.p3 = 2*random()-1
        self.p4 = 2*random()-1
    def __str__(self):
      return p(self.p1)+"|"+p(self.p2)+"|"+p(self.p3)+"|"+p(self.p4)

    def f(self, x, y=0, z=0):
        return self.p1 * 1/(1+exp(x)) + self.p2 * y **2 + self.p3 * z + self.p4

nb_test = 100000
BestOutput = None
Best = None
BestAccuracy = 0

for _ in range(nb_test):
    L = []
    M = [
        [Neurone(), Neurone(), Neurone()],
        [Neurone(), Neurone(), None],
        [Neurone(), None, None],
    ]
    for i in range(-10, 11):
        fin = 1 if i >= 0 else -1
        L.append(
            (
                M[2][0].f(
                    M[1][0].f(M[0][0].f(i), M[0][1].f(i), M[0][2].f(i)),
                    M[1][1].f(M[0][0].f(i), M[0][1].f(i), M[0][2].f(i)),
                    M[0][1].f(i)
                ),
                fin,
            )
        )

    # Calculate accuracy for the current matrix
    #current_accuracy = sum(       (output - fin) / output if output != 0 else 1 for output, fin in L) / len(L)
    current_accuracy = ca()
    if current_accuracy > BestAccuracy:
        BestOutput = L
        BestAccuracy = current_accuracy
        Best = M
        affCa()
        print("******************************")

print("Best Matrix:")
if Best is not None:
    affCa()
else:
    print("No best matrix found.")