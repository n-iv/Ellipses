table1 = [0,1,2,3]
table2 = table1 # table2 pointe vers table1
table2[0]=4 # table1 change son contenu
print(table1) # On obtient [4,1,2,3] car les deux tableaux pointent la même adresse mémoire
table3 = table1[:] # table3 est un tableau identique à table1 : [4,1,2,3], mais il n'est pas placé à la même adresse mémoire
table3[1]=4 # table3 change son contenu mais table1 reste le même
print(table1) # On obtient [4,1,2,3]
print(table3) # On obtient [4,4,2,3]