#Question 1 :
n=int(input("Entrez un nombre impair :  "))
while n%2==0:
  n=int(input("Ce n'est pas un nombre impair. Entrez un nombre impair : "))

#Question 2 :
drapeau=[["." for i in range(n)] for j in range(n)]

#Question 3 :
for i in range(n):
  for j in range(n):
    if n//2==i or n//2==j or i==j or j==n-i-1:
      drapeau[i][j]="*"

#Question 4 :
for ligne in drapeau:
  aff=""
  for caractere in ligne :
    aff+=caractere+' '
  print(aff)