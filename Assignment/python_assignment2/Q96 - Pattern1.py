#Q96. Write a python program to print below pattern.
#* 
#* * 
#* * * 
#* * * * 
#* * * * * 

num = 5
 
for i in range(0,num):
    for j in range(0,num):
        if i < j :
            print(" " , end="")
        else:
            print("* " , end="")
    print(end='\n')