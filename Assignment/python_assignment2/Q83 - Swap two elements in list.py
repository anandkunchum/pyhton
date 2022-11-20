#Q83. Write a Python program to swap two elements in a list.

lst = ['a','b','c','d','e',1,2,3,4,5]

print('Actual list:', lst)

first_position = int(input('Enter the first element position:'))
second_position = int(input('Enter the second element position:'))

print('SWAP two elements..')

#logic to interchange first and last elements
temp_var = lst[first_position - 1]
lst[first_position - 1] = lst[second_position - 1]
lst[second_position - 1] = temp_var

print('updated list:', lst)

