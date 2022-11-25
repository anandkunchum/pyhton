#Q93. Write a Python program to create a list of tuples from given list having number and its cube in each tuple.
#Input: list = [9, 5, 6]
#Output: [(9, 729), (5, 125), (6, 216)]

list_a = [9, 5, 6]
list_result = []

for position in range(0,len(list_a)):
    (a,b) = (list_a[position],list_a[position] ** 3)
    list_result.append((a,b))

print(list_result)