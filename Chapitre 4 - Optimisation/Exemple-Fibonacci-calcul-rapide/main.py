def fibonacci(n):
  a, b = 0, 1
  for i in range(1,n):
      a, b = b, a+b
  return b

r = str(fibonacci(1000))
print(f'Le millième terme de la suite de Fibonacci a {len(r)} chiffres et vaut {r}.')