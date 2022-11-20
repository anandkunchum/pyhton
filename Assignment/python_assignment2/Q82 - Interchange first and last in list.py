#Q82. Write a Python program to interchange the first and last element in a list.

lst = ['a','b','c','d','e',1,2,3,4,5]

print('Actual list:', lst)

#logic to interchange first and last elements
temp_var = lst[0]
lst[0] = lst[-1]
lst[-1] = temp_var

print('updated list:', lst)