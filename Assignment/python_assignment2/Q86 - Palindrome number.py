#Q86. Write a Python program to check if a string is palindrome or not.

given_num = input('Enter number :')

if given_num == given_num[-1::-1]:
    print('Given number is palindrome')
else:
    print('Given number is NOT palindrome')