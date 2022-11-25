#Q91. Write a Python program to merge two dictionary.

dict_a = {"name":"Anand","city":"vizag"}
dict_b = {"company":"Renault","bike":"RE"}

dict_result = dict_a

for key, value in dict_b.items():
    dict_result[key] = value

print(dict_result)