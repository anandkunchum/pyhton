#Q80. Write a Python program to check Armstrong Number

given_num = input('Enter number :')

if given_num == given_num[-1::-1]:
    print('Given number is Armstrong number')
else:
    print('Given number is NOT Armstrong number')
