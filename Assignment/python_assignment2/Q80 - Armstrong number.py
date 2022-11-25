#Q80. Write a Python program to check Armstrong Number

given_num = input('Enter number :')
given_num_int = int(given_num)
result_num = 0

for position in range(0,len(given_num)):
    result_num += int(given_num[position]) ** 3

if given_num_int == result_num:
    print('Given number is Armstrong number')
else:
    print('Given number is NOT Armstrong number')
