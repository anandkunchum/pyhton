# Q100. Write a python program to print below pattern.
# A 
# B B 
# C C C 
# D D D D 
# E E E E E 

alphabets = ['A','B','C','D','E','F','G','H','I','J']

num = 5
 
for i in range(0,num):
    for j in range(0,num):
        if i < j :
            print(" " , end=" ")
        else:
            print(alphabets[i], end=" ")
    print(end='\n')