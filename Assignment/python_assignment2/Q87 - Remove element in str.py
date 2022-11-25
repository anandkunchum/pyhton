#Q87. Write a Python program to remove i'th element from a string.

var_str = "Welcome to iNeuron"
new_str = ""
remove_position = int(input('Enter position of the element to remove :'))
print(var_str)
for i in range(0,len(var_str)):
    if i != (remove_position - 1):
        new_str += var_str[i]
print(new_str)