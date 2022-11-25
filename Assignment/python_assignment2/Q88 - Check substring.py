#Q88. Write a Python program to check if a substring is present in a given string.

var_str = "Welcome to iNeuron"
sub_str = input('Enter sub-string:')
print('String:',var_str)
if var_str.__contains__(sub_str):
    print('Given substring is preset in String')
else:
    print('Given substring is NOT preset in String')
