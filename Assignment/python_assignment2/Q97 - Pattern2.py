#Q97. Write a python program to print below pattern.
#    *
#   **
#  ***
# ****
#*****

num = 5

for i in range(1,num+1):
    for j in range(0, num+1):
        if j <= (num - i):
            print(" " , end="")
        else:
            print("*" , end="")
    print(end='\n')