#Q98. Write a python program to print below pattern.
#    * 
#   * * 
#  * * * 
# * * * * 
#* * * * * 

num = 5
k = num

for i in range(0 , num):  
    for j in range(0 , k):  
        print(" " , end="") 
    k = k - 1  
    for j in range(0, i + 1):  
        print("* " , end="")
    print(end="\n")