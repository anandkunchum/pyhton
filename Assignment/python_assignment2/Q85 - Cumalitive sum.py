#Q85. Write a Python program to find cumulative sum of a list.

lst = [4, 10, 15, 18, 20, 30, 40, 50]
result_list = []
sum = 0
print('Actual list:',lst)
for item in lst:
    sum += item
    result_list.append(sum)
print('Cumulative sum list :',result_list)
