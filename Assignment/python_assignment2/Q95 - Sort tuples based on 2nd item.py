#Q95. Write a Python program to sort a list of tuples by second item.
#Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
#Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]

list_a = [('for', 24), ('Geeks', 8), ('Geeks', 30)] 

lst = len(list_a)
for i in range(0, lst):
    for j in range(0, lst-i-1):
        if (list_a[j][1] > list_a[j + 1][1]):
            temp = list_a[j]
            list_a[j]= list_a[j + 1]
            list_a[j + 1]= temp
print(list_a)

    