#Q84. Write a Python program to find N largest element from a list.

lst = [12,43,13,2,4,6,10,5,11,74,32,2]

print('Actual list',lst)
given_num = int(input('Enter any number for n :'))

list_result = list(set(lst))
list_result.sort()

print('nth largest number in the list :', list_result[-1 * given_num])


