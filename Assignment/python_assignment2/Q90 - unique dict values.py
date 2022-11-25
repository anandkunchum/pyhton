#Q90. Write a Python program to extract unquire dictionary values.

dict_a = {"list_a":[1,2,3,4,5], "list_b":[3,4,5,6,7], "list_c":[7,8,9,10]}

list_result = []

for key in dict_a:
    list_result.extend(dict_a[key])

list_unique = list(set(list_result))

print('Extracted unique dictionary values :', list_unique)