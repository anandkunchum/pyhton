
#Q79. Write a Python program to check if a number is prime or not.

given_num = int(input('Enter number :'))
factors_count = 0
for number in range(2,given_num):
    if given_num % number == 0:
        factors_count += 1
if factors_count == 0 or given_num == 1:
    print('Given number is Prime')
else:
    print('Given number is NOT Prime')