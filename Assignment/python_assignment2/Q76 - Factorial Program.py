#Q76. Write a Python program to find the factorial of a given number

num = int(input('Enter number :'))
result = 1
for number in range(1,num+1):
    result = number * result
print('Factorial of given number :',result)