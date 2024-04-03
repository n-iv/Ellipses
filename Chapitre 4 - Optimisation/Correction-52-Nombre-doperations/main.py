def nbOperationsFibonacci(n):
  if n in [1, 2]:
      return 0
  return 1+nbOperationsFibonacci(n-1)+nbOperationsFibonacci(n-2)

print(nbOperationsFibonacci(10)==54)
print("Attention, le prochain résultat prend un peu plus de 30 secondes à apparaître.")
print(nbOperationsFibonacci(40)==102334154)