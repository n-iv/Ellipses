n=int(input("An odd number plz :  "))
while n%2==0:
  n=int(input("It is not an odd number. Give an odd number  :     ")) 
  
L=[['\033[34m'+"■" for i in range(n)]for j in range(n)]
for i in range(n):
  for j in range(n):
    if n//2==i-1 or n//2==j-1 or n//2==i+1 or n//2==j+1 or i==j+1 or j==n-i or i==j-1 or j==n-i-2:
      L[i][j]="\033[0m"+"■"
    if n//2==i or n//2==j or i==j or j==n-i-1:
      L[i][j]="\033[31m"+"■"
      

for i in L:
  print(" ".join(i))