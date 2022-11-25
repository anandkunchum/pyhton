# Q99. Write a python program to print below pattern.
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

num = 5
 
for i in range(1,num+1):
    for j in range(1,num+1):
        if i < j :
            print(" " , end=" ")
        else:
            print(j, end=" ")
    print(end='\n')